from reportlab.pdfgen import canvas
from django.http import HttpResponse

from ..models import ReportFragment


def getpdf(request, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response
