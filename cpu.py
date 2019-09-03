import sys

class CPU:
	def __init__(self):
		self.ram = [0] * 256
		self.pc = 0
		self.registers = [0] * 8
