def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit_messages = {
        'packets': f'{quantity} {unit} available',
        'grams': f'{quantity} {unit} total',
        'area': f'covers {quantity} square meters'
    }
    message = unit_messages.get(unit, None)
    if message is None: print("Unknown unit type")
    else: print(f'{seed_type.capitalize()} seeds: {message}')
