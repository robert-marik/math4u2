"""
Snippets and constants used in Math4u files.

Copyright 2024 Math4u project
"""

from datetime import datetime
now = datetime.now()

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

.headerBtn a {{
    display: inline-block;
    padding: 2px 20px;
    font-size: 16px;
    color: #007bff;
    text-decoration: none;
    border: 1px solid #007bff;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s;
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
\usepackage{graphicx, amsmath, url, amssymb, longtable, amsfonts, booktabs, hyperref}

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
\usepackage[left=3cm,right=2cm,top=3cm,bottom=3cm, footskip=2cm]{geometry}
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
\vfill
\textit{Compilation: \today, \currenttime}

\clearpage
\end{document}
"""
