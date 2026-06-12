from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float =  Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str = Field(max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        good_mod = SpaceStation(station_id="ISS001", name="International Space Station", 
                                crew_size=6, power_level=85.5, oxygen_level=92.3,
                                last_maintenance="1995-05-22", is_operational=True, notes="")
        print("Valid station created:")
        print(f"ID: {good_mod.station_id}")
        print(f"Name: {good_mod.name}")
        print(f"Crew: {good_mod.crew_size}")
        print(f"Power: {good_mod.power_level}")
        print(f"Oxygen: {good_mod.oxygen_level}")
        if good_mod.is_operational:
            print(f"Status: Operational")
        else:
            print(f"Status: Inoperational")
    except ValidationError as e:
        print(e.errors()[0]['msg'])
    print("\n========================================")
    print("Expected validation error:")
    try:
        bad_mod = SpaceStation(station_id="ISS001", name="International Space Station", 
                               crew_size=6, power_level=185.5, oxygen_level=92.3,
                               last_maintenance="1995-05-22", is_operational=True, notes="")
    except ValidationError as e:
        print(e.errors()[0]['msg'])

if __name__ == "__main__":
    main()