# task 7 - thiago guarino
def exists_word(word, instance):
    results_list = list()
    for index in range(len(instance)):
        word_count_list = list()
        text_data_dict = instance.search(index)
        for line_index, line in enumerate(text_data_dict["linhas_do_arquivo"]):
            if word.casefold() in line.casefold():
                word_count_list.append({"linha": line_index + 1})
        result_data_dict = {
            "palavra": word,
            "arquivo": text_data_dict["nome_do_arquivo"],
            "ocorrencias": word_count_list
        }
        if len(result_data_dict["ocorrencias"]) > 0:
            results_list.append(result_data_dict)
    return results_list


# task 8 - thiago guarino
def search_by_word(word, instance):
    """Aqui irá sua implementação"""
