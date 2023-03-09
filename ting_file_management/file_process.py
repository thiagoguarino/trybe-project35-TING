from ting_file_management.file_management import txt_importer


# task 3 - thiago guarino
def process(path_file, instance):
    for dict_elem in instance.queue:
        if dict_elem["nome_do_arquivo"] == path_file:
            return None

    text_list = txt_importer(path_file)

    text_data_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_list),
        "linhas_do_arquivo": text_list
    }

    instance.enqueue(text_data_dict)

    print(
        f"'nome_do_arquivo': '{text_data_dict['nome_do_arquivo']}'\n",
        f"'qtd_linhas': {text_data_dict['qtd_linhas']}\n",
        f"'linhas_do_arquivo': {text_data_dict['linhas_do_arquivo']}\n")


# task 4 - thiago guarino
def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    path_file = instance.dequeue()

    print(f"Arquivo {path_file['nome_do_arquivo']} removido com sucesso")


# task 5 - thiago guarino
def file_metadata(instance, position):
    """Aqui irá sua implementação"""
