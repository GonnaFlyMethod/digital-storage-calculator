class Kilobit:

	def __init__(self, value_kilobits: int):
		self._value_kilobits = value_kilobits
		self.one_kilobit_in_bits = 10**3
		self._value_bits = self._convert_into_bits(value_kilobits)
		self.id = "kbit"
	
	def _convert_into_bits(self, value_kibibits: int) -> int:
		return value_kibibits * self.one_kilobit_in_bits
	
	def convert_from_bits_to_kilobits(self, bits: int) -> float:
		return (bits / self.one_kilobit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_kilobits(self) -> int:
		return self._value_kilobits


class Megabit:

	def __init__(self, value_megabits: int):
		self._value_megabits = value_megabits
		self.one_megabit_in_bits = 10**6
		self._value_bits = self._convert_into_bits(value_megabits)
		self.id = "Mbit"
	
	def _convert_into_bits(self, value_megabits: int) -> int:
		return value_megabits * self.one_megabit_in_bits
	
	def convert_from_bits_to_megabits(self, bits: int) -> float:
		return (bits / self.one_megabit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_megabits(self) -> int:
		return self._value_megabits


class Gigabit:

	def __init__(self, value_gigabits: int):
		self._value_gigabits = value_gigabits
		self.one_gigabit_in_bits = 10**9
		self._value_bits = self._convert_into_bits(value_gigabits)
		self.id = "Gbit"
	
	def _convert_into_bits(self, value_gigabits: int) -> int:
		return value_gigabits * self.one_gigabit_in_bits
	
	def convert_from_bits_to_gigabits(self, bits: int) -> float:
		return (bits / self.one_gigabit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_gigabits(self) -> int:
		return self._value_gigabits
		

class Terabit:

	def __init__(self, value_terabits: int):
		self._value_terabits = value_terabits
		self.one_terabit_in_bits = 10**12
		self._value_bits = self._convert_into_bits(value_terabits)
		self.id = "Tbit"
	
	def _convert_into_bits(self, value_terabits: int) -> int:
		return value_terabits * self.one_terabit_in_bits
	
	def convert_from_bits_to_terabits(self, bits: int) -> float:
		return (bits / self.one_terabit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits

	def get_val_in_terabits(self) -> int:
		return self._value_terabits


class Petabit:

	def __init__(self, value_petabits: int):
		self._value_petabits = value_petabits
		self.one_petabit_in_bits = 10**15
		self._value_bits = self._convert_into_bits(value_petabits)
		self.id = "Pbit"
	
	def _convert_into_bits(self, value_petabits: int) -> int:
		return value_petabits * self.one_petabit_in_bits
	
	def convert_from_bits_to_petabits(self, bits: int) -> float:
		return (bits / self.one_petabit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits

	def get_val_in_petabits(self) -> int:
		return self._value_petabits


class Exabit:

	def __init__(self, value_exabits: int):
		self._value_exabits = value_exabits
		self.one_exabit_in_bits = 10**18
		self._value_bits = self._convert_into_bits(value_exabits)
		self.id = "Ebit"

	def _convert_into_bits(self, value_exabits: int) -> int:
		return value_exabits * self.one_exabit_in_bits
	
	def convert_from_bits_to_exabits(self, bits: int) -> float:
		return (bits / self.one_exabit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_exabits(self) -> int:
		return self._value_exabits


class Zettabit:

	def __init__(self, value_zettabits: int):
		self._value_zettabits = value_zettabits
		self.one_zettabit_in_bits = 10**21
		self._value_bits = self._convert_into_bits(value_zettabits)
		self.id = "Zbit"

	def _convert_into_bits(self, value_zettabits: int) -> int:
		return value_zettabits * self.one_zettabit_in_bits
	
	def convert_from_bits_to_zettabits(self, bits: int) -> float:
		return (bits / self.one_zettabit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_zettabits(self) -> int:
		return self._value_zettabits


class Yottabit:
	
	def __init__(self, value_yottabits: int):
		self._value_yottabits = value_yottabits
		self.one_yottabit_in_bits = 10**24
		self._value_bits = self._convert_into_bits(value_yottabits)
		self.id = "Ybit"
	
	def _convert_into_bits(self, value_yottabits: int) -> int:
		return value_yottabits * self.one_yottabit_in_bits

	def convert_from_bits_to_yottabits(self, bits: int) -> float:
		return (bits / self.one_yottabit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_yottabits(self) -> int:
		return self._value_yottabits
