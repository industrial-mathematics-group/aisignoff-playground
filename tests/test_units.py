import math

import pytest

from playground.units import celsius_to_fahrenheit, celsius_to_kelvin, kelvin_to_celsius


def test_round_trip():
    assert math.isclose(kelvin_to_celsius(celsius_to_kelvin(21.5)), 21.5)


def test_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212


def test_negative_kelvin():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)
