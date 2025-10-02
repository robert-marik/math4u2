#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:12:24 2023

@author: marik
"""

import glob
import subprocess
import os
import pandas as pd
import argparse
import yaml
import logging
import get_metadata
logglevel = logging.INFO
logglevel = logging.DEBUG

logging.basicConfig(level=logglevel, format="%(asctime)s - %(levelname)s - %(message)s")       # nastaveni root loggeru

from datetime import datetime
now = datetime.now()

LANGS = ['en','cs','es','pl','sk']

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

<script src="https://utteranc.es/client.js"
        repo="robert-marik/math4u-comments"
        issue-term="title"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>

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

# TOC_FOOT = TOC_FOOT + JS_FOOT

def find_files():
    files = glob.glob('../*/cs*.md') + glob.glob('../sandbox/*/cs*.md')
    # files = [i.replace("/cs_article.md","").replace("../","") for i in files]   
    files.sort()
    return files

def find_versions(file):
    _ = file.split("/")
    data={}
    filename = _[-1]
    dirname = "/".join(_[1:-1])
    data={}
    for lang in LANGS:
        localized_filename = filename.replace("cs_",f"{lang}_")
        if os.path.isfile(f"../{dirname}/{localized_filename}"):
            data[lang] = localized_filename
        else:
            data[lang] = None
    if data['en'] is not None:
        title = subprocess.run(
            ["grep", "^# ",f"../{dirname}/{data['en']}","-m 1"],     
            capture_output = True, # Python >= 3.7 only
            text = True # Python >= 3.7 only
            )
    else:
        title = subprocess.run(
            ["grep", "^# ",f"../{dirname}/{data['cs']}","-m 1"],     
            capture_output = True, # Python >= 3.7 only
            text = True # Python >= 3.7 only
            )
    title = title.stdout
    if title is not None:
        title = title.replace("# ","").replace("\n","")
    data['title'] = title
    data['dirname'] = dirname
    data['filename'] = filename
    data['fullpath'] = f"{dirname}/{filename}"
    data['type'] = data['filename'].replace("cs_","").replace(".md","")
    proofreading_filename = filename.replace("cs_","en_").replace(".md","_proofreading.md")
    if os.path.isfile(f"../{dirname}/{proofreading_filename}"):
        data['proofreading'] = proofreading_filename
    else:
        data['proofreading'] = None
    
    return data
    
def row2toc(row, devel=False):
    logging.debug(row)
    number = row["fullpath"].split("_")[0].lstrip("0")
    if "sandbox" in number:
        number = ""
    out = ""
    for lang in LANGS:
        if row[lang] is None:
            out = out+f"<td>{lang.upper()}</td>"
        else:
            _, is_finished = get_info(f"{row['dirname']}/{row[lang]}")
            if (not devel) and (lang in ["cs"]) and ((is_finished is None) or (is_finished is False)):
                logging.info(f"Production version, skipping {row['title']} {lang} {is_finished}")
                return ""
            # print(row['title'], row[lang], is_finished)
            if is_finished is None:
                style = 'progress-unknown'
            elif is_finished:
                style = 'progress-finished'
            else:
                style = 'progress-unfinished'
            out = out+f"""
            <td class='{style} bold'>
            <a href='{row['dirname']}/{row[lang].replace('.md','.html')}'>{lang.upper()}
            </a></td>
            """
    title = "<span class='title'>" + row['title'] + "</span>"
    kws, _ = get_info(f"{row['dirname']}/en_article.md")
    yaml = get_metadata.get_metadata(f"{row['dirname']}/cs_article.md")
    if kws is not None and len(kws)>0:
        title = title + f"<br><span class='tockeywords'>({', '.join(kws)})<br> <span class='time'><img src='stopwatch.png'> {yaml['time']} min., <img src='speed.png'> {yaml['difficulty']}/3 </span></span>"
    if row['proofreading'] is not None:
        proofreafing_html_file = row['proofreading'].replace('.md','.html')
        command = 'git log --pretty=format:"%h" --reverse ../'+ row['dirname'] +'/'+row['proofreading'] +'| head -1'
        a = os.popen(command).read().strip()
        command = 'git diff ' + a + ' HEAD ../'+ row['dirname'] +'/'+row['proofreading'] + "> git_output.diff"
        a = os.popen(command).read()
        command = "pygmentize -f html -O full,style=trac -l diff -o diff.html git_output.diff"
        a = os.popen(command).read()
        command = "mv diff.html ../" + row['dirname'] +'/'+proofreafing_html_file
        a = os.popen(command).read()        
        opt_proofreading_link = f"<a href='{row['dirname']}/{proofreafing_html_file}'>link</a>"
    else:
        opt_proofreading_link = ""
    out = f"""
    <tr>
    <td>{number}</td>
    <td>{title}</td>
    <td>{row['type']}</td>
    {out}
    <td><a href="https://github.com/robert-marik/math4u/tree/main/{row['dirname']}">link</a></td>
    <td>{opt_proofreading_link}</td>
    </tr>
    """
    return out

def create_toc(df, devel=False):
    rows = [row2toc(row, devel=devel) for index, row in df.iterrows()]
    table = "\n".join(rows)
    table = f"""
    <input class="form-control" id="myInput" type="text" placeholder="What are you looking for?">
    <table class='table'><thead>
    <tr>
    <th>Číslo</th>
    <th>Název</th>
    <th>Typ</th>
    <th colspan="5">Jazyk</th>
    <th>Github</th>
    <th>Proofreading</th>
    </tr></thead><tbody id="myTable">
    {table}
    </tbody>
    </table>
    """
    if devel:
        out = HEAD+TOC_INTRO+DEVEL_INFO+table+TOC_FOOT+JS_FOOT+FOOT
    else:
        out = HEAD+TOC_INTRO+PRODUCTION_INFO+table+JS_FOOT+FOOT
    with open("_site/index.html","w") as f:
        f.write(out)

figure_name={
    "cs": "Obrázek",
    "sk": "Obrázok",
    "en": "Figure",
    "es": "Figura",
    "pl": "Rysunek",
}
        
def row2file(row,lang='cs'):
    file_to_convert = f"{row['dirname']}/{row['filename'].replace('cs_',lang+'_')}"
    
    prev_page = row['prev_page']
    next_page = row['next_page']
    if pd.isna(prev_page):
        prev_page = None
    if pd.isna(next_page):
        next_page = None

    if "sandbox" in row['dirname']:
        up = "../.."
    else:
        up = ".."
    output = ""

    if prev_page is not None:
        prev_page_html = f"{up}/{prev_page.replace('.md','.html')}"
        prev_page_html = prev_page_html.replace('/cs_',f"/{lang}_")
        action_prev = f"window.location.assign(\"{prev_page_html}\");"
    else:
        action_prev = "alert(\"This is the first article.\");"
    if next_page is not None:    
        next_page_html = f"{up}/{next_page.replace('.md','.html')}"
        next_page_html = next_page_html.replace('/cs_',f"/{lang}_")
        action_next = f"window.location.assign(\"{next_page_html}\");"
    else:
        action_next = "alert(\"Ths is the last article.\");"
    
    file_action = """
        <script>
            jQuery(document).on('keydown', function (event) {
                if (event.which == 37) {
        """ + action_prev + """
                } else if (event.which == 39) {
        """ + action_next + """
                }
            });
        </script>
        """
    
    if prev_page is not None:
        output = output + f"""<div class='buttons'>
         <a href="{prev_page_html}" class="btn btn-primary prevpage">Previous {lang.upper()}</a>
         """
    else:
        output = output + f"""<div class='buttons'>
         <span class="btn btn-secondary prevpage">Previous {lang.upper()}</span>
         """
    output = output + f"""
         <a href="{up}/index.html" class="btn btn-primary prevpage">TOC</a>
         <a href="https://github.com/robert-marik/math4u/tree/main/{file_to_convert}" class="btn btn-primary prevpage">View on GitHub</a>
         <a href="{(file_to_convert.split('/')[-1]).replace('.md','.pdf')}" class="btn btn-primary prevpage">PDF</a>
    """
    logging.debug(f"Zkracene PDF {lang} {row['dirname']}")
    output = output + f"""
             <a href="{(file_to_convert.split('/')[-1]).replace('.md','_reduced.pdf')}" class="btn btn-primary prevpage">PDF reduced</a>
        """
    for langs in LANGS:
        if row[langs] is None:
            output = output + f" <span class='btn btn-secondary'>{langs.upper()}</span> "
        else:
            link = row['filename']
            link = link.replace("cs_",f"{langs}_").replace(".md",".html")
            output = output + f" <a href='{link}' class='btn btn-primary'>{langs.upper()}</a> "

    if next_page is not None:
        output = output + f"""
         <a href="{next_page_html}" class="btn btn-primary prevpage">Next {lang.upper()}</a>
         """
    else:
        output = output + f"""
         <span class="btn btn-secondary prevpage">Next {lang.upper()}</span>
         """
    output = output + "</div>"
    
    if row[lang] is None:
        file_content = "<br>To appear."
    else:
        file_content = subprocess.run(
                ["pandoc", 
                 "--mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js",
                 f"../{file_to_convert}"
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
        for i in range(1,20):
            file_content =  file_content.replace(
            "<figcaption>",
                f"<figcaption >{figure_name[lang]} {i}. ", 1        
            )
        file_content =  file_content.replace(
            "<figcaption >",
            "<figcaption>"        
            )
        keywords,_ = get_info(file_to_convert)
        yaml = get_metadata.get_metadata(file_to_convert, lang='cs')
        if keywords is not None:
            file_content = file_content.replace("</h1>",f"</h1><div class='keywords'><span>Keywords: </span>{', '.join(keywords)}</div><span class='time'><img src='../stopwatch.png'> {yaml['time']} min., <img src='../speed.png'> {yaml['difficulty']}/3 </span><br><br>")
    css = ""    
    if os.path.isfile(f"../{row['dirname']}/{row['type']}.css"):
        with open(f"../{row['dirname']}/{row['type']}.css") as f:
            css = "\n".join(f.readlines())
    with open(f"_site/{file_to_convert.replace('.md','.html')}","w") as f:
        f.write(makeHEAD(css=css, title=file_to_convert) + output + file_content + file_action + FOOT)

def get_info(file_to_convert):
    with open(f"../{file_to_convert}", "r") as f:
        try:
            yaml_content = next(yaml.load_all(f, Loader=yaml.FullLoader))
            if 'keywords' in yaml_content.keys():
                keywords = yaml_content['keywords']
            else:
                keywords = []
            is_finished = False
            if 'is_finished' in yaml_content.keys():
                is_finished = yaml_content['is_finished']
            if type(keywords)==type("string"):
                keywords = [i.strip() for i in keywords.split(",")]
            return keywords, is_finished
        except:
            return None, None 
        
def check_git():
    """
    Tries to fetch and update git repository. Returns None if the
    repository is up to date. 
    Returns True if the update has been downloaded.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    git_output = subprocess.run( ["git", 
      "fetch",
      "origin"
      ],     
     capture_output = True, # Python >= 3.7 only
     text = True # Python >= 3.7 only
     )
    git_output = subprocess.run( ["git", 
      "status",
      "-uno"
      ],     
     capture_output = True, # Python >= 3.7 only
     text = True # Python >= 3.7 only
     )
    if "Your branch is up to date" in git_output.stdout:
        print("Git is up to date, exit.")
        return None
    else:
        subprocess.run( ["git", 
          "pull",
          ],     
         capture_output = True, # Python >= 3.7 only
         text = True # Python >= 3.7 only
         )
    return True
        
def main(): 
    """    
    Parameters
    ----------
    update_git : TYPE, optional
        True -> update git, exit if up to date, process files if somthing changed
        False -> do not update git and process the files
        The default is False.

    Returns
    -------
    None.

    """
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--skip_update", help="Skip Git update and compile even if Git is up to date.", action="store_true")
    argParser.add_argument("-d", "--devel", help="Create development version.", action="store_true")
    
    args = argParser.parse_args()
    if args.skip_update:
        update_git = False
    else:
        update_git = True

    if args.devel:
        devel = True
    else:
        devel = False
    # update_git = False        
    
    os.makedirs('_site',exist_ok=True)

    if update_git:
        if check_git() is None:
            return None

    out = [find_versions(file) for file in find_files()]
    df = pd.DataFrame(out)
    df['prev_page'] = df['fullpath'].shift(1)
    df['next_page'] = df['fullpath'].shift(-1)

    create_toc(df, devel=devel)
    for directory in df['dirname']:
        os.makedirs(f'_site/{directory}',exist_ok=True)
        os.popen(f"cp -r ../{directory}/* _site/{directory}/")
    for index, row in df.iterrows()       :
        for lang in LANGS:
            row2file(row,lang=lang)

if __name__ == '__main__':
    main()
        

# out = [find_versions(file) for file in find_files()]
# df = pd.DataFrame(out)

