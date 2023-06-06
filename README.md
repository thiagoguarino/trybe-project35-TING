## Trybe Project 35 - T.I.N.G - TRYBE IS NOT GOOGLE


## PROJECT OVERVIEW

  This is project #5 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project you must implement a program that simulates a document indexing algorithm similar to Google's. Your program must be able to identify occurrences of terms in TXT files. The program developed by you should have two modules:

  - File management module that allows you to attach text files (TXT format);
  - Search module that allows operating search functions on attached files;

  Stack: Python3, Pytest.

  **In this project we will not focus on the analysis of meanings or search for synonyms**

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>


## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

  *Description* | *Status*
  --- | :---:
  1.1 - the `enqueue` method must add a value to the queue, modifying its size | :heavy_check_mark:
  1.2 - the `dequeue` method should remove the oldest element in the queue, modifying its size | :heavy_check_mark:
  1.3 - the `search` method must search for a value in the List using indexes | :heavy_check_mark:
  1.4 - the `search` method should raise an exception when the index is invalid | :heavy_check_mark:
  2.1 - when executing the `txt_importer` method it should return a structure containing the lines of the file | :heavy_check_mark:
  2.2 - when executing the `txt_importer` method with a TXT file that does not exist, the message should be displayed: `Arquivo {path_file} não encontrado` | :heavy_check_mark:
  2.3 - when executing the `txt_importer` method with an extension other than `.txt`, a message should be displayed: `Formato Inválido` | :heavy_check_mark:
  3.1 - when executing the `process` function with a file that already exists in the queue, the execution must ignore it | :heavy_check_mark:
  3.2 - when executing the function `process` successfully it should return message via `stdout` | :heavy_check_mark:
  4.1 - when executing the `remove` function successfully, it should return a message via `stdout` | :heavy_check_mark:
  4.2 - when executing the `remove` function a non-existent file should return the message `Não há elementos` | :heavy_check_mark:
  5.1 - when successfully executing the `file_metadata` function it should return a message via `stdout` | :heavy_check_mark:
  5.2 - when executing the `file_metadata` function with an invalid position, it should return the message `posição Inválida` | :heavy_check_mark:
  6 - Implement the tests for the `PriorityQueue` class capable of storing small files as a priority | :heavy_check_mark:
  7.1 - when executing the `exists_word` function successfully should return the correct structure | :heavy_check_mark:
  7.2 - when executing the `exists_word` function with nonexistent word, it should return an empty List | :heavy_check_mark:
  8.1 - when executing the `search_by_word` function successfully it should return the correct structure | :heavy_check_mark:
  8.2 - when executing the `search_by_word` function with a nonexistent word, it should return an empty List | :heavy_check_mark:

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
