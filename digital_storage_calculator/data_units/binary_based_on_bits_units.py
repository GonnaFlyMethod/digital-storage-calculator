class Kibibit:

	def __init__(self, value_kibibits: int):
		self._value_kibibits = value_kibibits
		self.one_kibibit_in_bits = 2**10
		self._value_bits = self._convert_into_bits(value_kibibits)
		self.id = "Kibit"
	
	def _convert_into_bits(self, value_kibibits: int) -> int:
		return value_kibibits * self.one_kibibit_in_bits
	
	def convert_from_bits_to_kibibits(self, bits: int) -> float:
		return (bits / self.one_kibibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_kibibits(self) -> int:
		return self._value_kibibits


class Mebibit:

	def __init__(self, value_mebibits: int):
		self._value_mebibits = value_mebibits
		self.one_mebibit_in_bits = 2**20
		self._value_bits = self._convert_into_bits(value_mebibits)
		self.id = "Mibit"
	
	def _convert_into_bits(self, value_mebibits: int) -> int:
		return value_mebibits * self.one_mebibit_in_bits
	
	def convert_from_bits_to_mebibits(self, bits: int) -> float:
		return (bits / self.one_mebibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_mebibits(self) -> int:
		return self._value_mebibits


class Gibibit:

	def __init__(self, value_gibibits: int):
		self._value_gibibits = value_gibibits
		self.one_gibibit_in_bits = 2**30
		self._value_bits = self._convert_into_bits(value_gibibits)
		self.id = "Gibit"
	
	def _convert_into_bits(self, value_gibibits: int) -> int:
		return value_gibibits * self.one_gibibit_in_bits
	
	def convert_from_bits_to_gibibits(self, bits: int) -> float:
		return (bits / self.one_gibibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_gibibits(self) -> int:
		return self._value_gibibits
		

class Tebibit:

	def __init__(self, value_tebibits: int):
		self._value_tebibits = value_tebibits
		self.one_tebibit_in_bits = 2**40
		self._value_bits = self._convert_into_bits(value_tebibits)
		self.id = "Tibit"
	
	def _convert_into_bits(self, value_tebibits: int) -> int:
		return value_tebibits * self.one_tebibit_in_bits
	
	def convert_from_bits_to_tebibits(self, bits: int) -> float:
		return (bits / self.one_tebibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_tebibits(self) -> int:
		return self._value_tebibits


class Pebibit:

	def __init__(self, value_pebibits: int):
		self._value_pebibits = value_pebibits
		self.one_pebibit_in_bits = 2**50
		self._value_bits = self._convert_into_bits(value_pebibits)
		self.id = "Pibit"
	
	def _convert_into_bits(self, value_pebibits: int) -> int:
		return value_pebibits * self.one_pebibit_in_bits
	
	def convert_from_bits_to_pebibits(self, bits: int) -> float:
		return (bits / self.one_pebibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_pebibits(self) -> int:
		return self._value_pebibits


class Exbibit:

	def __init__(self, value_exbibits: int):
		self._value_exbibits = value_exbibits
		self.one_exbibit_in_bits = 2**60
		self._value_bits = self._convert_into_bits(value_exbibits)
		self.id = "Eibit"
	
	def _convert_into_bits(self, value_exbibits: int) -> int:
		return value_exbibits * self.one_exbibit_in_bits
	
	def convert_from_bits_to_exbibits(self, bits: int) -> float:
		return (bits / self.one_exbibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_exbibits(self) -> int:
		return self._value_exbibits


class Zebibit:
	
	def __init__(self, value_zebibits: int):
		self._value_zebibits = value_zebibits
		self.one_zebibit_in_bits = 2**70
		self._value_bits = self._convert_into_bits(value_zebibits)
		self.id = "Zibit"
	
	def _convert_into_bits(self, value_zebibits: int) -> int:
		return value_zebibits * self.one_zebibit_in_bits
	
	def convert_from_bits_to_zebibits(self, bits: int) -> float:
		return (bits / self.one_zebibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_zebibits(self) -> int:
		return self._value_zebibits


class Yobibit:
	
	def __init__(self, value_yobibits: int):
		self._value_yobibits = value_yobibits
		self.one_yobibit_in_bits = 2**70
		self._value_bits = self._convert_into_bits(value_yobibits)
		self.id = "Yibit"
	
	def _convert_into_bits(self, value_yobibits: int) -> int:
		return value_yobibits * self.one_yobibit_in_bits

	def convert_from_bits_to_yobibits(self, bits: int) -> float:
		return (bits / self.one_yobibit_in_bits)
	
	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_yobibits(self) -> int:
		return self._value_yobibits
