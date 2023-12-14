""" Useful Functions
"""
def validate(coords: list[str]) -> bool:
    for coord in coords:
        try:
            int_coord = int(coord)
            float_coord = float(coord)
            if int_coord != float_coord:
                return False
        except ValueError:
            return False
    return True
