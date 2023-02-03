# PeterGaoAway
Peter Gao HKUST Pastpaper Watermark remover

## Usage

- Install relevant depenencies (not a lot)
- Put PDFs in the same folder as `petergaoaway.py`
- Run `petergaoaway.py`
- Check the console output
  - If it halts, the script cannot detect the watermark. It may be caused by
    - Peter Gao has changed the watermark text sufficiently to prevent detection
    - Similar text found in the PDFs causing misdetection
    - No watermark at all (sometime this happens)
- Find your output in `output` folder, with `.clean.pdf` suffix
