# %%

import math4u
import sys

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
            # file.to_pdf()
            # file.pandiff()
    if copy:
        problem.copy_files_from_repository()
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