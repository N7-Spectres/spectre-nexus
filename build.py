"""Build Spectre Nexus from page.html + data.json.

  python3 build.py            -> dist/preview.html (private preview: shows "link needed" spots)
  python3 build.py --public   -> dist/index.html   (public site: hides anything without a link)

Edit data.json to change what the site shows, then rebuild.
"""
import base64, json, pathlib, sys

here = pathlib.Path(__file__).parent
public = "--public" in sys.argv
page = (here / "page.html").read_text()
data = json.loads((here / "data.json").read_text())
sprite = base64.b64encode((here / "assets/n7.png").read_bytes()).decode()

body = (page.replace("__NEXUS_DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
            .replace("__PREVIEW__", "false" if public else "true")
            .replace("__N7_SPRITE__", "data:image/png;base64," + sprite))

out = here / "dist"
out.mkdir(exist_ok=True)
if public:
    doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
           + body.replace("<style>", "</head>\n<body>\n<style>", 1) + "\n</body>\n</html>\n")
    (out / "index.html").write_text(doc)
    print("wrote", out / "index.html")
else:
    (out / "preview.html").write_text(body)
    print("wrote", out / "preview.html")
