import nbformat

NOTEBOOK_PATH = "LLM_Text_Generator.ipynb"  # <-- change this filename

nb = nbformat.read(NOTEBOOK_PATH, as_version=4)

# Remove widget metadata entirely
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

nbformat.write(nb, NOTEBOOK_PATH)
print(f"✅ Removed nb.metadata['widgets'] and saved: {NOTEBOOK_PATH}")
