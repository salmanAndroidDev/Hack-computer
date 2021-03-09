from converter import *


class Assembler:
    """
    Assembler program which can translate any given assembly heck language into
    hack machine language
    """

    def __init__(self, file):
        """Assembler constructor"""
        self.symbol_table = {}
        self.file = file
        self.commands = []
        self.hack_instructions = []

    def clean_data(self):
        """remove white space & comments & unnecessary fields"""
        for line in self.file:
            if line.startswith('//') or line.isspace():
                continue
            line = line.replace('\n', '')
            self.commands.append(line)

    def parse(self, command):
        """Unpack each command into it's underlying fields"""
        split_command = command.split('=')
        semi = 1
        dest = None
        if len(split_command) > 1:
            dest = split_command[0]
        else:
            semi = 0
        c_or_j = split_command[semi].split(';')
        comp = c_or_j[0]
        jump = c_or_j[1] if len(c_or_j) > 1 else None
        return comp, dest, jump

    def convert_A_instruction(self, instruction):
        """Convert any decimal number into 16-bit binary number"""
        number = int(instruction)
        binary = bin(number).replace("0b", "")
        return binary.zfill(16)

    def convert_C_instruction(self, instruction):
        """Translate any C instruction"""
        comp, dest, jump = self.parse(instruction)

        return f"111{convert_comp(comp)}{convert_dest(dest)}" \
               f"{convert_jump(jump)}"

    def translate_line_by_line(self):
        """Translates line by line"""
        for command in self.commands:
            if command.startswith('@'):  # is A instruction
                number = command.split('@')[-1]
                instruction = self.convert_A_instruction(number)

            else:  # is C instruction
                instruction = self.convert_C_instruction(command)

            self.hack_instructions.append(instruction)

    def manage_symbol_table(self):
        pass

    def translate(self):
        """Translate the whole file into language machine"""
        self.clean_data()
        self.translate_line_by_line()
