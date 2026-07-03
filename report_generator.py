from reportlab.pdfgen import canvas
import os

def generate_pdf(transcription, similarity, score, grade):

    print("generate_pdf() called")

    base_dir = os.path.dirname(os.path.abspath(__file__))

    report_dir = os.path.join(base_dir, "reports")
    os.makedirs(report_dir, exist_ok=True)

    pdf_path = os.path.join(report_dir, "Result_Report.pdf")

    pdf = canvas.Canvas(pdf_path)

    pdf.setFont("Helvetica-Bold",16)
    pdf.drawString(150,800,"Communication Analysis Report")

    pdf.setFont("Helvetica",12)
    pdf.drawString(50,760,"Transcription:")
    pdf.drawString(50,740,transcription)

    pdf.drawString(50,700,f"Semantic Similarity : {similarity:.2f}")
    pdf.drawString(50,680,f"Understanding Score : {score}")
    pdf.drawString(50,660,f"Classification : {grade}")

    pdf.save()

    print("PDF saved at:", pdf_path)

    return pdf_path