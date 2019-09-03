import sys

class CPU:
	def __init__(self):
		self.ram = [0] * 256
		self.pc = 0
		self.registers = [0] * 8
		self.PRN = 0b01000111
		self.ADD = 0b10100000
		self.SUB = 0b10100001
		self.MUL = 0b10100010
		self.LDI = 0b10000010
		self.HLT = 0b00000001
		self.DIV = 0b10100011
		self.MOD = 0b10100100
		self.running = True
