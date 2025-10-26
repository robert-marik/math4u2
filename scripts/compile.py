# %%
import math4u

# print(math4u.directories)

for dir in math4u.directories:
    problem = math4u.Problem(directory=dir)
    copy = False
    for file in problem.Files:
        yaml = file.yaml_header
        if 'workflow' in yaml.keys():
            print(file)
            copy = True
            file.to_html()
            file.to_pdf(output_path=f"_site/{problem.directory}/{file.path.name.split('.')[0]}.pdf")
    if copy:
        problem.copy_files_from_repository()

# copy file foot.png to _site directories
import shutil
dest = f"_site/foot.png"
shutil.copy("foot.svg", dest)
shutil.copy("head.svg", dest)
exit()

# %%

problem = math4u.Problem(number=23)
# print(problem)

# %%
problem = math4u.Problem(number=2)
problem.copy_files_from_repository()
# print(problem.files)

# %%

for file in problem.files.values():
    math4u.File(file).to_html()  # converts and caches HTML version