from byte_units.binary import (Kibibyte, Mebibyte, Gibibyte, Tebibyte,
							   Pebibyte, Exbibyte, Zebibyte, Yobibyte)
from byte_units.decimal import (Kilobyte, Megabyte, Gigabyte, Terabyte,
								Petabyte, Exabyte, Zettabyte, Yottabyte)

class Converter:

	_byte_units_methods_storage = {
		# Binary units
		"KiB": Kibibyte.convert_from_bytes_to_kibibytes,
		"MiB": Mebibyte.convert_from_bytes_to_mebibytes,
		"GiB": Gibibyte.convert_from_bytes_to_gibibytes,
		"TiB": Tebibyte.convert_from_bytes_to_tebibytes,
		"PiB": Pebibyte.convert_from_bytes_to_pebibytes,
		"EiB": Exbibyte.convert_from_bytes_to_exbibytes,
		"ZiB": Zebibyte.convert_from_bytes_to_zebibytes,
		"YiB": Yobibyte.convert_from_bytes_to_yobibytes,
			
		# Decimal units
		"KB": Kilobyte.convert_from_bytes_to_kilobytes,
		"MB": Megabyte.convert_from_bytes_to_megabytes,
		"GB": Gigabyte.convert_from_bytes_to_gigabytes,
		"TB": Terabyte.convert_from_bytes_to_terabytes,
		"PB": Petabyte.convert_from_bytes_to_petabytes,
		"EB": Exabyte.convert_from_bytes_to_exabytes,
		"ZB": Zettabyte.convert_from_bytes_to_zettabytes,
		"YB": Yottabyte.convert_from_bytes_to_yottabytes
		
	}
	
	@classmethod
	def convert(cls, value_from, value_to, return_in_bytes=False):
		value_from_in_bytes = value_from.get_val_in_bytes()
		method_for_conversion = cls._byte_units_methods_storage[value_to.id]
		final_result = method_for_conversion(value_to, value_from_in_bytes)
		
		if return_in_bytes:
			return value_from._convert_into_bytes(final_result)
		return final_result
