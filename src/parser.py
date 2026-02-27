import csv
import pathlib
from typing import Generator

from models import Investigator, Project

def read_cdi_csv(file: pathlib.Path) -> Generator[Project] :
    """ This function is responsible for reading the function and mapping the appropriate
        column in to the appropraite attribute.

    :param file:
    :return: A generator of projects
    """
    try:
        with open(file=file, mode="r", newline="", encoding="UTF-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                lead = Investigator(
                    name=row['leadpi_name'],
                    email=row['leadpi_email'],
                    center=row['leadpi_sc'],
                    mission_area=row['leadpi_ma'],
                    city=row['leadpi_city'],
                    state=row['leadpi_state'],
                    career_stage=row['leadpi_career_stage']
                )

                project = Project(
                    id=row['project_id'],
                    title=row['project_title'],
                    short_title=row['short_title'],
                    impact_statement=row['impact_statement'],
                    theme_explanation=row['theme_explanation'],
                    objective=row['objective'],
                    benefits=row['benefits'],
                    measure_success=row['measure_success'],
                    lead_pi=lead,
                    lead_role=row['leadpi_role'],
                    submitter_name=row['submitter_name'],
                    submitter_email=row['submitter_email'],
                    themes=row['themes'].split(';'),
                    collab_areas=row['collab_areas'].split(';'),

                    # don't add ssf_elements if there is not value or its an empty string.
                    ssf_elements=[val for val in (row['ssf_1'], row['ssf_2'], row['ssf_3']) if
                                  val is not None or val == '']
                )

                # Let's add the co-lead after project creation. As its reasonable to assume
                # that a project is by a single Investigator
                if row['copi1_name']:
                    project.co_lead = Investigator(name=row['copi1_name'])

                yield project
    except FileNotFoundError:
        print(f'file {file} was not found.')
