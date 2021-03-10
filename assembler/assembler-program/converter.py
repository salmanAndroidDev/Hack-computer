def convert_comp(code):
    """Convert any give compare code into it's corresponding binary code"""
    binary = '000000'
    if code is None:
        return binary
    elif code == '0':
        binary = '101010'
    elif code == '1':
        binary = '111111'
    elif code == '-1':
        binary = '111010'
    elif code == 'D':
        binary = '001100'
    elif code == 'A' or code == 'M':
        binary = '110000'
    elif code == '!D':
        binary = '001101'
    elif code == '!A' or code == '!M':
        binary = '110001'
    elif code == '-D':
        binary = '001111'
    elif code == '-A' or code == '-M':
        binary = '110011'
    elif code == 'D+1':
        binary = '011111'
    elif code == 'A+1' or code == 'M+1':
        binary = '110111'
    elif code == 'D-1':
        binary = '001110'
    elif code == 'A-1' or code == 'M-1':
        binary = '110010'
    elif code == 'D+A' or code == 'D+M':
        binary = '000010'
    elif code == 'D-A' or code == 'D-M':
        binary = '010011'
    elif code == 'A-D' or code == 'M-D':
        binary = '000111'
    elif code == 'D&A' or code == 'D&M':
        binary = '000000'
    elif code == 'D|A' or code == 'D|M':
        binary = '010101'
    else:
        binary = None

    if binary is None:
        raise ValueError(f'Syntax Error {code} is wrong compare code!')

    if code.count('M') > 0:
        binary = '1' + binary
    else:
        binary = '0' + binary
    return binary


def convert_dest(code):
    """Convert any give destination code into it's corresponding binary code"""
    binary = '000'
    if code is None:
        return binary
    elif code == 'M':
        binary = '001'
    elif code == 'D':
        binary = '010'
    elif code == 'MD':
        binary = '011'
    elif code == 'A':
        binary = '100'
    elif code == 'AM':
        binary = '101'
    elif code == 'AD':
        binary = '110'
    elif code == 'AMD':
        binary = '111'
    else:
        raise ValueError(f"Syntax error, {code} is wrong destination code!")
    return binary


def convert_jump(code):
    """Convert any give jump code into it's corresponding binary code"""
    binary = '000'
    if code is None:
        return binary
    elif code == 'JGT':
        binary = '001'
    elif code == 'JEQ':
        binary = '010'
    elif code == 'JGE':
        binary = '011'
    elif code == 'JLT':
        binary = '100'
    elif code == 'JNE':
        binary = '101'
    elif code == 'JLE':
        binary = '110'
    elif code == 'JMP':
        binary = '111'
    else:
        raise ValueError(f"Syntax error, {code} is wrong Jump code!")
    return binary


def initialize_symbol_table():
    """Returns a symbol table with all it's necessary symbols"""
    return {
        "R0": '0',
        "R1": '1',
        "R2": '2',
        "R3": '3',
        "R4": '4',
        "R5": '5',
        "R6": '6',
        "R7": '7',
        "R8": '8',
        "R9": '9',
        "R10": '10',
        "R11": '11',
        "R12": '12',
        "R13": '13',
        "R14": '14',
        "R15": '15',
        'SCREEN': '16384',
        'KBD': '24576',
        'SP': '0',
        'LCL': '1',
        'ARG': '2',
        'THIS': '3',
        'THAT': '4',
    }
