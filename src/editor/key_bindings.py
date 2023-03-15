from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import Condition
from .modes import EditorMode

def create_key_bindings(editor, save_file, status_control):
    key_bindings = KeyBindings()
    # Create key binding for the text editor
    @key_bindings.add('c-q')
    def exit(event):
        event.app.exit()
    # Exit the application when `CTRL+Q` is pressend
    @key_bindings.add('c-s')
    def save(event):
        buffer = event.app.current_buffer
        if editor.filepath:
            save_file(editor.filepath, buffer.text)
            status_control.text = [("class:status", "File saved")]
        else:
            event.app.exit(exception=RuntimeError('No file specified'))

    @key_bindings.add('i', filter=Condition(lambda: editor.mode == EditorMode.NORMAL))
    def enter_insert_mode(event):
        editor.mode = EditorMode.INSERT
        status_control.text = [("class:status", "INSERT mode")]

    @key_bindings.add('escape', filter=Condition(lambda: editor.mode == EditorMode.INSERT))
    def exit_insert_mode(event):
        editor.mode = EditorMode.NORMAL
        status_control.text = [("class:status", "NORMAL mode")]

    return key_bindings
