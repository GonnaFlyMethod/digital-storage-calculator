class Kilobyte:
	def __init__(self, value_kilobytes: int):
		self._value_kilobytes = value_kilobytes
		self.one_kilobyte_in_bits = 8000
		self._value_bits = self._convert_into_bits(value_kilobytes)
		self.id = "KB"
	
	def _convert_into_bits(self, value_kilobytes: int) -> int:
		return value_kilobytes * self.one_kilobyte_in_bits
	
	def convert_from_bits_to_kilobytes(self, bits: int) -> float:
		return (bits / self.one_kilobyte_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_kilobytes(self) -> int:
		return self._value_kilobytes


class Megabyte:

	def __init__(self, value_megabytes: int):
		self._value_megabytes = value_megabytes
		self.one_megabyte_in_bits = 8e+6
		self._value_bits = self._convert_into_bits(value_megabytes)
		self.id = "MB"
	
	def _convert_into_bits(self, value_megabytes: int) -> int:
		return value_megabytes * self.one_megabyte_in_bits
	
	def convert_from_bits_to_megabytes(self, bits: int) -> float:
		return (bits / self.one_megabyte_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_megabytes(self) -> int:
		return self._value_megabytes
	

class Gigabyte:

	def __init__(self, value_gigabytes: int):
		self._value_gigabytes = value_gigabytes
		self.one_gigabyte_in_bits = 8e+9
		self._value_bits = self._convert_into_bits(value_gigabytes)
		self.id = "GB"
	
	def _convert_into_bits(self, value_gigabytes: int) -> int:
		return value_gigabytes * self.one_gigabyte_in_bits
	
	def convert_from_bits_to_gigabytes(self, bits: int) -> float:
		return (bits / self.one_gigabyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_gigabytes(self) -> int:
		return self._value_gigabytes


class Terabyte:

	def __init__(self, value_terabytes: int):
		self._value_terabytes = value_terabytes
		self.one_terabyte_in_bits = 8e+12
		self._value_bits = self._convert_into_bits(value_terabytes)
		self.id = "TB"
	
	def _convert_into_bits(self, value_terabytes: int) -> int:
		return value_terabytes * self.one_terabyte_in_bits
	
	def convert_from_bits_to_terabytes(self, bits: int) -> float:
		return (bits / self.one_terabyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_terabytes(self) -> int:
		return self._value_terabytes

		
class Petabyte:
	
	def __init__(self, value_petabytes: int):
		self._value_petabytes = value_petabytes
		self.one_petabyte_in_bits = 8e+15
		self._value_bits = self._convert_into_bits(value_petabytes)
		self.id = "PB"
	
	def _convert_into_bits(self, value_petabytes: int) -> int:
		return value_petabytes * self.one_petabyte_in_bits
	
	def convert_from_bits_to_petabytes(self, bits: int) -> float:
		return (bits / self.one_petabyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bytes
	
	def get_val_in_petabytes(self) -> int:
		return self._value_petabytes

		
class Exabyte:

	def __init__(self, value_exabytes: int):
		self._value_exabytes = value_exabytes
		self.one_exabyte_in_bits = 8e+18
		self._value_bits = self._convert_into_bits(value_exabytes)
		self.id = "EB"
	
	def _convert_into_bits(self, value_exabytes: int) -> int:
		return value_exabytes * self.one_exabyte_in_bits
	
	def convert_from_bits_to_exabytes(self, bits: int) -> float:
		return (bits / self.one_exabyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_exabytes(self) -> int:
		return self._value_exabytes


class Zettabyte:

	def __init__(self, value_zettabytes: int):
		self._value_zettabytes = value_zettabytes
		self.one_zettabyte_in_bits = 8e+21
		self._value_bits = self._convert_into_bits(value_zettabytes)
		self.id = "ZB"
	
	def _convert_into_bits(self, value_zettabytes: int) -> int:
		return value_zettabytes * self.one_zettabyte_in_bits
	
	def convert_from_bits_to_zettabytes(self, bits: int) -> float:
		return (bits / self.one_zettabyte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_zettabyte(self) -> int:
		return self._value_zettabytes


class Yottabyte:

	def __init__(self, value_yottabytes: int):
		self._value_yottabytes = value_yottabytes
		self.one_yottabyte_in_bits = 8e+24
		self._value_bits = self._convert_into_bits(value_yottabytes)
		self.id = "YB"

	def _convert_into_bits(self, value_yottabytes: int) -> int:
		return value_yottabytes * self.one_yottabyte_in_bits
	
	def convert_from_bits_to_yottabytes(self, bits: int) -> float:
		return (bits / self.one_yottabyte_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_yottabyte(self) -> int:
		return self._value_yottabytes
