from pypdf import PdfWriter

pdfs = [
    "./paper/Intro/build/intro.pdf",
    "./paper/Plan/build/plan.pdf",
    "./paper/Analysis/build/analysis.pdf",
    "./paper/Conclusion/build/conclusion.pdf",
]

merger = PdfWriter()
for pdf in pdfs:
    merger.append(pdf)
merger.write("main.pdf")
