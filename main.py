import subprocess

from pathlib import Path

from src.parser import read_cdi_csv
from src.templates import env

def _compile(file, build_target) -> int:
    """ Compile the provided tex file to a pdf and return the result code of compilation
    0 for success 1 for failure.  Note, that its still possible that there are issues with the
    layout of the document despite a successful build.

    :param file: a rendered tex file from jinja
    :param build_target: the folder where the pdf should be compiled to
    :return: Returns a 0 if xelatex compiled successful or 1 if it failed during
        compilation.
    """
    output =  f"-output-directory={build_target}"
    proc = subprocess.run(
        ['xelatex', output, "-shell-escape", "-interaction=nonstopmode", file],
        stdout=subprocess.DEVNULL
    )
    return proc.returncode


def _cleanup(build_directory: Path, keep_tex_source: bool) -> None:
    """
    Delete intermediate files created by xelatex that are not needed after succssful build.

    keep_tex_source:  If set to True then the tex file used to build the pdf will be kept,
        otherwise its deleted and just final pdfs are retained.
    """
    extensions = {".aux", ".log", ".tex"}
    if keep_tex_source:
        extensions = {".aux", ".log"}

    for file in build_directory.rglob("*"):
        if file.suffix.lower() in extensions:
            file.unlink()


def main(file: str, build_target: str, keep_tex_source: bool = True) -> None:
    """ Main function which coordinates all of the processing and build steps.

    :param file:  The filename of the CSV containing the project data.

    :param build_target: The folder where project pdfs should be build too.

    :param keep_tex_source:  If True, the tex file created by Jinja will be kept. This
        allow a user to potentially edit a specific tex file and then re-build the pdf
        in a one off process.  These changes will not be retained if this script is run
        again.

    :return: None
    """
    template = env.get_template('soi-template.tex.jinja')

    # Grab data.  This is a generator so it returns 1 row each time
    # project is called via iterations
    projects = read_cdi_csv(file)

    # Build current project to pdf and then cleaup after the build, if successful.
    for project in projects:
        target_path = Path(build_target)
        target_path.mkdir(parents=True, exist_ok=True)
        target_file = target_path / f'Statement-{project.id}.tex'

        rendered_tex = template.render(project=project)
        f = open(target_file, "w", encoding="utf-8")
        f.write(rendered_tex)
        f.close()

        print(f'Buliding pdf: {target_file.name}')
        result = _compile(str(target_file.as_posix()), build_target)

        if result == 1:
            print(f'Tex file {target_file.name} failed to build.')

        _cleanup(target_path, keep_tex_source)


if __name__ == "__main__":
    main('fy26-example-input.csv', build_target="./build", keep_tex_source=True)