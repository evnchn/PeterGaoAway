import fitz
import glob
import os
import sys

try:
    os.mkdir("output")
except:
    pass

for original_file in glob.glob("*.pdf"):

    doc = fitz.open(original_file)

    for i, page in enumerate(doc):
        arr_select = [x for x in page.get_text().splitlines() if "Academic use within HKUST only." in x]
        print(arr_select)
        if len(arr_select) != 1:
            print(f"For file: {original_file}")
            print(f"Failure to detect watermark string on page {i+1}!")
            input("Submit file sample to evnchn immediately for counteraction!")
            continue
        draft = page.search_for(arr_select[0])
        
        for rect in draft:
            annot = page.add_redact_annot(rect)
            page.apply_redactions()
            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
        # then save the doc to a new PDF:
    doc.save(os.path.join("output", original_file.replace(".pdf",".clean.pdf")), garbage=3, deflate=True)