import sys


# task 2 - thiago guarino
def txt_importer(path_file):
    try:
        if (path_file.endswith('.txt')) is not True:
            raise AssertionError
        with open(path_file, 'r') as file:
            text = file.read().split("\n")
            return text
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except AssertionError:
        print("Formato inválido\n", file=sys.stderr)
