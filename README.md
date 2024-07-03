# PDF Merger

## Project Description

This project's main goal is to merge different PDFs into a one single PDF file **using Python**. This app will gather all PDFs the user has given in the directory and merge them alphabetically into one single PDF file. This app is mainly focused on **educational purposes.**

## Used Libraries

- **pypdf**
  - Append all given PDF files in a single PDF writer object
  - Write the result on a new PDF file
  
- **os**
  - Gather all PDFs in the /pdf directory
  - Evaluate alt-text usage

## Usage
 2. Drag all PDF files you want to merge in the **/pdf** directory (delete example PDFs beforehand) of the app.
 3. If needed, name the PDF files alphabetically in the order you want them to be ordered.
 4. Run the **merger.py** file.
 5. The merged PDF result will be created named **"merged-pdf.pdf"**.
