from prompt_toolkit.key_binding import KeyBindings

def create_key_bindings(filepath, save_file):
    # Create key binding for the text editor.
    key_bindings = KeyBindings()

    @key_bindings.add('c-q')
    def exit(event):
        # Exit the application when `CTRL+Q` is pressend
        event.app.exit()

    @key_bindings.add('c-s')
    def save(event):
        buffer = event.app.current_buffer
        if filepath:
            save_file(filepath, buffer.text)
        else:
            event.app.exit(exception=RuntimeError('No file specified'))

    return key_bindings
