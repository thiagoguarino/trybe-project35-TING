import sys

from ting_file_management.file_process import process
from ting_file_management.file_process import remove
from ting_file_management.file_process import file_metadata

from ting_file_management.queue import Queue

from ting_word_searches.word_search import exists_word
from ting_word_searches.word_search import search_by_word


queue = Queue()


def add_file():
    user_input = input("Digite o path do Arquivo: ")
    return process(user_input, queue)


def remove_file():
    return remove(queue)


def get_meta_data():
    aaa = int(input("digite a posição que deseja da Fila: "))
    return file_metadata(queue, aaa)


def simple_search():
    user_input = input("Digite a palavra: ")
    return exists_word(user_input, queue)


def complex_search():
    user_input = input("Digite a palavra: ")
    return search_by_word(user_input, queue)


def exit_app():
    return "Encerrando script"


function = {
    "0": add_file,
    "1": remove_file,
    "2": get_meta_data,
    "3": simple_search,
    "4": complex_search,
    "5": exit_app
}

menu_text = """Selecione uma das opções a seguir:
 0 - adicionar um arquivo na Fila;
 1 - remove o primeiro arquivo da Fila;
 2 - busca meta dados do arquivo;
 3 - faz busca Simples por palavra;
 4 - faz busca Complexa por palavra;
 5 - Sair.
 """


def handle_option(chosen_option):
    if chosen_option == "5":
        return True  # Indicates to exit the loop
    elif chosen_option in function:
        function[chosen_option]()
    else:
        sys.stderr.write("Opção inválida\n")
    return False  # Indicates to continue the loop


def menu():
    exit_menu = False
    while not exit_menu:
        try:
            chosen_option = input(menu_text + "OPÇÃO: ")
            exit_menu = handle_option(chosen_option)
        except Exception:
            sys.stderr.write("Opção inválida\n")


if __name__ == "__main__":
    menu()
