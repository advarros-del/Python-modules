from pydantic import BaseModel, Field, DataTime

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_lenght=10)
    name: str = Field(min_length=1, max_lenght=50)
    crew_size: int = Field(min_length=1, max_lenght=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float =  Field(ge=0.0, le=100.0)
    last_maintenance: DataTime
    is_operational: bool = True
    notes: str = Field(max_lenght=200)


def main() -> None:
    good_mod = SpaceStation("ISS001", "International Space Station", 6, 85.5, 92.3, 15/6/1955, True, "")
    bad_mod = SpaceStation("a", "international brown balls", "z", 134, 541, False)
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {good_mod.station_id}")
    print(f"Crew: {good_mod.crew_size}")
    print(f"Power: {good_mod.power_level}")
    print(f"Oxygen: {good_mod.oxygen_level}")
    if good_mod.is_operational:
        print(f"Status: Operational")
    else:
        print(f"Status: Inoperational")
    print("\n========================================")
    print("Expected validation error:")
    print(f"Crew: {bad_mod.crew_size}")


if __name__ == "__main__":
    main()
