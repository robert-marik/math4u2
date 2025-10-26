"""
LaTeX Compiler library (object-oriented)

Provides a simple Python class `LatexCompiler` to compile LaTeX source into PDF
using a LaTeX engine (pdflatex, xelatex, lualatex).

Features:
- compile from string or file
- configurable engine, number of runs, bibtex support, timeout
- captures stdout/stderr and returns a result object
- optional cleaning of intermediate files

Usage (high-level):
- from latex_compiler import LatexCompiler
- compiler = LatexCompiler(engine='pdflatex', runs=2)
- result = compiler.compile_string(my_tex_source)
- if result.success: print('PDF:', result.pdf_path)
- else: print('Errors:', result.log)

This file is intended as a single-file lightweight library suitable for
embedding in projects or expanding further.
"""

from __future__ import annotations

import subprocess
import tempfile
import shutil
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Tuple


@dataclass
class CompileResult:
    success: bool
    pdf_path: Optional[Path]
    log: str
    stdout: str
    stderr: str
    workdir: Optional[Path] = None


class LatexCompilationError(Exception):
    pass


class LatexCompiler:
    """Object-oriented LaTeX compiler wrapper.

    Parameters
    ----------
    engine: str
        LaTeX engine to use (e.g. 'pdflatex', 'xelatex', 'lualatex').
    runs: int
        How many times to run the engine (often 1-3; bibliography may need extra runs).
    bibtex: bool
        Whether to run bibtex between runs (if .aux appears and bibliography is used).
    timeout: int
        Per-run timeout in seconds.
    keep_intermediates: bool
        Whether to keep .aux/.log/.out files in the working directory (default False).
    extra_args: Optional[List[str]]
        Extra command-line args to pass to the LaTeX engine (e.g. ['-interaction=nonstopmode']).
    """

    def __init__(
        self,
        engine: str = "pdflatex",
        runs: int = 2,
        bibtex: bool = False,
        timeout: int = 30,
        keep_intermediates: bool = False,
        extra_args: Optional[List[str]] = None,
    ) -> None:
        self.engine = engine
        self.runs = max(1, int(runs))
        self.bibtex = bool(bibtex)
        self.timeout = int(timeout)
        self.keep_intermediates = bool(keep_intermediates)
        self.extra_args = extra_args or ["-interaction=nonstopmode", "-halt-on-error"]

    def _run(self, cmd: List[str], cwd: Path) -> Tuple[subprocess.CompletedProcess, str]:
        """Run a command in cwd. Return (CompletedProcess, combined_output).
        """
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(cwd),
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
        except subprocess.TimeoutExpired as e:
            raise LatexCompilationError(f"LaTeX run timed out after {self.timeout}s: {e}")

        combined = "\n".join([proc.stdout or "", proc.stderr or ""]) or ""
        return proc, combined

    def _run_bibtex(self, aux_basename: str, cwd: Path) -> Tuple[subprocess.CompletedProcess, str]:
        cmd = ["bibtex", aux_basename]
        return self._run(cmd, cwd)

    def compile_string(self, source: str, output_path: Optional[Path] = None, tex_filename: str = "document.tex") -> CompileResult:
        """Compile LaTeX source given as a string.

        If output_path is provided and successful, the produced PDF will be moved there.
        output_path may be a directory or a full filename. If not provided, the PDF stays
        in the temporary workdir and `result.pdf_path` points to it.
        """
        with tempfile.TemporaryDirectory() as td:
            workdir = Path(td)
            tex_file = workdir / tex_filename
            tex_file.write_text(source, encoding="utf-8")
            return self._compile_tex_file(tex_file, output_path, workdir)

    def compile_file(self, input_path: Path, output_path: Optional[Path] = None) -> CompileResult:
        """Compile an existing .tex file.

        A temporary working directory is used and the input file (and its resources) are copied there.
        """
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(input_path)

        with tempfile.TemporaryDirectory() as td:
            workdir = Path(td)
            # copy the input file and sibling resources (same dir) into workdir
            shutil.copy2(str(input_path), str(workdir / input_path.name))

            # copy helper files in same directory referenced by relative paths (basic approach)
            for p in input_path.parent.iterdir():
                if p == input_path:
                    continue
                # copy common inclusions: images, .sty, .bib in the same folder
                if p.suffix.lower() in {'.sty', '.bib', '.png', '.jpg', '.jpeg', '.pdf', '.eps'}:
                    try:
                        shutil.copy2(str(p), str(workdir / p.name))
                    except Exception:
                        pass

            tex_file = workdir / input_path.name
            return self._compile_tex_file(tex_file, output_path, workdir)

    def _compile_tex_file(self, tex_file: Path, output_path: Optional[Path], workdir: Path) -> CompileResult:
        """Internal compile implementation. Workdir is already prepared and current files exist there."""
        basename = tex_file.stem
        log_accumulator: List[str] = []

        pdf_path: Optional[Path] = None

        for run in range(1, self.runs + 1):
            cmd = [self.engine] + self.extra_args + [str(tex_file.name)]
            try:
                proc, combined = self._run(cmd, workdir)
            except LatexCompilationError as e:
                return CompileResult(False, None, str(e), "", "", workdir if self.keep_intermediates else None)

            log_accumulator.append(f"--- Run {run} ({' '.join(cmd)}) ---\n")
            log_accumulator.append(combined)

            # if bibtex flag is set and .aux appears after first run, run bibtex once
            aux_file = workdir / (basename + ".aux")
            if run == 1 and self.bibtex and aux_file.exists():
                try:
                    bibproc, bibout = self._run_bibtex(basename, workdir)
                    log_accumulator.append("--- bibtex ---\n")
                    log_accumulator.append(bibout)
                except LatexCompilationError as e:
                    log_accumulator.append(f"BibTeX error: {e}")

            # quick heuristic: if engine returned nonzero code and contains '!' or 'Error', we may abort early
            if proc.returncode != 0:
                # continue collecting outputs but break after last run
                pass

        # check for produced PDF
        candidate = workdir / (basename + ".pdf")
        if candidate.exists():
            pdf_path = candidate
            # move to output if requested
            if output_path:
                out = Path(output_path)
                if out.is_dir():
                    out_pdf = out / candidate.name
                else:
                    # parent dir
                    out.parent.mkdir(parents=True, exist_ok=True)
                    out_pdf = out
                shutil.move(str(candidate), str(out_pdf))
                pdf_path = out_pdf
        else:
            # failed: try to return log and collected stdout/stderr
            combined_log = "\n".join(log_accumulator)
            return CompileResult(False, None, combined_log, "", "", workdir if self.keep_intermediates else None)

        combined_log = "\n".join(log_accumulator)

        # cleanup if requested
        if not self.keep_intermediates:
            for ext in ['.aux', '.log', '.out', '.toc', '.bbl', '.blg', '.lof', '.lot']:
                p = workdir / (basename + ext)
                try:
                    if p.exists():
                        p.unlink()
                except Exception:
                    pass
            # if we moved pdf to output, no need to keep tmp dir
            return CompileResult(True, pdf_path, combined_log, "", "", None)
        else:
            return CompileResult(True, pdf_path, combined_log, "", "", workdir)


# Small CLI convenience
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Simple LaTeX compiler')
    parser.add_argument('input', help='Path to .tex file to compile (or - for stdin)')
    parser.add_argument('--engine', default='pdflatex', help='LaTeX engine (pdflatex/xelatex/lualatex)')
    parser.add_argument('--runs', type=int, default=2, help='Number of engine runs')
    parser.add_argument('--bibtex', action='store_true', help='Run bibtex if needed')
    parser.add_argument('--out', default=None, help='Output PDF path or directory')
    parser.add_argument('--keep', action='store_true', help='Keep intermediate files')
    args = parser.parse_args()

    compiler = LatexCompiler(engine=args.engine, runs=args.runs, bibtex=args.bibtex, keep_intermediates=args.keep)

    if args.input == '-':
        source = sys.stdin.read()
        res = compiler.compile_string(source, output_path=Path(args.out) if args.out else None)
    else:
        res = compiler.compile_file(Path(args.input), output_path=Path(args.out) if args.out else None)

    if res.success:
        print('Compiled PDF:', res.pdf_path)
    else:
        print('Compilation failed. Log:\n')
        print(res.log)
