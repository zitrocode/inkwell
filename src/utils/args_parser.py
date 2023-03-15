import argparse

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description='Inkwell text editor')
    parser.add_argument('file', metavar='file', type=str, nargs='?', help='file to open')
    args = parser.parse_args()
    return args
