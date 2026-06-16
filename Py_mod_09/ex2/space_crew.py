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
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "Planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validator(self):
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Invalid id. You must introduce a valid id")
        ranks: list = [member.timestamp for member in self.crew]
        if Rank.COMMANDER not in ranks and Rank.CAPTAIN not in ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        if (
            self.duration_days > 365
            and sum(member.year_experience for member in self.crew) < 5
        ):
            raise ValueError(
                "The  total experience for this mission is not enough")
        if any(member.is_active is False for member in self.crew):
            raise ValueError("All the crew memebers have to be active.")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    try:
        member1 = CrewMember(member_id="Cap13",
                             name="Sarah Connor",
                             timestamp=Rank.COMMANDER,
                             age=45,
                             specialization="Mission Command",
                             year_experience=15,
                             is_active=True
                             )
        member2 = CrewMember(member_id="Lieut12",
                             name="John Smith",
                             timestamp=Rank.LIEUTENANT,
                             age=22,
                             specialization="Navigation",
                             year_experience=3,
                             is_active=True
                             )
        member3 = CrewMember(member_id="Off44",
                             name="Alice Johnson",
                             timestamp=Rank.OFFICER,
                             age=31,
                             specialization="Engineering",
                             year_experience=5,
                             is_active=True
                             )
        member4 = CrewMember(member_id="Pop13",
                             name="Bob Bobber",
                             timestamp=Rank.CADET,
                             age=18,
                             specialization="Clean WC",
                             year_experience=1,
                             is_active=True
                             )
    except ValueError as e:
        print(e)
    try:
        good_mis = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_time="2994-07-23",
            duration_days=900,
            crew=[member1, member2, member3],
            mission_status="Planned",
            budget_millions=2500
        )
        print(f"Mission: {good_mis.mission_name}")
        print(f"ID: {good_mis.mission_id}")
        print(f"Destination: {good_mis.destination}")
        print(f"Duration: {good_mis.duration_days} days")
        print(f"Budget: ${good_mis.budget_millions}M")
        print(f"Crew size: {len(good_mis.crew)}")
        print("Crew members:")
        for member in good_mis.crew:
            print(f"- {member.name} ({member.timestamp.value}) -"
                  f" {member.specialization})")
    except ValidationError as e:
        print(e.errors()[0]['msg'].split(", ", 1)[1])
    print("\n=========================================")
    print("Expected validation error:")
    try:
        bad_mis = SpaceMission(
            mission_id="M2045_SUN",
            mission_name="GOES TO SUN",
            destination="Sun",
            launch_time="3994-07-23",
            duration_days=200,
            crew=[member2, member4],
            mission_status="Planned",
            budget_millions=1500
        )
        print(f"Mission: {bad_mis.mission_name}")
        print(f"ID: {bad_mis.mission_id}")
        print(f"Destination: {bad_mis.destination}")
        print(f"Duration: {bad_mis.duration_days} days")
        print(f"Budget: ${bad_mis.budget_millions}M")
        print(f"Crew size: {len(bad_mis.crew)}")
        print("Crew members:")
        for member in bad_mis.crew:
            print(f"- {member.name} ({member.timestamp} -"
                  f" {member.specialization})")
    except ValidationError as e:
        print(e.errors()[0]['msg'].split(", ", 1)[1])


if __name__ == "__main__":
    main()
