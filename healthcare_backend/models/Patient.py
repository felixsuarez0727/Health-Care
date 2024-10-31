from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Patient(BaseModel):
    Patient:Optional[str]=None
    Labcode:Optional[str]=None
    Project:Optional[str]=None
    Cohort:Optional[str]=None
    CaseId:Optional[str]=None
    Center:Optional[str]=None
    CenterCode:Optional[str]=None
    TrialCode:Optional[str]=None
    ExternalId:Optional[str]=None
    Specie:Optional[str]=None
    Consent:Optional[str]=None
    Disease:Optional[str]=None
    EvolutiveStage:Optional[str]=None
    DiagnosisState:Optional[str]=None
    DiagnosisDate:Optional[datetime]=None
    InclusionDate:Optional[datetime]=None
