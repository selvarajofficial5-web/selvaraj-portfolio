import json
import os
from jinja2 import Environment, FileSystemLoader

def main():
    with open("Content/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader("Templates"), autoescape=True)
    template = env.get_template("index.html")
    html = template.render(d=data)

    os.makedirs("Sites", exist_ok=True)
    with open("Sites/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Done! Open: Sites/index.html")

if __name__ == "__main__":
    main()
