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

	def PRN_OP(self):
		pc = self.pc
		reg = self.registers
		read = self.ram_read
		op_a = read[pc + 1]
		print(reg[op_a])
		pc += 2

	def LDI_OP(self):
		pc = self.pc
		reg = self.registers
		read = self.ram_read
		op_a = read(pc + 1)
		op_b = read(pc + 2)
		pc += 3

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

	def ADD_OP(self, reg_a, reg_b):
		pc = self.pc
		reg = self.registers
		reg[reg_a] += reg[reg_b]
		pc += 1

	def MUL_OP(self, reg_a, reg_b):
		pc = self.pc
		reg = self.registers
		reg[reg_a] *= reg[reg_b]
		pc += 1

	def SUB_OP(self, reg_a, reg_b):
		pc = self.pc
		reg = self.registers
		reg[reg_a] -= reg[reg_b]
		pc += 1

	def DIV_OP(self, reg_a, reg_b):
		pc = self.pc
		reg = self.registers
		reg[reg_a] /= reg[reg_b]
		pc += 1


	def alu(self, op, reg_a, reg_b):
		ADD, MUL, SUB, DIV = (self.ADD, self.MUL, self.SUB, self.DIV)
		ADD_OP, MUL_OP = (self.ADD_OP, self.MUL_OP)
		SUB_OP, DIV_OP= (self.SUB_OP, self.DIV_OP)
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
		else:
			raise Exception("Unsupported ALU operation")

	def ram_read(self, addr):
		return self.ram[addr]

	def ram_write(self, addr, value):
		ram = self.ram
		ram[addr] = value

	def trace(self):
		"""
		Handy function to print out the CPU state. You might want to call this
		from run() if you need help debugging.
		"""
		print(f"TRACE: %02X | %02X %02X %02X |" % (
			self.pc,
			# self.fl,
			# self.ie,
			self.ram_read(self.pc),
			self.ram_read(self.pc + 1),
			self.ram_read(self.pc + 2)
		), end='')

		for i in range(8):
			print(" %02X" % self.registers[i], end='')

		print()

	def run(self):
		pc = self.pc
		ram = self.ram
		ram_len = len(self.ram) - 1
		pc = self.pc
		command = ram[pc]
		while True:
			IR = ram[pc]