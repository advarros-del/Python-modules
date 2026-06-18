from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validator(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("The id must start with 'AC'")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if (
            self.contact_type == ContactType.PHYSICAL
            and self.is_verified is False
        ):
            raise ValueError("Physical contact must be verified")
        if (
            self.signal_strength > 7.0
            and len(self.message_received.strip()) == 0
        ):
            raise ValueError(
                "Radio contact requires at least 7 "
                "strength signal and a message.")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        time: datetime = datetime.fromisoformat("1994-07-23T10:00:00")
        good_al = AlienContact(contact_id="AC_2024_001",
                               timestamp=time,
                               location="Area 51, Nevada",
                               contact_type=ContactType.RADIO,
                               signal_strength=8.5,
                               duration_minutes=45,
                               witness_count=5,
                               message_received="Greetings from Zeta Reticuli",
                               is_verified=False)
        print(f"ID: {good_al.contact_id}")
        print(f"Type: {good_al.contact_type}")
        print(f"Location: {good_al.location}")
        print(f"Signal: {good_al.signal_strength}/10")
        print(f"Duration: {good_al.duration_minutes} minutes")
        print(f"Witnesses: {good_al.witness_count}")
        print(f"Message: '{good_al.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]['msg'].split(", ", 1)[1])
    print("\n======================================")
    print("Expected validation error:")
    try:
        time1: datetime = datetime.fromisoformat("1994-07-23T10:00:00")
        bad_al = AlienContact(contact_id="AC_2024_001",
                              timestamp=time1,
                              location="Area 51, Nevada",
                              contact_type=ContactType.TELEPATHIC,
                              signal_strength=8.5,
                              duration_minutes=45,
                              witness_count=2,
                              message_received="Greetings from Zeta Reticuli",
                              is_verified=False)
        print(f"ID: {bad_al.contact_id}")
    except ValidationError as e:
        print(e.errors()[0]['msg'].split(", ", 1)[1])


if __name__ == "__main__":
    main()
