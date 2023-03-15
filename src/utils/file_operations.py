def load_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
