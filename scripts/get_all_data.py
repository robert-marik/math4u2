#
# Create csv file for import on https://math4u.vsb.cz/import/m4u_rwp

#%%
import glob
import get_metadata
import yaml
import pandas as pd

dirs = glob.glob("../00*/cs_article.md")
dirs = sorted([d.split("/")[1] for d in dirs])

def get_yaml(dir, lang):
    file = f"../{dir}/{lang}_article.md"
    with open(file, "r") as f:
        text = f.read()
    yaml_text = text.split("---")[1]
    data = yaml.safe_load(yaml_text)
    # find the line which starts with # and get the title
    title_line = [line for line in text.split("\n") if line.startswith("#")][0]
    title = title_line.lstrip("# ").strip()
    data["title"] = title
    # add suffix lang to each key
    data = {f"{k}_{lang}": v for k, v in data.items()}
    return data

langs = ["cs", "en", "es", "pl", "sk"]
url = "https://math4u.mendelu.cz/rwp/"
def get_dir_data(dir):
    data = {}
    for lang in langs:
        data.update(get_yaml(dir, lang))
    data["directory"] = dir
    return data

data = [get_dir_data(d) for d in dirs]


#%%
df = pd.DataFrame(data)
c = [i for i in df.columns if "is_finished" in i]
df = df.drop(columns=c+["remark_en"])
df = df.rename(columns={"difficulty_cs": "difficulty", 'time_cs': 'time'})
target = ['html', 'pdf', 'pdf_reduced']

for lang in langs:
    df[f"html_{lang}"] = url + df["directory"] + f"/{lang}_article.html"
    df[f"pdf_{lang}"] = url + df["directory"] + f"/{lang}_article.pdf"
    df[f"pdf_reduced_{lang}"] = url + df["directory"] + f"/{lang}_article_reduced.pdf"

df

#%%

df = df.drop(columns=["remark_en"])
df.to_json("all_data.json", orient="records", indent=2)

#%%