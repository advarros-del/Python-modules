from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = light_spell_allowed_ingredients()
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
    allowed_ingredients = [ingredient.capitalize() for ingredient in allowed_ingredients]
    ingredients_list = [ingredient.capitalize() for ingredient in ingredients_list]
    boolenan: bool = False
    for ingredient in ingredients_list:
        if ingredient in allowed_ingredients:
            boolenan = True
    if boolenan == False:
        return f"{ingredients} - INVALID)"
    return f"{ingredients} - VALID)"
    