import pandas as pd
import json
import subprocess
from jinja2 import Template
import os

def generate_report(data_source, template_path, output_pdf):
    # 1. Load Data
    if data_source.endswith('.csv'):
        df = pd.read_csv(data_source)
        data_dict = df.to_dict(orient='records')
        headers = df.columns.tolist()
    else:
        with open(data_source, 'r') as f:
            data_dict = json.load(f)
            headers = data_dict[0].keys() if data_dict else []

    # 2. Render Markdown Template
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    template = Template(template_content)
    markdown_content = template.render(
        headers=headers,
        rows=data_dict,
        title="Automated System Report"
    )

    # 3. Save temporary Markdown file
    temp_md = "temp_report.md"
    with open(temp_md, "w") as f:
        f.write(markdown_content)

    # 4. Use Pandoc to convert MD to PDF
    # --variable margin=1in: Sets page margins
    # --pdf-engine=weasyprint: You can also use 'xelatex' or 'pdflatex'
    try:
        subprocess.run([
            'pandoc', temp_md, 
            '-o', output_pdf,
            '--variable', 'geometry:margin=1in',
            '--variable', 'fontsize=11pt',
            '--pdf-engine=xelatex'  # Requires a LaTeX distribution like MiKTeX/TeXLive
        ], check=True)
        print(f"Successfully generated {output_pdf}")
    finally:
        if os.path.exists(temp_md):
            os.remove(temp_md)

# Execution
if __name__ == "__main__":
    generate_report('data.csv', 'template.md', 'final_report.pdf')


# subprocess.run(['pandoc', temp_md, 'metadata.yaml', '-o', output_pdf, '--pdf-engine=xelatex'])