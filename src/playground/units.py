"""Unit conversions for temperatures."""

ZERO_CELSIUS = 273.15


def celsius_to_kelvin(c):
    """Degrees Celsius to kelvin."""
    return c + ZERO_CELSIUS


def kelvin_to_celsius(k):
    """Kelvin to degrees Celsius."""
    if k < 0:
        raise ValueError("a temperature in kelvin can't be negative")
    return k - ZERO_CELSIUS


def celsius_to_fahrenheit(c):
    """Degrees Celsius to degrees Fahrenheit."""
    return c * 9 / 5 + 32
