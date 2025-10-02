#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:08:13 2024

@author: marik
"""

import subprocess
import os
import glob
import pandas as pd
import shutil
import logging
import pickle
import hashlib
import get_metadata

logging.basicConfig(level="INFO")       # nastaveni root loggeru
logger = logging.getLogger("build_latex")
logger.setLevel(logging.INFO)
logger.info("Logging initiated")

def calculate_md5(file_path):
    """
    https://www.geeksforgeeks.org/finding-md5-of-files-recursively-in-directory-in-python/
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

latexfile_header = r"""
\nonstopmode
\documentclass[oneside]{article}
\usepackage{graphicx, amsmath, url, amssymb, longtable, amsfonts, booktabs}

\parindent 0 pt
\parskip=6pt

\let\rmdefault\sfdefault

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
      \oldincludegraphics[width=\paperwidth]{../head.pdf}%
    }%
  }%
  \AtPageLowerLeft{%
    \raisebox{-20pt}{%
      \oldincludegraphics[width=\paperwidth]{../foot.pdf}%
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

\def\arctg{\mathop{\mathrm{arctg}}}

\author{Math4u project}
\date{2022--2025}

\def\tightlist{\itemsep 0 pt\relax}
\begin{document}

%\title{}
%\author{Math4You}
%\date{2023--2025}
%\maketitle

\def\hypertarget#1#2{#2}

\def\meta{}
\let\oldsection\section
\def\section#1{\oldsection{#1}\par{\itshape \meta\par} \bigskip }

"""

latexfile_foot = r"""

\clearpage
\end{document}
"""

def osetri_text(text):
    text = text.replace(u'\u2006'," ")
    text = text.replace(u'\u2004'," ")
    text = text.replace(r'\begin{figure}',r'\begin{figure}[H]')
    text = text.replace(r'.svg',r'.pdf')
    text = text.replace(r'\textbackslash iffalse',r'\iffalse')
    text = text.replace(r'\textbackslash fi',r'\fi')
    return {'reduced':text, 'full':text.replace(r"\iffalse","").replace(r"\fi","")}

os.makedirs('_latex',exist_ok=True)

def find_files():
    files = glob.glob('../*/*_*.md') + glob.glob('../sandbox/*/*_*.md')
    # files = [i.replace("/cs_article.md","").replace("../","") for i in files]   
    files.sort()
    return files

df = pd.read_csv("image2pdf_setting.csv", dtype=str)

allfiles = [i for i in find_files() if "proofreading" not in i]
# allfiles = [i for i in allfiles if "regrese" in i]

logger.info("Zacinam zpracovani vsech souboru")

try:
    with open('saved_dictionary.pkl', 'rb') as f:
        soucty = pickle.load(f)
except:
    soucty = {}

for file_to_convert in allfiles:
    if file_to_convert in soucty.keys() and calculate_md5(file_to_convert) == soucty[file_to_convert]:
        logger.info(f"Skipping {file_to_convert}")
        continue
    # if "18" not in file_to_convert:
    #     continue
    logger.info(f"Pandoc for {file_to_convert}")
    file_content_dict = subprocess.run(
            ["pandoc", 
             "-tlatex",
             f"{file_to_convert}"
             ],     
            capture_output = True, # Python >= 3.7 only
            text = True # Python >= 3.7 only
            )
    file_content = osetri_text(file_content_dict.stdout)['full']
    file_reduced_content = osetri_text(file_content_dict.stdout)['reduced']

    yaml = get_metadata.get_metadata(file_to_convert[1:])
    yaml_cs = get_metadata.get_metadata(file_to_convert[1:], lang='cs')

    directory = "/".join(file_to_convert.split("/")[1:-1])
    grafic_path = r"\graphicspath{{../}{../../"+directory+"}}\n"
    filename = (file_to_convert.split("/")[-1]).split(".")[0]
    babel = ""
    if filename[:2]=="cs":
        babel = r"\usepackage[czech]{babel}"
    if filename[:2]=="sk":
        babel = r"\usepackage[slovak]{babel}"
    if filename[:2]=="pl":
        babel = r"\usepackage[polish]{babel}"
    if filename[:2]=="es":
        babel = r"\usepackage[spanish]{babel}"

    if "article" in file_to_convert:
        try:
            kwds = ', '.join(yaml['keywords'])
        except KeyError:
            kwds = ''
        metadata = f"""
    \\def\\meta{{
    Keywords:  {kwds} 

    }}
    """
    else:
        metadata = ""

    file_content = latexfile_header + grafic_path + metadata + file_content + latexfile_foot
    file_content = file_content.replace("%%%BABEL",babel) 
    
    file_reduced_content = latexfile_header + grafic_path + metadata + file_reduced_content + latexfile_foot
    file_reduced_content = file_reduced_content.replace("%%%BABEL", babel)

    for n,i,s in df[df['number']==directory[:5]].values:
        file_content = file_content.replace(r"\includegraphics{"+i+"}",r"\oldincludegraphics["+s+"]{"+i+"}")
        file_reduced_content = file_reduced_content.replace(r"\includegraphics{"+i+"}",r"\oldincludegraphics["+s+"]{"+i+"}")

    with open(f"_latex/{filename}.tex","w") as out:
        out.write(file_content)
        out.flush()
    with open(f"_latex/{filename}_reduced.tex","w") as out:
        out.write(file_reduced_content)
        out.flush()
    out_directory = directory
    if "sandbox" in directory:
        out_directory = directory.replace("sandbox/","")
    os.makedirs("_latex/"+out_directory,exist_ok=True)
    logger.info("Vlna")
    subprocess.run(["vlna","-l",f"{filename}.tex"],
                capture_output = True, # Python >= 3.7 only
                text = True, # Python >= 3.7 only
                cwd = "_latex/"
                )
    subprocess.run(["vlna","-l",f"{filename}_reduced.tex"],
                    capture_output = True, # Python >= 3.7 only
                    text = True, # Python >= 3.7 only
                    cwd = "_latex/"
                    )
    for i in range(2):
        logger.info(f"Compiling {filename}.tex")
        compilation = subprocess.run(
            ["xelatex", 
             "-output-directory="+out_directory,
             f"{filename}.tex",
             ],     
            capture_output = True, # Python >= 3.7 only
            text = True, # Python >= 3.7 only
            cwd = "_latex/"
            )
    shutil.copy(f"_latex/{filename}.tex",f"_latex/{directory[:5]}_{filename}.tex")
    if True or filename[:2]=="cs":
        for i in range(2):
            logger.info(f"Compiling {filename}_reduced.tex")
            compilation = subprocess.run(
                ["xelatex",
                 "-output-directory=" + out_directory,
                 f"{filename}_reduced.tex",
                 ],
                capture_output=True,  # Python >= 3.7 only
                text=True,  # Python >= 3.7 only
                cwd="_latex/"
            )
        shutil.copy(f"_latex/{filename}.tex", f"_latex/{directory[:5]}_{filename}_reduced.tex")

    soucty[file_to_convert] = calculate_md5(file_to_convert)
    logger.info(f"Saving md5 sum {soucty[file_to_convert]}")
    with open('saved_dictionary.pkl', 'wb') as f:
        pickle.dump(soucty, f)

