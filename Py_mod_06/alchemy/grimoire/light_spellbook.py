from .light_validator import validate_ingredients

def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    return f"{spell_name}: {validate_ingredients(ingredients)}"
    