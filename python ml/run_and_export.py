import os
import sys
import shutil
import asyncio
import subprocess
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

try:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except Exception:
    pass

BASE_DIR = r"c:\dev\code\python ml"
OUT_DIR = os.path.join(BASE_DIR, "to print 11 to 18")
ORIG_NAMES_DIR = os.path.join(OUT_DIR, "original_notebook_names")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(ORIG_NAMES_DIR, exist_ok=True)

# List of notebooks with their corresponding experiment number and target names
NOTEBOOKS = [
    {
        "num": 11,
        "filename": "Decision Tree Classificiation .ipynb",
        "clean_name": "11_Decision Tree Classificiation.pdf",
    },
    {
        "num": 12,
        "filename": "Random Forest Algo.ipynb",
        "clean_name": "12_Random Forest Algo.pdf",
    },
    {
        "num": 13,
        "filename": "KNN.ipynb",
        "clean_name": "13_KNN.pdf",
    },
    {
        "num": 14,
        "filename": "K Means.ipynb",
        "clean_name": "14_K Means.pdf",
    },
    {
        "num": 15,
        "filename": "PCA.ipynb",
        "clean_name": "15_PCA.pdf",
    },
    {
        "num": 16,
        "filename": "K FOLD.ipynb",
        "clean_name": "16_K FOLD.pdf",
    },
    {
        "num": 17,
        "filename": "Detecting Outliers.ipynb",
        "clean_name": "17_Detecting Outliers.pdf",
    },
    {
        "num": 18,
        "filename": "Email spam Naive.ipynb",
        "clean_name": "18_Email spam Naive.pdf",
    },
]

PRINT_CSS = """
<style>
@media print {
  @page {
    size: A4 portrait;
    margin: 1.5cm 1.2cm;
  }
  body {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    background-color: #ffffff !important;
    font-size: 10.5pt !important;
  }
  .jp-Cell {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    margin-bottom: 12px !important;
  }
  .jp-Cell-outputWrapper, .jp-OutputArea, .jp-OutputArea-child {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  .jp-RenderedImage img, .jp-OutputArea-output img {
    max-width: 95% !important;
    height: auto !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    display: block !important;
    margin: 6px auto !important;
  }
  table.dataframe {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    border-collapse: collapse !important;
  }
}
</style>
"""

def process_notebook(item):
    fname = item["filename"]
    nb_path = os.path.join(BASE_DIR, fname)
    print(f"\n==========================================")
    print(f"Processing Experiment {item['num']}: {fname}")
    print(f"==========================================")

    # 1. Read notebook
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # 2. Execute notebook
    print("Executing notebook cells...")
    ep = ExecutePreprocessor(timeout=300, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": BASE_DIR}})
    print("Execution complete.")

    # 3. Save executed notebook back to disk
    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print("Saved executed notebook with outputs back to disk.")

    # 4. Convert to HTML
    print("Exporting to HTML...")
    html_exporter = HTMLExporter()
    body, _ = html_exporter.from_notebook_node(nb)

    # Inject print CSS before </head>
    if "</head>" in body:
        body = body.replace("</head>", f"{PRINT_CSS}\n</head>")
    else:
        body = f"{PRINT_CSS}\n{body}"

    temp_html = os.path.join(BASE_DIR, f"_temp_exp_{item['num']}.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(body)

    # 5. Export HTML to PDF using Edge headless
    target_clean_pdf = os.path.join(OUT_DIR, item["clean_name"])
    base_stem = os.path.splitext(fname)[0].rstrip()
    target_orig_pdf = os.path.join(ORIG_NAMES_DIR, f"{base_stem}.pdf")

    print(f"Generating PDF: {item['clean_name']} ...")
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={target_clean_pdf}",
        temp_html,
    ]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0:
        print(f"Edge conversion failed with code {res.returncode}")
        print("stderr:", res.stderr.decode("latin1", errors="ignore"))
        sys.exit(1)

    # Also copy to original_notebook_names
    shutil.copy2(target_clean_pdf, target_orig_pdf)

    # Clean up temp html
    if os.path.exists(temp_html):
        os.remove(temp_html)

    size_kb = os.path.getsize(target_clean_pdf) / 1024
    print(f"SUCCESS: Created {item['clean_name']} ({size_kb:.1f} KB)")
    print(f"Also copied to: original_notebook_names/{base_stem}.pdf")

def main():
    print("Starting execution and PDF export of notebooks 11 to 18...")
    for item in NOTEBOOKS:
        process_notebook(item)
    print("\nALL 8 NOTEBOOKS PROCESSED SUCCESSFULLY!")

if __name__ == "__main__":
    main()

