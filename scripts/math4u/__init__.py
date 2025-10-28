from fileinput import filename
from pathlib import Path
import yaml
import subprocess
import os
import logging
import shutil
import pandas as pd
import rich
from math4u.snippets import makeHEAD, FOOT, file_action, figure_name, LATEXFILE_HEADER, LATEXFILE_FOOT

from datetime import datetime
now = datetime.now()

langs = ["en", "es", "cs", "sk", "pl"]

DIR_PATH = Path("..")
DIR_OLDPATH = Path("../../math4u")

df_image_settings = pd.read_csv("image2pdf_setting.csv", dtype=str)

# find directories ../00*
directories = [d.name for d in DIR_PATH.iterdir() if d.is_dir() and d.name.startswith("00")]
# sort directories by name
directories.sort()

class Problem:
    def __init__(self, directory=None, number=None):
        if directory is not None:
            self.directory = directory
        else:
            # find directory from number, the directory name is in directories and 
            # starts with the number, like ../00023_Title_of_problem
            if number is None:
                raise ValueError("Either directory or number must be provided")
            dir_name = [i for i in directories if f"{number:05d}" in i]
            if not dir_name:
                raise ValueError(f"Problem with number {number} not found")
            if len(dir_name) > 1:
                raise ValueError(f"Multiple problems with number {number} found: {dir_name}")
            dir_name = dir_name[0]
            self.directory = dir_name
        # return file directory/cs_article.md
        self.files = {lang: Path(self.directory) / f"{lang}_article.md" for lang in langs}
        self.Files = [File(self.files[lang], parent=self) 
                      for lang in langs if (Path(DIR_PATH)/(self.files[lang])).exists()]

    def __repr__(self):
        return f"Problem(directory={self.directory})"
    
    def copy_files_from_repository(self, skip_md=True, target="_site"):
        # copy all files from DIR_PATH to _site/directory
        target_dir = Path(target) / self.directory
        target_dir.mkdir(parents=True, exist_ok=True)
        # find all files in DIR_PATH/directory
        source_dir = DIR_PATH / self.directory
        for file in source_dir.iterdir():
            if file.is_file():
                if skip_md and file.suffix == ".md":
                    continue
                target_file = target_dir / file.name
                shutil.copy2(file, target_file)
                

class File:
    def __init__(self, path, parent=None):
        self.path = Path(path)
        self.language = self.path.name.split("_")[0]
        self.content = (DIR_PATH / self.path).read_text(encoding="utf-8")
        self.yaml_header = self._extract_yaml_header()
        self.parent = parent

    def _extract_yaml_header(self):
        if self.content.startswith("---"):
            end = self.content.find("\n---", 3)
            if end != -1:
                yaml_content = self.content[3:end]
                try:
                    return yaml.safe_load(yaml_content)
                except yaml.YAMLError as e:
                    logging.error(f"YAML parsing error in file {self.path}: {e}")
                return {}
        return {}
    
    def __repr__(self):
        return f"File(path={self.path}, language={self.language})"
    
    @property
    def html_content(self, ini_path=DIR_PATH):
        file_content = subprocess.run(
                ["pandoc", 
                 "--mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js",
                 f"{ini_path}/{self.path}"
                 ],     
                capture_output = True, # Python >= 3.7 only
                text = True # Python >= 3.7 only
                )
        file_content = file_content.stdout
        file_content = f"<div class='problem_body'> {file_content} </div>"
        file_content =  file_content.replace(
            "<blockquote>",
            "<div class='alert alert-primary'>"        
            )
        file_content =  file_content.replace(
            "</blockquote>",
            "</div>"        
            )
        file_content =  file_content.replace(r"\iffalse","")
        file_content =  file_content.replace(r"\fi","")
        for i in range(1,20):
            file_content =  file_content.replace(
            "<figcaption>",
                f"<figcaption >{figure_name[self.language]} {i}. ", 1        
            )
        file_content =  file_content.replace(
            "<figcaption >",
            "<figcaption>"        
            )
        return file_content

    @property
    def latex_content(self):
        file_content = subprocess.run(
                ["pandoc", 
                 "-f", "markdown",
                 "-t", "latex",
                 f"{DIR_PATH}/{self.path}"
                 ],     
                capture_output = True, # Python >= 3.7 only
                text = True # Python >= 3.7 only
                )
        file_content = file_content.stdout
        return file_content

    @property
    def latex_old_content(self):
        file_content = subprocess.run(
                ["pandoc", 
                 "-f", "markdown",
                 "-t", "latex",
                 f"{DIR_PATH}/{str(self.path).replace('.md', '_old.md')}"
                 ],     
                capture_output = True, # Python >= 3.7 only
                text = True # Python >= 3.7 only
                )
        file_content = file_content.stdout
        return file_content

    def to_html(self):
        target = Path("_site") / self.path.parent/ f"{self.language}_article.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        css = ""    
        test_css_file = f"{DIR_PATH}/{self.path.parent.name}/article.css"
        if os.path.isfile(test_css_file):
            with open(test_css_file) as f:
                css = "\n".join(f.readlines())
        html_page = makeHEAD(css=css, title=self.path)
        html_page += f"Workflow: {self.yaml_header.get('workflow','unknown')}<br>\n"
        keywords = self.yaml_header.get('keywords', [])
        if keywords:
            html_page += f"<div class='header_keywords'>Keywords: <span>{'; '.join(keywords)}</span></div>\n"
        html_page += f"<div class='time'>Last update: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>\n"
        html_page += "<hr>\n"
        html_page += self.html_content
        html_page += file_action
        html_page += FOOT
        target.write_text(html_page, encoding="utf-8")
        return target

    # def pandiff(self):
    #     target = Path("_site") / self.path.parent/ f"{self.language}_article_diff.html"
    #     target.parent.mkdir(parents=True, exist_ok=True)
    #     new_file = f"{DIR_PATH}/{self.path}"
    #     old_file = f"{DIR_OLDPATH}/{self.path}"
    #     if not os.path.isfile(old_file):
    #         raise FileNotFoundError(old_file)
    #         return
    #     print(f"Comparing {new_file} to {old_file}")
    #     diff_output = subprocess.run(
    #             ["pandiff", 
    #              old_file,
    #              new_file,
    #              "--output", 
    #              str(target),
    #              "-s"
    #              ],     
    #             capture_output = True, # Python >= 3.7 only
    #             text = True # Python >= 3.7 only
    #             )
    #     # check if pandiff was successful
    #     if diff_output.returncode != 0:
    #         # error occurred
    #         print(f"pandiff failed: {diff_output.stderr}")
    #     return target
    
    # def to_pdf(self, output_path=None, remove_iffalse=True):
    #     content = self.latex_content
    #     if remove_iffalse:
    #         content = content.replace(r"\iffalse","").replace(r"\fi","")
    #     temp_tex = Path("_temp") / self.parent.directory /f"{self.language}_article.tex"
    #     # create parent directory
    #     temp_tex.parent.mkdir(parents=True, exist_ok=True)
    #     # copy all files from problem directory to _temp/problem_directory
    #     self.parent.copy_files_from_repository(skip_md=True, target="_temp")
    #     temp_tex.write_text(LATEXFILE_HEADER + content + LATEXFILE_FOOT, encoding="utf-8")
    #     cmd = ["xelatex", str(temp_tex)]
    #     proc = subprocess.run(cmd, capture_output=True, text=True)
    #     if proc.returncode != 0:
    #         print(f"pdflatex failed: {proc.stderr}")

    def to_pdf(self, output_path=None):
        content = self.latex_content
        old_content = self.latex_old_content
        def osetri_text(text):
            text = text.replace(u'\u2006'," ")
            text = text.replace(u'\u2004'," ")
            text = text.replace(r'\begin{figure}',r'\begin{figure}[H]')
            text = text.replace(r'.svg',r'.pdf')
            text = text.replace(r'\includesvg[keepaspectratio]', r'\includegraphics')
            text = text.replace(r'\textbackslash iffalse',r'\iffalse')
            text = text.replace(r'\textbackslash fi',r'\fi')

            return {'reduced':text, 'full':text.replace(r"\iffalse","").replace(r"\fi","")}

        def osetri_soubor(text):
            babel = ""
            if self.language=="cs":
                babel = r"\usepackage[czech]{babel}"
            if self.language=="sk":
                babel = r"\usepackage[slovak]{babel}"
            if self.language=="pl":
                babel = r"\usepackage[polish]{babel}"
            if self.language=="es":
                babel = r"\usepackage[spanish]{babel}"
            text = text.replace("%%%BABEL",babel)
 
            keywords = self.yaml_header.get("keywords", [])
            kwds = ', '.join(keywords)
            metadata = f"""
                \\def\\meta{{
                Keywords:  {kwds} 

                }}
                """
            text = text.replace("%%%METADATA",metadata)
            for n,i,s in df_image_settings[df_image_settings['number']==self.parent.directory[:5]].values:
                text = text.replace(r"\includegraphics{"+i+"}",r"\oldincludegraphics["+s+"]{"+i+"}")

            return text
        
        content = osetri_text(content)['full']
        old_content = osetri_text(old_content)['full']
        LATEXFILE_HEADER_ = LATEXFILE_HEADER.replace("%%%GRAPHICSPATH", r"\graphicspath{{../../}{../}{}{../../../"+self.parent.directory+"/}}")

        temp_tex = Path("_temp") / self.parent.directory / f"{self.language}_article.tex"
        temp_tex_old = Path("_temp") / self.parent.directory / f"{self.language}_article_old.tex"
        tex_dir = temp_tex.parent  # adresář, kde bude probíhat kompilace

        # vytvoření adresáře
        tex_dir.mkdir(parents=True, exist_ok=True)

        # zkopírování všech potřebných souborů
        # self.parent.copy_files_from_repository(skip_md=True, target="_temp")

        # zapsání latexového souboru
        temp_tex.write_text(osetri_soubor(LATEXFILE_HEADER_ + content + LATEXFILE_FOOT), 
                            encoding="utf-8")
        temp_tex_old.write_text(osetri_soubor(LATEXFILE_HEADER_ + old_content + LATEXFILE_FOOT), 
                                encoding="utf-8")

        # spuštění kompilace v adresáři, kde je tex soubor
        cmd = ["xelatex", temp_tex.name]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=tex_dir)
        if proc.returncode != 0:
            print(f"xelatex failed: {proc.stderr}")
        else:
            print("PDF compilation succeeded.")

        # latexdiff
        diff_tex = Path("_temp") / self.parent.directory / f"{self.language}_article_diff.tex"
        cmd_diff = ["latexdiff", temp_tex_old.name, temp_tex.name]
        with open(diff_tex, "w", encoding="utf-8") as f:
            proc_diff = subprocess.run(cmd_diff, stdout=f, stderr=subprocess.PIPE,
                                       text=True, cwd=tex_dir)
        if proc_diff.returncode != 0:
            print(f"latexdiff failed: {proc_diff.stderr}")
        else:
            print("latexdiff generation succeeded.")
        # kompilace
        cmd = ["xelatex", diff_tex.name]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=tex_dir)        
        if proc_diff.returncode != 0:
            print(f"latex of diff failed: {proc_diff.stderr}")
        else:
            print("Latex diff generation succeeded.")

        if output_path:
            output_pdf = tex_dir / f"{self.language}_article.pdf"
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            if output_pdf.exists():
                output_pdf.replace(output_path)

            output_pdf = tex_dir / f"{self.language}_article_diff.pdf"
            output_path = Path(output_path.parent) / f"{self.language}_article_diff.pdf"
            if output_pdf.exists():
                output_pdf.replace(output_path)

def get_problem(directory):
    return Problem(directory)

def get_all_problems():
    base_path = Path(__file__).parent.parent
    problem_dirs = [p for p in base_path.iterdir() if p.is_dir() and p.name.startswith("00")]
    return [get_problem(p) for p in problem_dirs]