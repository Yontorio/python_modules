from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    normalized = ingredients.lower()
    valid = any(item in normalized
                for item in dark_spell_allowed_ingredients())
    result = "VALID" if valid else "INVALID"
    return f"{ingredients} - {result}"
