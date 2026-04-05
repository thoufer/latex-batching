## Purpose
The intent of this code is to take a csv file containing information about project 
proposals to CDI for the current fiscal year and build a pdf of each proposal for 
reviewers. 

PDFs can be rendered via 2 different mechanisms; XeLaTex or [weasyprint]
(https://weasyprint.org). Xelatex is used over pdfLaTeX solely to access underlying 
Windows font Calibri.  Both methods utilize [Jinja]
(https://jinja.palletsprojects.com/en/stable/) is as the template rendering engine.  


## Installation
This project was built using uv and python 3.14.  It requires that you have a LaTeX 
distribution installed locally, and the path to those binaries are on your system path 
(usually done by the installer). 

If you have uv you can get up and running via:
```commandline
 cd /path/to/LaTeX-batching/
 uv init
 uv sync
```

No uv?  Create you virtual environment.  
```commandline
 pip install jijna2 weasyprint
```

## Usage
There are 2 example build files; main.py and main-weasprint.py.  The main.py builds pdfs
using XeLatex and points to the soi-template.tex.jinja build template.  The 
main-weasyprint uses weasyprint as the underlying build.  Weasyprint offers an 
interesting use case, as we can mirror the same build process as XeLaTex (data -> 
template -> PDF), but we can also use the same command to build a custom html file 
that could be use for web display as well as the PDF, and these layouts may be 
different. This is handled with different css files.

## Notes, remaining challenges and questions
During development there were a number of "what if" that might need to be addressed
should this be considered for any sort of production.

1. How does the submitter relate to the primary investigator (e.g., should submitter 
attributes be elsewhere?)
  
2. Currently, I put the lead_pi_role as an attribute of the project.  If co-leads also 
have "roles" may be this should be incorporated into the investigator class. 

3. If a project can have more than 2 Investigators then the project class needs 
modification, and the template will need looping functionality to print all team members. 

4. If and instance of the investigator only has a name it will be rendered as <name> 
followed by an em dash but nothing else.  The em dash should only be rendered _if_ there 
are attributes to also be rendered

5. The escape_tex "filter" may need to be applied to more attributes than I currently do.

6. .Should rendered pdfs have a different naming scheme?