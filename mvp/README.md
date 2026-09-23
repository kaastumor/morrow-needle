# Needle Corpus Explorer v0.1

This directory is the deliberately thin browser projection over the canonical
Needle corpus. It reads `../corpus/index-v0.1.json` directly at runtime; do not
commit a copied or generated corpus here.

## Local launch

From the repository root:

```sh
python -m http.server 8000
```

Then open `http://localhost:8000/mvp/` in a browser.

Opening `index.html` directly as a `file://` URL is not supported because browser
fetch security rules may block access to the sibling canonical corpus file.

## Scope

The MVP uses static HTML, CSS and vanilla JavaScript only. There is no build
step, backend, database, authentication, model call, analytics or frontend
dependency.
