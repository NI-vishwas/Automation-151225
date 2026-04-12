import pandas as pd
import markdown
from jinja2 import Template
from weasyprint import HTML
from datetime import datetime

def create_pdf_from_md(data_file, template_file, output_pdf):
    # 1. Load Data
    if data_file.endswith('.csv'):
        df = pd.read_csv(data_file)
    else:
        df = pd.read_json(data_file)
    
    headers = df.columns.tolist()
    rows = df.values.tolist()

    # 2. Read Markdown Template
    with open(template_file, 'r') as f:
        md_template = f.read()

    # 3. Render Markdown with Data
    template = Template(md_template)
    rendered_md = template.render(
        title="Automated Data Report",
        date=datetime.now().strftime("%Y-%m-%d"),
        headers=headers,
        rows=rows
    )

    # 4. Convert Markdown to HTML
    # We add 'tables' extension so the Markdown tables render correctly
    html_content = markdown.markdown(rendered_md, extensions=['tables'])

    # 5. Add Basic CSS Styling
    styled_html = f"""
    <html>
        <head>
            <style>
                body {{ font-family: 'Helvetica'; margin: 40px; line-height: 1.6; }}
                table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
                th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
                th {{ background-color: #f4f4f4; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #2c3e50; }}
                h2 {{ color: #34495e; margin-top: 30px; }}
            </style>
        </head>
        <body>{html_content}</body>
    </html>
    """

    # 6. Generate PDF
    HTML(string=styled_html).write_pdf(output_pdf)
    print(f"Report generated: {output_pdf}")

# Usage
# create_pdf_from_md('data.csv', 'report.md', 'output_report.pdf')