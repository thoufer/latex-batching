from dataclasses import dataclass, field


@dataclass
class Investigator:
    """ An object representing a research investigator on a project """
    name: str
    center: str = None
    mission_area: str = None
    email: str = None
    region: str = None
    city: str = None
    state: str = None
    career_stage: str = None


@dataclass
class Project:
    """ A CDI project """
    id: str
    title: str
    short_title: str
    impact_statement: str
    theme_explanation: str
    objective: str
    benefits: str
    measure_success: str
    lead_pi: Investigator
    lead_role: str
    submitter_name: str
    submitter_email: str
    co_lead: Investigator = None
    ssf_elements: list[str] = field(default_factory=list)
    themes: list[str] = field(default_factory=list)
    collab_areas: list[str] = field(default_factory=list)
