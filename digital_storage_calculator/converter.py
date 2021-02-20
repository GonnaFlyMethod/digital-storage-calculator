from data_units.simple_units import Bit, Byte;

from data_units.binary_based_on_bits_units import (Kibibit, Mebibit, Gibibit, Tebibit,
                                                   Pebibit, Exbibit, Zebibit, Yobibit)
from data_units.binary_based_on_bytes_units import (Kibibyte, Mebibyte, Gibibyte, Tebibyte,
							                        Pebibyte, Exbibyte, Zebibyte, Yobibyte)

from data_units.decimal_based_on_bits_units import (Kilobit, Megabit, Gigabit, Terabit,
								                    Petabit, Exabit, Zettabit, Yottabit)
from data_units.decimal_based_on_bytes_units import (Kilobyte, Megabyte, Gigabyte, Terabyte,
								                     Petabyte, Exabyte, Zettabyte, Yottabyte)


class Converter:
	
	_byte_units_methods_storage = {
	# 1) Simple units
		"B": Byte.convert_from_bits_to_bytes,

	# 2) Binary units

		# 2.1) Binary units that are based on bits
		"Kibit": Kibibit.convert_from_bits_to_kibibits,
		"Mibit": Mebibit.convert_from_bits_to_mebibits,
		"Gibit": Gibibit.convert_from_bits_to_gibibits,
		"Tibit": Tebibit.convert_from_bits_to_tebibits,
		"Pibit": Pebibit.convert_from_bits_to_pebibits,
		"Eibit": Exbibit.convert_from_bits_to_exbibits,
		"Zibit": Zebibit.convert_from_bits_to_zebibits,
		"Yibit": Yobibit.convert_from_bits_to_yobibits,
		
		# 2.2) Binary units that are based on bytes
		"KiB": Kibibyte.convert_from_bits_to_kibibytes,
		"MiB": Mebibyte.convert_from_bits_to_mebibytes,
		"GiB": Gibibyte.convert_from_bits_to_gibibytes,
		"TiB": Tebibyte.convert_from_bits_to_tebibytes,
		"PiB": Pebibyte.convert_from_bits_to_pebibytes,
		"EiB": Exbibyte.convert_from_bits_to_exbibytes,
		"ZiB": Zebibyte.convert_from_bits_to_zebibytes,
		"YiB": Yobibyte.convert_from_bits_to_yobibytes,
			
	# 3) Decimal units
	
		# 3.1) Decimal units that are based on bits
		"kbit": Kilobit.convert_from_bits_to_kilobits,
		"Mbit": Megabit.convert_from_bits_to_megabits,
		"Gbit": Gigabit.convert_from_bits_to_gigabits,
		"Tbit": Terabit.convert_from_bits_to_terabits,
		"Pbit": Petabit.convert_from_bits_to_petabits,
		"Ebit": Exabit.convert_from_bits_to_exabits,
		"Zbit": Zettabit.convert_from_bits_to_zettabits,
		"Ybit": Yottabit.convert_from_bits_to_yottabits,

		# 3.2) Decimal units that are based on bits
		"B":  Byte.convert_from_bits_to_bytes,
		"KB": Kilobyte.convert_from_bits_to_kilobytes,
		"MB": Megabyte.convert_from_bits_to_megabytes,
		"GB": Gigabyte.convert_from_bits_to_gigabytes,
		"TB": Terabyte.convert_from_bits_to_terabytes,
		"PB": Petabyte.convert_from_bits_to_petabytes,
		"EB": Exabyte.convert_from_bits_to_exabytes,
		"ZB": Zettabyte.convert_from_bits_to_zettabytes,
		"YB": Yottabyte.convert_from_bits_to_yottabytes
		
	}

	@classmethod
	def convert(cls, value_from, value_to, return_in_bits=False):
		value_from_in_bits = value_from.get_val_in_bits()

		if value_to.id == "bit":
			result_scientific_notation = "%.2e" % value_from_in_bits
			return result_scientific_notation
		else:
			method_for_conversion = cls._byte_units_methods_storage[value_to.id]
			final_result = method_for_conversion(value_to, value_from_in_bits)

			if return_in_bits:
				return value_from._convert_into_bits(final_result)
			return final_result
