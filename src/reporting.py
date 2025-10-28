import os
from datetime import datetime
from fpdf import FPDF

from src.log_setup import logging
logger = logging.getLogger(__name__)


def generate_pdf_report(kpis, plots_dir='reports/plots'):
    
    os.makedirs('reports', exist_ok=True)
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_draw_color(180, 180, 180)
    pdf.rect(10, 10, 190, 277)  # border frame

    pdf.set_font('Arial', 'B', 18)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 10, 'API Data Dashboard Report', ln=True, align='C')
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0, 10, 'Automated Daily Summary', ln=True, align='C')
    pdf.ln(10)

    # KPI Section
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Key Performance Indicators', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.set_fill_color(245, 245, 245)
    pdf.set_draw_color(200, 200, 200)
    pdf.ln(5)

    for key, value in kpis.items():
        pdf.cell(80, 8, str(key), border=1, fill=True)
        pdf.cell(80, 8, str(value), border=1, ln=True)

    pdf.ln(10)
    pdf.set_draw_color(150, 150, 150)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(10)

    #Charts Section
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Charts and Visualizations', ln=True)
    pdf.ln(5)

    for img in sorted(os.listdir(plots_dir)):
        if img.endswith('.png'):
            img_path = os.path.join(plots_dir, img)
            pdf.image(img_path, w=170)
            pdf.ln(8)

    # Footer
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, f'Generated automatically - {datetime.now():%Y-%m-%d %H:%M:%S}', 0, 0,'C')

    pdf.output('reports/dashboard.pdf')
    logger.info(' PDF report generated successfully: reports/dashboard.pdf')