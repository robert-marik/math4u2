# %%
import importlib
import math4u
import pandas as pd
# print(math4u.directories)


# importlib.reload(math4u)
# file = math4u.File(path="00008_Solid_Geometry-Distance_of_cities/cs_article.md")
# copy = True
# file.to_html()


# %%
files = []
for dir in math4u.directories:
    problem = math4u.Problem(directory=dir)
    copy = False
    for file in problem.Files:
        try:
            yaml = file.yaml_header
        except:
            continue
        if 'workflow' in yaml.keys():
            try:
                print(file)
                copy = True
                file.to_html()
                file.to_pdf(output_path=f"_site/{problem.directory}/{file.path.name.split('.')[0]}.pdf")
                files.append(file)
            except:
                logging.warning(f"Error processing file {file}")
    if copy:
        problem.copy_files_from_repository()

# copy file foot.png to _site directories
import shutil

shutil.copy("foot.svg", "_site/foot.svg")
shutil.copy("head.svg", "_site/head.svg")




# %%


from datetime import datetime
now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M")

import math4u_table

df = pd.DataFrame(
[[i.language, str(i.path.parent), i.path.name.split(".")[0], i.yaml_header['workflow'], 
  "; ".join(i.yaml_header['keywords']), date_time] for i in files]
, columns=['language', 'directory', 'name', 'workflow', 'keywords','date_time'])


# math4u_table.main(

dirs = df["directory"].unique().tolist()
math4u_table.main(dirs, output_path="_site/index.html")

# %%


# df = pd.DataFrame(
# [[i.language, str(i.path.parent), i.path.name.split(".")[0], i.yaml_header['workflow'], 
#   "; ".join(i.yaml_header['keywords']), date_time] for i in files]
# , columns=['language', 'directory', 'name', 'workflow', 'keywords','date_time'])
# df.to_csv("math4u_file_workflows.csv")
# df['html'] = df['directory'] + "/" + df['name'] + ".html"
# df['pdf'] = df['directory'] + "/" + df['name'] + ".pdf"
# df['pdf_reduced'] = df['directory'] + "/" + df['name'] + "_reduced.pdf"
# df['diff2old'] = df['directory'] + "/" + df['name'] + "_diff.pdf"
# df.to_csv("math4u_file_workflow.csv")
# shutil.copy("math4u_file_workflow.csv", "_site/rwp_data.csv")
# shutil.copy("index_html", "_site/index.html")


# %%
