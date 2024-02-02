FILE_PATH = 'todos.txt'


def get_todos(filepath=FILE_PATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_write, filepath=FILE_PATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_write)
