import json
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def generate_pdf(input_file, template_path, output_pdf):
    # 1. Load Data (Works for CSV or JSON)
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_json(input_file)

    headers = df.columns.tolist()
    rows = df.values.tolist()

    # 2. Setup Jinja2 Environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)

    # 3. Render HTML with Data
    html_out = template.render(title="Data Export", headers=headers, rows=rows)

    # 4. Convert HTML to PDF
    HTML(string=html_out).write_pdf(output_pdf)
    print(f"Successfully created {output_pdf}")

# Usage
generate_pdf('data.json', 'report_template.html', 'final_report.pdf')