def open_and_read(path):
    with open(path, 'r') as file:
        return file.readlines()