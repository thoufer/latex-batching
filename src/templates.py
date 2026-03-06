from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from .utils import escape_tex


# Setup jinja environmnent and load the necssary template
env = Environment(loader=FileSystemLoader(Path('templates')))

# Add helper to jinja filters so certain characters render correctly in tex file.
env.filters['escape_tex'] = escape_tex