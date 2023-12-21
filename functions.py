""" Useful Functions
"""
def validate(coords: list[str]) -> bool:
    """Coordinates validation function

    Args:
        coords (list[str]): list of coordinates

    Returns:
        bool: True if validation is OK, else - False
    """
    for coord in coords:
        try:
            int_coord = int(coord)
            float_coord = float(coord)
            if int_coord != float_coord:
                return False
        except ValueError:
            return False
    return True
