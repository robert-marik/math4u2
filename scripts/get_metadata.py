#%%

import yaml

def get_metadata(file_to_convert, lang=None):
    if lang is not None:
        # Replace the filename with {lang}_article.md. Keep the directory.
        _ = file_to_convert.split("/")
        _[-1] = f"{lang}_article.md"
        file_to_convert = "/".join(_)
    with open(f"../{file_to_convert}", "r") as f:
        yaml_content = next(yaml.load_all(f, Loader=yaml.FullLoader))
        if 'keywords' in yaml_content.keys():
            keywords = yaml_content['keywords']
            if type(keywords)==type("string"):
                keywords = [i.strip() for i in keywords.split(",")]
            yaml_content['keywords'] = keywords
        return yaml_content


def main():
    ans = get_metadata("00011_Trigonometry_Crossing_the_river/en_article.md", lang='cs')
    print(ans)

if __name__ == "__main__":
    main()

# %%
