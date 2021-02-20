class Kibibyte:

	def __init__(self, value_kibibytes: int):
		self._value_kibibytes = value_kibibytes
		self.one_kibibyte_in_bits = 8192
		self._value_bits = self._convert_into_bits(value_kibibytes)
		self.id = "KiB"
	
	def _convert_into_bits(self, value_kibibytes: int) -> int:
		return value_kibibytes * self.one_kibibyte_in_bits
	
	def convert_from_bits_to_kibibytes(self, bits: int) -> float:
		return (bits / self.one_kibibyte_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_kibibytes(self) -> int:
		return self._value_kibibytes


class Mebibyte:

	def __init__(self, value_mebibytes: int):
		self._value_mebibytes = value_mebibytes
		self.one_mebibyte_in_bits = 8.389e+6
		self._value_bits = self._convert_into_bits(value_mebibytes)
		self.id = "MiB"
	
	def _convert_into_bits(self, value_mebibytes: int) -> int:
		return value_mebibytes * self.one_mebibyte_in_bytes
	
	def convert_from_bits_to_mebibytes(self, bits: int) -> float:
		return (bits / self.one_mebibyte_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_mebibytes(self) -> int:
		return self._value_mebibytes
	

class Gibibyte:

	def __init__(self, value_gibibytes: int):
		self._value_gibibytes = value_gibibytes
		self.one_gibibyte_in_bits = 8.59e+9
		self._value_bits = self._convert_into_bits(value_gibibytes)
		self.id = "GiB"
	
	def _convert_into_bits(self, value_gibibytes: int) -> int:
		return value_gibibytes * self.one_gibibyte_in_bits
	
	def convert_from_bits_to_gibibytes(self, bits: int) -> float:
		return (bits / self.one_gibibyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_gibibytes(self) -> int:
		return self._value_gibibytes


class Tebibyte:

	def __init__(self, value_tebibytes: int):
		self._value_tebibytes = value_tebibytes
		self.one_tebibyte_in_bits = 8.796e+12
		self._value_bits = self._convert_into_bits(value_tebibytes)
		self.id = "TiB"
	
	def _convert_into_bits(self, value_terabytes: int) -> int:
		return value_terabytes * self.one_tebibyte_in_bits
	
	def convert_from_bits_to_tebibytes(self, bits: int) -> float:
		return (bits / self.one_tebibyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_terabytes(self) -> int:
		return self._value_tebibytes

		
class Pebibyte:
	
	def __init__(self, value_pebibytes: int):
		self._value_pebibytes = value_pebibytes
		self.one_pebibyte_in_bits = 9.007e+15
		self._value_bits = self._convert_into_bits(value_pebibytes)
		self.id = "PiB"
	
	def _convert_into_bits(self, value_petabytes: int) -> int:
		return value_petabytes * self.one_pebibyte_in_bits
	
	def convert_from_bits_to_pebibytes(self, bits: int) -> float:
		return (bits / self.one_pebibyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_pebibytes(self) -> int:
		return self._value_pebibytes

		
class Exbibyte:

	def __init__(self, value_exbibytes: int):
		self._value_exbibytes = value_exabytes
		self.one_exbibyte_in_bits = 9.223e+18
		self._value_bits = self._convert_into_bits(value_exbibytes)
		self.id = "EiB"
	
	def _convert_into_bits(self, value_exabytes: int) -> int:
		return value_exabytes * self.one_exbibyte_in_bits
	
	def convert_from_bits_to_exbibytes(self, bits: int) -> float:
		return (bits / self.one_exbibyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_exbibytes(self) -> int:
		return self._value_exbibytes


class Zebibyte:

	def __init__(self, value_zebibytes: int):
		self._value_zebibytes = value_zebibytes
		self.one_zebibyte_in_bits = 9.445e+21
		self._value_bits = self._convert_into_bits(value_zebibytes)
		self.id = "ZiB"
	
	def _convert_into_bits(self, value_zettabytes: int) -> int:
		return value_zettabytes * self.one_zebibyte_in_bytes
	
	def convert_from_bits_to_zebibytes(self, bits: int) -> float:
		return (bits / self.one_zebibyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_zebibyte(self) -> int:
		return self._value_zebibytes


class Yobibyte:

	def __init__(self, value_yobibytes: int):
		self._value_yobibytes = value_yobibytes
		self.one_yobibyte_in_bits = 9.671e+24
		self._value_bits = self._convert_into_bits(value_yobibytes)
		self.id = "YiB"

	def _convert_into_bits(self, value_yottabytes: int) -> int:
		return value_yottabytes * self.one_yobibyte_in_bits
	
	def convert_from_bits_to_yobibytes(self, bits: int) -> float:
		return (bits / self.one_yobibyte_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_yobibyte(self) -> int:
		return self._value_yobibytes