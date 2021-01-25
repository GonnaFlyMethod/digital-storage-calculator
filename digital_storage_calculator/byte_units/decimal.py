class Megabyte:

	def __init__(self, value_megabytes: int):
		self._value_megabytes = value_megabytes
		self.one_megabyte_in_bytes = (1000 ** 2)
		self._value_bytes = self._convert_into_bytes(value_megabytes)
		self.id = "MB"
	
	def _convert_into_bytes(self, value_megabytes: int) -> int:
		return value_megabytes * self.one_megabyte_in_bytes
	
	def convert_from_bytes_to_megabytes(self, bytes: int) -> float:
		return (bytes / self.one_megabyte_in_bytes)
	
	def get_val_in_bytes(self) -> int:
		return self._value_bytes
	
	def get_val_in_megabytes(self) -> int:
		return self._value_megabytes
	

class Gigabyte:

	def __init__(self, value_gigabytes: int):
		self._value_gigabytes = value_gigabytes
		self.one_gigabyte_in_bytes = (1000 ** 3)
		self._value_bytes = self._convert_into_bytes(value_gigabytes)
		self.id = "GB"
	
	def _convert_into_bytes(self, value_gigabytes: int) -> int:
		return value_gigabytes * self.one_gigabyte_in_bytes
	
	def convert_from_bytes_to_gigabytes(self, bytes: int) -> float:
		return (bytes / self.one_gigabyte_in_bytes)

	def get_val_in_bytes(self) -> int:
		return self._value_bytes
	
	def get_val_in_gigabytes(self) -> int:
		return self._value_gigabytes


class Terabyte:

	def __init__(self, value_terabytes: int):
		self._value_terabytes = value_terabytes
		self.one_terabyte_in_bytes = (1000 ** 4)
		self._value_bytes = self._convert_into_bytes(value_terabytes)
		self.id = "TB"
	
	def _convert_into_bytes(self, value_terabytes: int) -> int:
		return value_terabytes * self.one_terabyte_in_bytes
	
	def convert_from_bytes_to_terabytes(self, bytes: int) -> float:
		return (bytes / self.one_terabyte_in_bytes)

	def get_val_in_bytes(self) -> int:
		return self._value_bytes
	
	def get_val_in_terabytes(self) -> int:
		return self._value_terabytes

		
class Petabyte:
	
	def __init__(self, value_petabytes: int):
		self._value_petabytes = value_petabytes
		self.one_petabyte_in_bytes = (1000 ** 5)
		self._value_bytes = self._convert_into_bytes(value_petabytes)
		self.id = "PB"
	
	def _convert_into_bytes(self, value_petabytes: int) -> int:
		return value_petabytes * self.one_petabyte_in_bytes
	
	def convert_from_bytes_to_petabytes(self, bytes: int) -> float:
		return (bytes / self.one_petabyte_in_bytes)

	def get_val_in_bytes(self) -> int:
		return self._value_bytes
	
	def get_val_in_petabytes(self) -> int:
		return self._value_petabytes

		
class Exabyte:

	def __init__(self, value_exabytes: int):
		self._value_exabytes = value_exabytes
		self.one_exabyte_in_bytes = (1000 ** 6)
		self._value_bytes = self._convert_into_bytes(value_exabytes)
		self.id = "EB"
	
	def _convert_into_bytes(self, value_exabytes: int) -> int:
		return value_exabytes * self.one_exabyte_in_bytes
	
	def convert_from_bytes_to_exabytes(self, bytes: int) -> float:
		return (bytes / self.one_exabyte_in_bytes)

	def get_val_in_bytes(self) -> int:
		return self._value_bytes
	
	def get_val_in_exabytes(self) -> int:
		return self._value_exabytes


class Zettabyte:

	def __init__(self, value_zettabytes: int):
		self._value_zettabytes = value_zettabytes
		self.one_zettabyte_in_bytes = (1000 ** 7)
		self._value_bytes = self._convert_into_bytes(value_zettabytes)
		self.id = "ZB"
	
	def _convert_into_bytes(self, value_zettabytes: int) -> int:
		return value_zettabytes * self.one_zettabyte_in_bytes
	
	def convert_from_bytes_to_zettabytes(self, bytes: int) -> float:
		return (bytes / self.one_zettabyte_in_bytes)

	def get_val_in_bytes(self) -> int:
		return self._value_bytes
	
	def get_val_in_zettabyte(self) -> int:
		return self._value_zettabytes


class Yottabyte:

	def __init__(self, value_yottabytes: int):
		self._value_yottabytes = value_yottabytes
		self.one_yottabyte_in_bytes = (1000 ** 8)
		self._value_bytes = self._convert_into_bytes(value_yottabytes)
		self.id = "YB"

	def _convert_into_bytes(self, value_yottabytes: int) -> int:
		return value_yottabytes * self.one_yottabyte_in_bytes
	
	def convert_from_bytes_to_yottabytes(self, bytes: int) -> float:
		return (bytes / self.one_yottabyte_in_bytes)
	
	def get_val_in_bytes(self) -> int:
		return self._value_bytes
	
	def get_val_in_yottabyte(self) -> int:
		return self._value_yottabytes
