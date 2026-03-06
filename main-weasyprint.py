from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from weasyprint import HTML

from src.parser import read_cdi_csv


env = Environment(loader=FileSystemLoader(Path('templates')))
template = env.get_template('templates/soi-template.html')


def main(file: str, build_target: str) -> None:
    projects = read_cdi_csv(file)

    for project in projects:
        target_path = Path(build_target)
        target_path.mkdir(parents=True, exist_ok=True)
        target_file = target_path / f'Statement-{project.id}.tex'

        rendered_html = template.render(project=project)
        html_object = HTML(string=rendered_html)
        html_object.write_pdf(target_file)


if __name__ == "__main__":
    main(file='fy26-example-input.csv', build_target='build/html/')
