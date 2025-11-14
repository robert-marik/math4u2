import os
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

LANGS = {
    "cs": "CZ",
    "en": "ENG",
    "sk": "SK",
    "pl": "PL",
    "es": "ES",
}

WORKFLOW_COLORS = {
    "in progress": "red",
    "translating": "green",
    "finished": "blue",
}

DIR_PREFIX = ".."


def read_workflow(path):
    # print(f"[INFO] Reading workflow from {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # print(f"[DEBUG] Content starts with: {content[:30]!r}")
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                yaml_block = content[3:end]
                data = yaml.safe_load(yaml_block)
                return data.get("workflow", None)
    except Exception as e:
        print(f"[WARN] Nepodarilo se nacist workflow z {path}: {e}")

    return None




def collect_data(directories):
    rows = []
    for d in directories:
        dirname = os.path.basename(d)

        row = {
            "dirname": dirname,
            "old": [],
            "new": []
        }

        # STARÉ VERZE
        for code, label in LANGS.items():
            old_url = f"https://rwp.math4u.vsb.cz/{dirname}/{code}_article.html"
            row["old"].append({"label": label, "url": old_url})

        # NOVÉ VERZE
        for code, label in LANGS.items():
            filename = f"{code}_article.md"
            print("[INFO] Checking file:", filename)
            path = os.path.join(DIR_PREFIX,d, filename)

            if not os.path.exists(path):
                row["new"].append({"label": label, "exists": False})
            else:
                wf = read_workflow(path)
                print(f"[INFO] Workflow for {path}: {wf}")
                row["new"].append({
                    "label": label,
                    "exists": True,
                    "url": f"{d}/{filename.replace('.md', '.html')}",
                    "workflow": wf,
                    "color": WORKFLOW_COLORS.get(wf, "black")
                })

        rows.append(row)

    return rows


def main(dirs, output_path="_site/new_index.html"):

    # ────────────────────────────────────────────────
    # 1) Absolutní cesta ke skriptu
    # ────────────────────────────────────────────────
    BASE = os.path.dirname(os.path.abspath(__file__))
    print(f"[INFO] BASE PATH = {BASE}")

    template_dir = os.path.join(BASE, "templates")
    template_name = "index.html.j2"

    # ────────────────────────────────────────────────
    # 2) Kontrola složky templates
    # ────────────────────────────────────────────────
    print(f"[INFO] Template directory = {template_dir}")

    if not os.path.isdir(template_dir):
        print("[ERROR] Složka 'templates' NEEXISTUJE!")
        return

    # ────────────────────────────────────────────────
    # 3) Výpis obsahu templates
    # ────────────────────────────────────────────────
    print("[INFO] Obsah složky templates:")
    print("       ", os.listdir(template_dir))

    template_path = os.path.join(template_dir, template_name)
    print(f"[INFO] Template path: {template_path}")

    if not os.path.exists(template_path):
        print(f"[ERROR] Šablona {template_name} NEEXISTUJE!")
        return

    # ────────────────────────────────────────────────
    # 4) Nastavení Jinja
    # ────────────────────────────────────────────────
    env = Environment(loader=FileSystemLoader(template_dir))

    try:
        tmpl = env.get_template(template_name)
    except TemplateNotFound:
        print(f"[ERROR] Jinja nenašla šablonu: {template_name}")
        return
    except Exception as e:
        print(f"[ERROR] Chyba při načítání šablony: {e}")
        return

    # ────────────────────────────────────────────────
    # 5) Generování HTML
    # ────────────────────────────────────────────────
    html = tmpl.render(rows=collect_data(dirs), LANGS=LANGS)

    # ────────────────────────────────────────────────
    # 6) Zajištění existence cílové složky
    # ────────────────────────────────────────────────
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        print(f"[INFO] Vytvářím složku {out_dir}")
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[OK] Vygenerováno → {output_path}")


if __name__ == "__main__":
    dirs = [
        "00008_Solid_Geometry-Distance_of_cities",
        "00010_Analytic_geometry_Parabolic_calculator",
        "00013_Golf_ball",
        "00020_Radioactivity_and_Kramatorsk",
        "00027_Golden_Ratio",
    ]
    main(dirs)
