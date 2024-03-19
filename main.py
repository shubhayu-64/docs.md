from typing import Tuple
from flask import Flask, render_template, abort
import markdown
import os

from models.models import DocsModel

app = Flask(__name__)

# Define Markdown extensions and their configurations
extensions = ['fenced_code', 'footnotes', 'meta', 'smarty', 'tables', 'toc', 'codehilite']
extensions_configs = {
        'smarty': {'smart_dashes': True, 'smart_quotes': True, 'smart_angled_quotes': True, 'smart_ellipses': True},
        'codehilite': {'use_pygments': True, 'css_class': 'highlight'}
    }

# Function to read Markdown file and convert to HTML
def read_markdown(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    md = markdown.Markdown(output_format='html', extensions=extensions, extension_configs=extensions_configs)
    html_content = md.convert(content)

    metadata = getattr(md, 'Meta', {})
    metadata = {key: ', '.join(value) if key != 'tags' else value[0].split(', ') for key, value in metadata.items()}

    # Get css from static/styles.css file
    with open('static/styles.css', 'r', encoding='utf-8') as css_file:
        css = css_file.read()

    data = DocsModel(html=html_content, css=css, **metadata)
    content = data.model_dump()

    return content, metadata

# Route to render Markdown files
@app.route('/<path:slug>/')
def render_markdown(slug):
    # Assuming slug corresponds to folder structure
    file_path = os.path.join('docs', slug + '.md')

    # Check if file exists
    if not os.path.isfile(file_path):
        abort(404)

    # Read Markdown file and convert to HTML
    content, metadata = read_markdown(file_path)

    # Render HTML
    return render_template('markdown.html', html_content=content["html"], metadata=metadata)

if __name__ == '__main__':
    app.run(debug=True)
