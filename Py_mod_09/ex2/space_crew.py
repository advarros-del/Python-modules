from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum

class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    timestamp: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    year_experience: int = Field(ge=0, le=50)
    is_active: bool = True

class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_time: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list = Field(CrewMember, ge=1, le=12)
    mission_status: str = "Planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)
    
    @model_validator(mode=’after’)
    def mission_validator(self):
        if not self.mission_id.startswith("M"):
            pass
        if not "commander" in self.crew or not "captain" in self.crew:
            pass
        if self.duration_days > 365 and self.crew.year_experience(): #sumar
            pass
        if false in self.crew.CrewMember.is_active :
            pass

def main() -> None:
    pass

if __name__ == "__main__":
    main()
