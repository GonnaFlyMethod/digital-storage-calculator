from data_units.simple_units import Bit, Byte;

from data_units.binary_based_on_bits_units import (Kibibit, Mebibit, Gibibit, Tebibit,
                                                   Pebibit, Exbibit, Zebibit, Yobibit)
from data_units.binary_based_on_bytes_units import (Kibibyte, Mebibyte, Gibibyte, Tebibyte,
							                        Pebibyte, Exbibyte, Zebibyte, Yobibyte)

from data_units.decimal_based_on_bits_units import (Kilobit, Megabit, Gigabit, Terabit,
								                    Petabit, Exabit, Zettabit, Yottabit)
from data_units.decimal_based_on_bytes_units import (Kilobyte, Megabyte, Gigabyte, Terabyte,
								                     Petabyte, Exabyte, Zettabyte, Yottabyte)


class DataUnitCreator:
	
	data_units_classes_storage = {
	# 1) Simple units
		"B": Byte.convert_from_bits_to_bytes,

	# 2) Binary units

		# 2.1) Binary units that are based on bits
		"Kibit": Kibibit,
		"Mibit": Mebibit,
		"Gibit": Gibibit,
		"Tibit": Tebibit,
		"Pibit": Pebibit,
		"Eibit": Exbibit,
		"Zibit": Zebibit,
		"Yibit": Yobibit,
		
		# 2.2) Binary units that are based on bytes
		"KiB": Kibibyte,
		"MiB": Mebibyte,
		"GiB": Gibibyte,
		"TiB": Tebibyte,
		"PiB": Pebibyte,
		"EiB": Exbibyte,
		"ZiB": Zebibyte,
		"YiB": Yobibyte,
			
	# 3) Decimal units
	
		# 3.1) Decimal units that are based on bits
		"kbit": Kilobit,
		"Mbit": Megabit,
		"Gbit": Gigabit,
		"Tbit": Terabit,
		"Pbit": Petabit,
		"Ebit": Exabit,
		"Zbit": Zettabit,
		"Ybit": Yottabit,

		# 3.2) Decimal units that are based on bits
		"B":  Byte,
		"KB": Kilobyte,
		"MB": Megabyte,
		"GB": Gigabyte,
		"TB": Terabyte,
		"PB": Petabyte,
		"EB": Exabyte,
		"ZB": Zettabyte,
		"YB": Yottabyte
		
	}
