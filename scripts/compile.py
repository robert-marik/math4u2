# %%
import math4u
import pandas as pd
# print(math4u.directories)

files = []
for dir in math4u.directories:
    problem = math4u.Problem(directory=dir)
    copy = False
    for file in problem.Files:
        yaml = file.yaml_header
        if 'workflow' in yaml.keys():
            print(file)
            copy = True
            files.append(file)
            file.to_html()
            file.to_pdf(output_path=f"_site/{problem.directory}/{file.path.name.split('.')[0]}.pdf")
    if copy:
        problem.copy_files_from_repository()

# copy file foot.png to _site directories
import shutil

shutil.copy("foot.svg", "_site/foot.svg")
shutil.copy("head.svg", "_site/head.svg")


# %%
files 

# %%

#import rich
#rich.inspect(files[0])
# %%

df = pd.DataFrame(
[[i.language, str(i.path.parent), i.path.name.split(".")[0], i.yaml_header['workflow'], i.yaml_header['keywords']] for i in files]
, columns=['language', 'directory', 'name', 'workflow', 'keywords'])
df.to_csv("math4u_file_workflows.csv")
df['html'] = df['directory'] + "/" + df['name'] + ".html"
df['pdf'] = df['directory'] + "/" + df['name'] + ".pdf"
df['diff2old'] = df['directory'] + "/" + df['name'] + "_diff.pdf"
df.to_csv("math4u_file_workflow.csv")
shutil.copy("math4u_file_workflow.csv", "_site/rwp_data.csv")
shutil.copy("index_html", "_site/index.html")


# %%
df
# %%
