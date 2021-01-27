def compute_windchill(temp, vel):
    """
    Compute the wind chill factor given the temperature and wind speed

    NOTE: This computation is valid only for temperatures between -45F and +45F and for wind speeds between 3 mph and
    60 mph.

    Parameters:
        temp: The temperature in units of F (float)
        vel: The wind speed in units of mph (float)
    """

    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    vel16 = vel**0.16
    wci = a + (b*temp) - (c*vel16) + (d*temp*vel16)
    return wci


def compute_heatindex(temp, hum):
    """
    Compute the heat index given the temperature and the humidity

    Parameters:
        temp: The temperature in units of F (float)
        hum: The relative humidity in units of % (float)
    """

    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    rh = hum/100
    hi = a + (b * temp) + (c * rh) + (d * temp * rh) + (e * temp**2) + (f * rh**2) + (g * temp**2 * rh) + \
        (h * temp * rh**2) + (i * temp**2 * rh**2)
    return hi
