from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML, CSS

def generate_pdf(request):
    context = {'example_data': 'Hello, World!'}
    template = get_template('index.html')
    html_content = template.render(context)
    html = HTML(string=html_content, base_url=request.build_absolute_uri())
    pdf_file = html.write_pdf()
    pdf_file = html.write_pdf(stylesheets=["/home/codiant/Learning/pdf_render/src/src/templates/index.css", 
                                           CSS(string='@page { size: A0; margin: 1cm }')])
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="output.pdf"'
    return response

