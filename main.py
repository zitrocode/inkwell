from src.application import run_editor
from src.utils.args_parser import parse_command_line_arguments

if __name__ == '__main__':
    args = parse_command_line_arguments()
    run_editor(args)
