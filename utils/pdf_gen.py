from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

class PDFGenerator:
    def __init__(self, title):
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
        self.title = title

    def create(self, content):
        c = canvas.Canvas("daily_report.pdf")
        c.setFont('HeiseiMin-W3', 16)
        c.drawString(50, 800, self.title)
        c.setFont('HeiseiMin-W3', 12)
        y = 750
        for line in content.split('\n'):
            c.drawString(50, y, line)
            y -= 20
        c.save()
        return "daily_report.pdf"