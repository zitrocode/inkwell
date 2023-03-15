from pathlib import Path
from prompt_toolkit import Application
from .editor.layout import create_layout
from .editor.key_bindings import create_key_bindings
from .utils.args_parser import parse_command_line_arguments
from .utils.file_operations import load_file, save_file

def create_application(args):
    file_content = None
    filepath = ""
    if args.file:
        filepath = Path(args.file).resolve()
        if filepath.exists():
            file_content = load_file(filepath)

    layout = create_layout(file_content)
    key_bindings = create_key_bindings(filepath, save_file)

    # Create the main application instance for the text editor.
    app = Application(
        layout=layout,
        key_bindings=key_bindings,
        full_screen=True
    )
    return app

def run_editor(args):
    app = create_application(args)
    app.run()

if __name__ == '__main__':
    args = parse_command_line_arguments()
    run_editor(args)
