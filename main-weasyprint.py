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

        # render directly from string
        rendered_html = template.render(project=project)
        document = HTML(string=rendered_html).render(
            stylesheets=[CSS('static/css/soi-template.css')])
        document.write_pdf(target_file.with_suffix('.pdf'))

        # render from intermediate html file
        # html_file = open(target_file.with_suffix('.html'), 'w')
        # html_file.write(rendered_html)
        # html_file.close()

        # document = HTML(string=rendered_html).render(
        #     stylesheets=[CSS('static/css/soi-template.css')])
        # document.write_pdf(target_file.with_suffix('.pdf'))


if __name__ == "__main__":
    main(file='fy26-example-input.csv', build_target='build/html/')
