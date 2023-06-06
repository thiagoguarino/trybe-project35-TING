## Trybe Project 35 - T.I.N.G - TRYBE IS NOT GOOGLE


## PROJECT OVERVIEW

  This is project #5 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project is Neste projeto você deverá implementar um programa que simule um algoritmo de indexação de documentos similar ao do Google. Seu programa deverá ser capaz de identificar ocorrências de termos em arquivos TXT.

Para isso, o programa desenvolvido por você deverá ter dois módulos:

Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT) e;
Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.
Neste projeto não iremos focar na análise de significados ou busca por sinônimos. 
  
  Stack: Python3, Pytest.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>


## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

    *Description* | *Status*
    --- | :---:
    1.1 - Será validado que o método `enqueue` deve adicionar um valor a fila, modificando seu tamanho | :heavy_check_mark:
    1.2 - Será validado que o método `dequeue` deve remover o elemento a mais tempo na fila, modificando seu tamanho | :heavy_check_mark:
    1.3 - Será validado que o método `search` deve buscar um valor na lista à partir de um índice | :heavy_check_mark:
    1.4 - Será validado que o método `search` deve lançar uma exceção quando o índice for inválido | :heavy_check_mark:
    2.1 - Será validado que ao executar o método `txt_importer` deve retornar uma estrutura contendo as linhas do arquivo | :heavy_check_mark:
    2.2 - Será validado que ao executar o método `txt_importer` com um arquivo TXT que não exista, deve ser exibida a mensagem: `Arquivo {path_file} não encontrado` | :heavy_check_mark:
    2.3 - Será validado que ao executar o método `txt_importer` com uma extensão diferente de `.txt`, deve ser exibida uma mensagem: `Formato inválido` | :heavy_check_mark:
    3.1 - Será validado que ao executar a função `process` com o mesmo nome a execução deverá ser ignorada | :heavy_check_mark:
    3.2 - Será validado que ao executar a função `process` com sucesso deverá retornar mensagem via `stdout` | :heavy_check_mark:
    4.1 - Será validado que ao executar a função `remove` com sucesso deverá retornar mensagem via `stdout` | :heavy_check_mark:
    4.2 - Será validado que ao executar a função `remove` um arquivo inexistente deverá retornar a mensagem `Não há elementos` | :heavy_check_mark:
    5.1 - Será validado que ao executar a função `file_metadata` com sucesso deverá retornar mensagem via `stdout` | :heavy_check_mark:
    5.2 - Será validado que ao executar a função `file_metadata` com posição inválida deverá retornar a mensagem `Posição inválida` | :heavy_check_mark:
    6 - Implemente os testes para a classe `PriorityQueue` capaz de armazenar arquivos pequenos de forma prioritária | :heavy_check_mark:
    7.1 - Será validado que ao executar a função `exists_word` com sucesso deverá retornar a mensagem | :heavy_check_mark:
    7.2 - Será validado que ao executar a função `exists_word` com palavra inexistente deverá retornar uma lista vazia | :heavy_check_mark:
    8.1 - Será validado que ao executar a função `search_by_word` com sucesso deverá retornar a mensagem | :heavy_check_mark:
    8.2 - Será validado que ao executar a função `search_by_word` com palavra inexistente deverá retornar uma lista vazia | :heavy_check_mark:

</details>

<details>
  <summary><strong>How to Execute the Tests</strong></summary>

  To execute the tests, first check if you have the virtual environment up and running.

  <strong>To Execute All tests:</strong> ```$ python3 -m pytest```

  the file `pyproject.toml` already correctly configures pytest. However, in case you have issues with that and want a complete explicit output, the command is:

  ```bash
  python3 -m pytest -s -vv
  ```

  In case you need to execute just one test file, use the command:

  ```bash
  python3 -m pytest tests/filename.py
  ```

  In case you need to execute just one test function, use the command:

  ```bash
  python3 -m pytest -k test_function_name
  ```

  If you wish that the tests stop from being executed when the first error happens, use the param `-x`

  ```bash
  python3 -m pytest -x tests/filename.py
  ```

  To execute a specific test of a file, type the command:

  ```bash
  python3 -m pytest tests/filename.py::test_function_name
  ```
</details>


## HOW TO RUN THE APP


1. clone the repository

  - `git clone git@github.com:thiagoguarino/trybe-project35-TING.git`

2. enter the project's folder 

  - `cd trybe-project35-TING`

3. create and open the project's virtual environment

- `python3 -m venv .venv && source .venv/bin/activate`

4. install dependencies

- `python3 -m pip install -r dev-requirements.txt`

5. test the functions manually on each file.

    a - the files: file_management.py, file_process.py, word_search.py 

    b - set the params: `a = txt_importer('statics/nome_pedro.txt')`, then print it: `print(a)`

    c - instance a new queue - `project = Queue()`, call `process("statics/arquivo_teste.txt", project)`

    d - declare in a variable `word1 = exists_word("pedro", project)`, `word2 = search_by_word("pedro", project)`

    e - print them - `print(word1)` and `print(word2)`

6. how to execute the functions on: 
    a - `python3 ting_file_management/file_management.py` and `python3 ting_file_management/file_process.py`

    b - `python3 word_searches/word_search.py`
