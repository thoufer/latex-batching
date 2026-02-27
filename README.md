## Purpose
The intent of this code is to take a csv file containing information about project proposale to CDI for the current
fiscal year. That information is rendered into a pdf via XeLaTeX. XeLateX is used over pdfLaTeX solely to access 
underlying Windows font Calibri.  [Jinja](https://jinja.palletsprojects.com/en/stable/) is used as the template 
rendering engine.  If one is well versed in HTML and CSS, one might consider abandoning LaTeX altogether and use 
[weasyprint](https://weasyprint.org).  

## Installation
This project was built using uv and python 3.14.  It requires that you have a TeX distribution installed locally, and
the path to those binaries are on your system path (usually done by the installer). 

If you have uv you can get up and running via:
```commandline
 cd /path/to/LaTeX-batching/
 uv init
 uv sync
```

No uv?  Create you virtual environment.  The only pthon-dependency is jinja.
```commandline
 pip install jijna2
```

 ## Notes, remaining challenges and questions
    * How does the submitter relate to the primary investigator (e.g., should submitter attributes be elsewhere?)
    * Currently, I put the the lead_pi_role as an attribute of the project.  If co-leads also have "roles" may be
        this should be incorportated into the investigator class.
    * If a project can have more than 2 Investigators then the project class needs modification, and the template 
        will need looping functionality to print all team members.
    * If and instance of the investigator only has a name it will be rendered as <name> followed by an em dash
        but nothing else.  The em dash should only be rendered _if_ there are are attributes to also be rendered
    * The escape_tex "filter" may need to be applied to more attributes than I currently do.
    * Should rendered pdfs have a different naming scheme?