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


	def load(self):
		addr = 0
		ram = self.ram

		for instr in ram:
			ram[addr] = instr
			addr += 1
	def HLT_OP(self, op):

		HLT = self.HLT
		if op is HLT:
			self.running = False

	def alu(self, op):
		ADD, MUL, SUB, DIV, MOD = (self.ADD, self.MUL, self.SUB, self.DIV, self.MOD)
		ADD_OP, MUL_OP = (self.ADD_OP, self.MUL_OP)
		SUB_OP, DIV_OP, MOD_OP = (self.SUB_OP, self.DIV_OP, self.MOD_OP)
		pc = self.pc
		if op is ADD:
			ADD_OP(reg_a, reg_b)
			pc += 1
		elif op is MUL:
			MUL_OP(reg_a, reg_b)
			pc += 1
		elif op is SUB:
			SUB_OP(reg_a, reg_b)
			pc += 1
		elif op is DIV:
			DIV_OP(reg_a, reg_b)
			pc += 1
		elif op is MOD:
			MOD_OP(reg_a, reg_b)
			pc += 1
		else:
			raise Exception("Unsupported ALU operation")

	def run(self):
		pc = self.pc
		ram = self.ram
		ram_len = len(self.ram) - 1
		pc = self.pc
		command = ram[pc]
		while True:
			IR = ram[pc]