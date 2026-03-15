"""
    This build file builds a PDF document from an HTML and CSS styling using weasyprint.

    NOTE: weasyprint has an external dependency for the Pango library maintained by GTK.
    Installing on Windows may be a chore, given that GTK is linux os based.  So,
    recommendation is to run this via MacOS, Docker, or possibly WSL2, but I haven't
    tested on anything other than MacOS.
"""
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from weasyprint import HTML, CSS

from src.parser import read_cdi_csv


env = Environment(loader=FileSystemLoader(Path('templates')))
template = env.get_template('soi-template.html')


def main(file: str, build_target: str) -> None:
    projects = read_cdi_csv(file)

    for project in projects:
        target_path = Path(build_target)
        target_path.mkdir(parents=True, exist_ok=True)
        target_file = target_path / f'Statement-{project.id}'

        # This render the jinja template the HTML directly to a string which is stored in
        # python, and then that string is passed to weasyprint to render the final PDF.
        rendered_html = template.render(project=project)
        document = HTML(string=rendered_html).render(
            stylesheets=[CSS('static/css/soi-template.css')])
        document.write_pdf(target_file.with_suffix('.pdf'))

        # This code block renders the jinja template into an HTML file stored locally.
        # That HTML file is then passed to weasyprint to render the final PDF.  NOTE
        # we can render the HTML and PDF using different underlying CSS layouts,
        # potentially making this more flexible in a production setting.
        # html_file = open(target_file.with_suffix('.html'), 'w')
        # html_file.write(rendered_html)
        # html_file.close()

        # document = HTML(string=rendered_html).render(
        #     stylesheets=[CSS('static/css/soi-template.css')])
        # document.write_pdf(target_file.with_suffix('.pdf'))


if __name__ == "__main__":
    main(file='fy26-example-input.csv', build_target='build/html/')
