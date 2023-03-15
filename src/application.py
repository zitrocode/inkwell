from pathlib import Path
from prompt_toolkit import Application
from src.editor import Editor, create_editor_layout, create_key_bindings
from src.utils.file_operations import load_file, save_file

def create_application(args):
    file_content = None
    filepath = ""
    if args.file:
        filepath = Path(args.file).resolve()
        if filepath.exists():
            file_content = load_file(filepath)

    editor = Editor(filepath)
    layout, status_control = create_editor_layout(editor, file_content)
    key_bindings = create_key_bindings(editor, save_file, status_control)

    # Create the main application instance for the text editor
    app = Application(
        layout=layout,
        key_bindings=key_bindings,
        full_screen=True
    )
    return app

def run_editor(args):
    app = create_application(args)
    app.run()
