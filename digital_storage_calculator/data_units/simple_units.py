class Bit:
	def __init__(self, value_bits: int):
		self._value_bits = value_bits
		self.one_bit_in_bits = 1
		self._value_bits = self._convert_into_bits(value_bits)
		self.id = "bit"
	
	def _convert_into_bits(self, value_bits: int) -> int:
		return value_bits * self.one_bit_in_bits

	def get_val_in_bits(self) -> str:
		return self._value_bits


class Byte:
	def __init__(self, value_bytes: int):
		self._value_bytes = value_bytes
		self.one_byte_in_bits = 8
		self._value_bits = self._convert_into_bits(value_bytes)
		self.id = "B"
	
	def _convert_into_bits(self, value_bytes: int) -> int:
		return value_bytes * self.one_byte_in_bits
	
	def convert_from_bits_to_bytes(self, bits: int) -> float:
		return (bits / self.one_byte_in_bits)

	def get_val_in_bits(self) -> int:
		return self._value_bits
	
	def get_val_in_kilobytes(self) -> int:
		return self._value_bytes
