import json
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_from_data(data, output_filename):
    """
    data: List of lists (e.g., [['Header1', 'Header2'], ['Value1', 'Value2']])
    """
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    elements = []
    
    # Add a Title
    styles = getSampleStyleSheet()
    elements.append(Paragraph("Data Export Report", styles['Title']))
    
    # Create the Table
    t = Table(data)
    
    # Add Style (Grid, Colors, Alignment)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    t.setStyle(style)
    
    elements.append(t)
    doc.build(elements)

# --- DATA PARSING HELPERS ---

def csv_to_list(filepath):
    with open(filepath, 'r') as f:
        return list(csv.reader(f))

def json_to_list(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        # Assuming JSON is a list of dicts: [{"name": "Alice", "age": 30}, ...]
        headers = list(data[0].keys())
        rows = [list(item.values()) for item in data]
        return [headers] + rows

# Example Usage:
data = csv_to_list('data.csv')
create_pdf_from_data(data, 'report.pdf')