from fileinput import filename
from pathlib import Path
import yaml
import subprocess
import os
import logging
import shutil
import pandas as pd
import rich

from datetime import datetime
now = datetime.now()

langs = ["en", "es", "cs", "sk", "pl"]

DIR_PATH = Path("..")
DIR_OLDPATH = Path("../../math4u")

df_image_settings = pd.read_csv("image2pdf_setting.csv", dtype=str)

figure_name={
    "cs": "Obrázek",
    "sk": "Obrázok",
    "en": "Figure",
    "es": "Figura",
    "pl": "Rysunek",
}

file_action = """
    """

# hlavicky z https://getbootstrap.com/docs/4.3/getting-started/introduction/
def makeHEAD(css="", title="Math4u Real World Problems"):
    return f"""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    macros: {{
      arctg: "{{\\\\mathop{{\\\\mathrm {{arctg}}}}}}",
    }}
  }}
}};
</script>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js"></script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>

  <title>{title}</title>
  <style>
  body {{max-width:1000px;margin:auto;margin-top:5px; padding:10px;}}
  .buttons {{margin-bottom:20px;}}
  img {{max-width:90%; margin:auto; display:block;}}
  .time img {{display:inline-block; width: 2em;}}
  figcaption {{max-width:90%; margin:auto; font-style: italic; font-size: 80%;display:block; text-align: center;}}
  alert {{width:100%;}}
  .keywords span {{font-style:italic}}
  .keywords {{margin-bottom:10px;}}
  .tockeywords {{font-style:italic; font-size:80%}}
  .progress-unknown a , .progress-unknown {{color:green}}
  .progress-unfinished a , .progress-unfinished {{color:red;}}
  .progress-finished a , .progress-finished {{color:#007bff;}}
  .bold {{font-weight:bold;}}
  .time {{font-style: normal;}}
  .title {{font-weight: bold; font-size: 1.2em;}}

  #myInput {{width:50%; margin-left:auto; margin-bottom: 10px;}}

@media print {{
  body {{
    font-size: 18pt; /* Nastavte po¾adovanou velikost písma pro tisk */
  }}
  img{{max-width:50%;}}
}}

.header {{background-color: lightgray; }}
td, th {{padding-left: 10px;padding-right: 10px;}}
tr:nth-child(even) {{background-color: #f2f2f2;}}
  
  .buttons {{
  display: flex;
  gap: 10px; /* Mezera mezi tlačítky */
    flex-wrap: wrap; /* Umožňuje tlačítkům zalamování na úzkém displeji */
}}

.btn {{
  flex-grow: 1; /* Tlačítka se roztáhnou tak, aby vyplnila celý řádek */
  text-align: center; /* Vycentrování textu tlačítka */
}}
  
  {css}
  </style>
  </head>
  <body>
<div >
<img src="../head.svg" style="width: 100% !important; max-width: 100% !important;">
<div>
"""

HEAD = makeHEAD()

FOOT = """
<img src="../foot.svg" style="width: 100% !important; max-width: 100% !important;">
<div>


    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
"""

TOC_INTRO = f"""
<h1>Real World Problems</h1>
<div class="alert alert-success">Last update: {now.strftime("%d/%m/%Y %H:%M:%S")}</div>

<div class="alert alert-success">V tabulce jsou názvy a klíčová slova v CS, odkazy na soubory a odkaz na soubor na GitHub-u.
Uvnitř příkladu je možné přejít na jinou jazykovou verzi (klikání) nebo na další příklad v řadě (klikáním nebo šipkama z klávesnice).

</div>

"""

DEVEL_INFO = """
<div class="alert alert-success">Toto je vývojová verze. Produkční verze s hotovými příklady je na <a href="https://math4u.mendelu.cz">https://math4u.mendelu.cz</a>
</div>
"""

PRODUCTION_INFO = """
<div class="alert alert-success">Toto je produkční verze. Vývojová verze se všemi příklady je na <a href="https://um.mendelu.cz/math4u/site/">https://um.mendelu.cz/math4u/site/</a>
a je chráněna heslem.
</div>
"""


TOC_FOOT = """
<div class='info'>
<b>Legend</b>
<ul>
<li><span class=''>EN</span> English version not available yet. Will be created from the czech version (Mirka). The header will contain "is_finished: False".
<li><span class='bold progress-unfinished'>EN</span> English version in progress. The file is in one the the following stages: translation (Mirka), proofreading (Tereza), making changes according to Tereza's suggestions (Mirka). When all the steps will be finished, the last author (Mirka) should fix the line 'is_finished: False' to 'is_finished: True'.
<li><span class='bold progress-finished'>EN</span> English version is finished. Only minor fixes in future.
<li><span class='bold progress-unfinished'>CS</span> Na české verzi se pracuje. V hlavičce je 'is_finished: False' nebo nic. Po zkontrolování musí být v hlavičce informace 'is_finished: True'.
<li><span class='bold progress-finished'>CS</span> Verze v češtině je hotová, už jednom drobnější opravy. V hlavičce je informace 'is_finished: True'.
<li><span >ES</span> The Spain version will be here. However, not ready for translation yet.
<li><span class='bold progress-unfinished'>ES</span> Spain translation in progress. The header contains 'is_finished: False' row. When the translator finishes her/his work, she/he should fix the line 'is_finished: False' to True in the header.
<li><span class='bold progress-finished'>ES</span> Spain version finised. Minor improvements and correstions still possible. The header contains 'is_finished: True'.
<li>The other langages use the same scheme as ES.
<li><span class='bold progress-unknown'>CS</span> The status is not set explicitly or somehting went wrong.
</ul>

Workflow
<ul>
<li> Czech version is created and discussed. (Authors, Petr, Maruška)
<li> English version is translated from the Czech one. (Mirka)
<li> Proofreading English version. (Tereza gives suggestions to Mirka) The changes are in the column proofreading.
<li> Creating translations to ES, PL, SK from CS or EN. (Translators)
</ul>

</div>
"""

JS_FOOT = """
<script>
$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
</script>
"""

LATEXFILE_HEADER = r"""
\nonstopmode
\documentclass[oneside]{article}
\usepackage{graphicx, amsmath, url, amssymb, longtable, amsfonts, booktabs}

\parindent 0 pt
\parskip=6pt

\let\rmdefault\sfdefault

%%%GRAPHICSPATH

% Determine if the image is too wide for the page.
\makeatletter
\def\ScaleIfNeeded{%
  \ifdim\Gin@nat@width>\linewidth
    \linewidth
  \else
    \Gin@nat@width
  \fi
}
\makeatother
\def\hypertarget#1#2{#2}

% Resize figures that are too wide for the page.
\let\oldincludegraphics\includegraphics
\renewcommand\includegraphics[2][]{%
  \oldincludegraphics[width=\ScaleIfNeeded]{#2}
}

\usepackage{titlesec} 
\usepackage{tikz}
\usepackage{fontspec}
\usepackage{xcolor}
\usepackage[left=4cm,right=2.5cm,top=3cm,bottom=3cm, footskip=2cm]{geometry}
\usepackage{fancyhdr}

%------------------Main Font-------------------------
%\setmainfont{Fira Sans}
%Make sure you have the compiler "XeLaTeX" activated on your settings for your LaTeX document in order to see the font 

%------------------Color Set--------------------------
\definecolor{LightBlue}{RGB}{66, 163, 251}
\definecolor{DarkBlue}{RGB}{36, 100, 176}
\definecolor{LightGray}{gray}{.94}
\definecolor{DarkGray}{gray}{.172}
\definecolor{Orange}{RGB}{229, 133, 3}
\definecolor{MediumBlue}{RGB}{38, 119, 193}

%------------------Section Default Setting-------------
\titleformat*{\section}{\color{black}\normalfont\bfseries\Huge}
\titleformat*{\subsection}{\color{black}\normalfont\bfseries\LARGE}
\titleformat*{\subsubsection}{\color{black}\normalfont\bfseries\LARGE}

%-------------------Section Numbers Removal------------
\setcounter{secnumdepth}{0}


%-------------------------Header & Footer------------------------


\def\pandocbounded#1{#1}

\usepackage{eso-pic} % pro vložení obrázků na každou stránku
% Makro pro vložení obrázku nahoře na každé stránce
% Obrázek NA VŠECH STRÁNKÁCH, nahoře, přes celou šířku
\AddToShipoutPictureBG{%
  \AtPageUpperLeft{%
    \raisebox{-\height}{%
      \oldincludegraphics[width=\paperwidth]{../../head.pdf}%
    }%
  }%
  \AtPageLowerLeft{%
    \raisebox{-20pt}{%
      \oldincludegraphics[width=\paperwidth]{../../foot.pdf}%
    }%
  }%
}

\def\thepage{\hbox to 0 pt{\hss\hbox to \paperwidth{\hskip 2cm\bfseries\color{darkblue}\arabic{page}\hfil}\hss}}

\usepackage{tcolorbox}
\definecolor{myblue}{HTML}{AEEBF8}
\definecolor{darkblue}{HTML}{333399}

\tcbset{on line, arc=0pt,outer arc=0pt,colback=myblue, colframe=myblue, boxsep=0pt,left=5pt,right=5pt,top=8pt,bottom=8pt, boxrule=0pt,bottomrule=0pt,toprule=0pt}
\renewenvironment{quote}{\begin{minipage}{\linewidth}\begin{tcolorbox}}{\end{tcolorbox}\end{minipage}}

\definecolor{myblue2}{HTML}{21DEF8}
\usepackage[font=small,labelfont=bf, font={color=darkblue}]{caption}

\renewenvironment{quote}{\begin{minipage}{\linewidth}\begin{tcolorbox}}{\end{tcolorbox}\end{minipage}}
\let\rmdefault\sfdefault
%%%BABEL
                   
\usepackage{float}
\usepackage{datetime}

\def\arctg{\mathop{\mathrm{arctg}}}

\author{Math4u project}
\date{2025--2026}

\def\tightlist{\itemsep 0 pt\relax}
\begin{document}

\def\hypertarget#1#2{#2}

\def\meta{}
\let\oldsection\section
\def\section#1{\oldsection{#1}\par{\itshape \meta\par} \bigskip }

%%%METADATA

"""

LATEXFILE_FOOT = r"""

\bigskip
\textit{Compilation: \today, \currenttime}

\clearpage
\end{document}
"""

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