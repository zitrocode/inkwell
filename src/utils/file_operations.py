def load_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read()

def save_file(filename, content):
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(content)
