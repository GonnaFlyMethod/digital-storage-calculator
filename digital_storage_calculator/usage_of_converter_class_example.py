from all_data_units import *
from converter import Converter


Ybit = Yottabit(1)
b = Bit(1)
new_conversion = Converter();
print(new_conversion.convert(Ybit, b));