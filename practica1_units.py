import numpy as np

import metpy.calc as mpcalc
from metpy.units import units

distance = np.arange(1, 5) * units.meters
time = units.Quantity(np.arange(2, 10, 2), 'sec')
gravity=9.81 * units.meter / (units.second * units.second)
9.81 * units('m/s^2')

print(distance / time)

temperature = 73.2 * units.degF
rh = 64 * units.percent
dewpoint = mpcalc.dewpoint_from_relative_humidity(temperature, rh)

print(dewpoint)
print(dewpoint.to('degF'))