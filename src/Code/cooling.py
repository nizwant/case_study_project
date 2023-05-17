def cooling(
        cooling_rate: float,
        temperature: float,
        min_temperature: float
) -> float:
    """
    Performs cooling on given temperature.
    """
    new_temperature = cooling_rate * temperature
    return max(new_temperature, min_temperature)
