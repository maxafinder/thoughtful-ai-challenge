from enum import Enum


class PackageType(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def validate_inputs(width, height, length, mass):
    if not all(isinstance(x, (int, float)) for x in [width, height, length, mass]):
        raise ValueError("All inputs must be numbers.")
    if min(width, height, length) <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    if mass < 0:
        raise ValueError("Mass cannot be negative.")


def is_heavy(mass):
    return mass >= 20


def is_bulky(width, height, length):
    volume = width * height * length
    return volume >= 1_000_000 or max(width, height, length) >= 150


def sort(width, height, length, mass):
    validate_inputs(width, height, length, mass)
    heavy = is_heavy(mass)
    bulky = is_bulky(width, height, length)

    if heavy and bulky:
        return PackageType.REJECTED
    elif heavy or bulky:
        return PackageType.SPECIAL
    else:
        return PackageType.STANDARD
