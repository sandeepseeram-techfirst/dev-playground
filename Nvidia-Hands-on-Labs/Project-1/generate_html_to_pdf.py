
import os
import subprocess
import sys

# Read the master markdown file
with open('master_document.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zimbabwe Parliamentary Intervention Notes 2025</title>
    <style>
        body {{
            font-family: 'Times New Roman', serif;
            font-size: 12pt;
            line-height: 1.5;
            margin: 1in;
            color: #000;
        }}
        h1 {{
            font-size: 16pt;
            font-weight: bold;
            margin-top: 24pt;
            margin-bottom: 12pt;
            page-break-before: always;
        }}
        h2 {{
            font-size: 14pt;
            font-weight: bold;
            margin-top: 18pt;
            margin-bottom: 9pt;
        }}
        p {{
            margin-bottom: 12pt;
            text-align: justify;
        }}
        ul {{
            margin-bottom: 12pt;
        }}
        .title-page {{
            text-align: center;
            margin-top: 2in;
        }}
        .references {{
            font-size: 10pt;
        }}
        a {{
            color: #0000EE;
            text-decoration: none;
        }}
        @media print {{
            body {{ margin: 0.5in; }}
            h1 {{ page-break-before: always; }}
        }}
    </style>
</head>
<body>
"""

# Process markdown to HTML
lines = md_content.split('\n')
in_references = False
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    if line.startswith('# '):
        html_content += f'<h1>{line[2:]}</h1>\n'
    elif line.startswith('## '):
        if 'References' in line:
            html_content += '<h1>References</h1>\n<div class="references">\n'
            in_references = True
        else:
            html_content += f'<h2>{line[3:]}</h2>\n'
    elif line.startswith('### '):
        html_content += f'<h3>{line[4:]}</h3>\n'
    elif line.startswith('- '):
        if not in_references:
            html_content += f'<ul><li>{line[2:]}</li></ul>\n'
        else:
            html_content += f'<p>{line[2:]}</p>\n'
    elif line.startswith('**') and line.endswith('**'):
        html_content += f'<p><strong>{line[2:-2]}</strong></p>\n'
    elif line.startswith('*') and line.endswith('*'):
        html_content += f'<p><em>{line[1:-1]}</em></p>\n'
    elif line.startswith('---'):
        continue
    else:
        if line and not line.startswith('==='):
            if in_references:
                html_content += f'<p>{line}</p>\n'
            else:
                html_content += f'<p>{line}</p>\n'

if in_references:
    html_content += '</div>\n'

html_content += """
</body>
</html>
"""

# Save HTML file
with open('Zimbabwe_Parliament_Intervention_Notes_2025.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file created successfully: Zimbabwe_Parliament_Intervention_Notes_2025.html")

# Try to convert to PDF using wkhtmltopdf
try:
    subprocess.run(['wkhtmltopdf', 'Zimbabwe_Parliament_Intervention_Notes_2025.html', 'Zimbabwe_Parliament_Intervention_Notes_2025.pdf'], check=True)
    print("PDF file created successfully: Zimbabwe_Parliament_Intervention_Notes_2025.pdf")
except subprocess.CalledProcessError:
    print("wkhtmltopdf not found. Please install wkhtmltopdf to generate PDF.")
    print("HTML file is ready for manual conversion to PDF.")