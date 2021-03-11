from assembler import Assembler
import sys

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        file = open(file_name, 'r')
        file_text = file.readlines()
        file.close()

        assembler = Assembler(file_text)
    except IndexError:
        print("Wrong!!! you have to send an asm file as parameter")
    except FileNotFoundError:
        print("Wrong there is no such file in this directory")

    assembler.translate()
    hack_file = file_name.split('.')[0] + '.hack'

    file = open(hack_file, 'w')
    for instruction in assembler.hack_instructions:
        file.write(instruction + '\n')
    file.close()
    print(f"Successfully assembled {file_name} into {hack_file}")