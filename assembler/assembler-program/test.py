from unittest import TestCase
from assembler import Assembler


def prepare_test(test_file):
    instructions = []
    for line in test_file:
        instruction = line.split('	')[1]
        instruction = instruction.replace('\n', '')
        instructions.append(instruction)
    return instructions


ASSEMBLY_FILES_DIRECTORY = 'assembly-files/'
ASSEMBLY_TEST_FILES_DIRECTORY = 'assembly-test-files/'


class UnitTest(TestCase):
    def setUp(self):
        file = open(ASSEMBLY_FILES_DIRECTORY+'Rect.asm', 'r')  # Select assembly file
        text_file = file.readlines()
        file.close()
        file = open(ASSEMBLY_TEST_FILES_DIRECTORY + 'test_Rect.txt', 'r')  # Select binary test file
        test_file = file.readlines()
        file.close()

        self.assembler = Assembler(text_file)
        self.instructions = prepare_test(test_file)

    def test_clean_data(self):
        """Test that clean data works as expected"""
        self.assembler.clean_data()
        commands = self.assembler.commands
        for command in commands:
            is_bad = command.isspace() or '//' in command \
                     or '/*' in command or '*/' in command
            self.assertFalse(is_bad)
        self.assembler.clean_symbols()

    def test_clean_symbols(self):
        """
        Test that symbols are cleaned successfully by comparison with corresponding
        no-symbol files
        """
        self.assembler.clean_data()
        self.assembler.clean_symbols()

        file = open(ASSEMBLY_FILES_DIRECTORY + 'RectL.asm', 'r')
        text_file = file.readlines()
        file.close()

        new_assembler = Assembler(text_file)
        new_assembler.clean_data()

        for i in range(len(new_assembler.commands)):
            commandL = new_assembler.commands[i]
            command = self.assembler.commands[i]
            self.assertEqual(commandL, command)

    def test_parse(self):
        """Test that c instruction is parsed successfully"""
        c_instruction = {'D=A': ('A', 'D', None),
                         'D=D+A': ('D+A', 'D', None),
                         'D;JGT': ('D', None, 'JGT'),
                         '0;JMP': ('0', None, 'JMP')}

        for key in c_instruction.keys():
            comp, dest, jump = self.assembler.parse(key)
            t_comp, t_dest, t_jump = c_instruction[key]
            self.assertEqual(comp, t_comp)
            self.assertEqual(dest, t_dest)
            self.assertEqual(jump, t_jump)

    def test_convert_C_instruction(self):
        """Test that C instruction is converted to it's corresponding binary code"""
        self.assembler.clean_data()
        self.assembler.clean_symbols()
        for i in range(len(self.assembler.commands)):
            instruction = self.assembler.commands[i]
            if instruction.startswith('@'):  # A instruction
                continue
            else:  # C instruction
                binary_c = self.assembler.convert_C_instruction(instruction)
                self.assertEqual(self.instructions[i], binary_c)

    def test_translate(self):
        """Test that translation was done successfully"""
        self.assembler.translate()

        self.assertEqual(len(self.instructions),
                         len(self.assembler.hack_instructions))

        for i in range(len(self.instructions)):
            self.assertEqual(self.instructions[i],
                             self.assembler.hack_instructions[i])
