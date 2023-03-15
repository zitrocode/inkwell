from prompt_toolkit.buffer import Buffer
from prompt_toolkit.filters import Condition
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.layout.controls import BufferControl
from .modes import EditorMode
from .line_numbers import create_line_numbers_window
from .status import create_status_window

def create_editor_layout(editor, file_content):
    # Create the main layout for the text editor, including the text buffer and line numbers.
    text_buffer = Buffer(read_only=Condition(lambda: editor.mode == EditorMode.NORMAL))
    original_mode = editor.mode
    editor.mode = EditorMode.INSERT
    if file_content:
        text_buffer.insert_text(file_content)
    editor.mode = original_mode

    # Create a Window to display the text buffer
    text_window = Window(
        content=BufferControl(buffer=text_buffer),
        width=None,
        wrap_lines=True,
        allow_scroll_beyond_bottom=True
    )

     # Create a Window to display the line numbers
    line_numbers_window = create_line_numbers_window(text_buffer, text_window)

    status_control, status_window = create_status_window()

    layout = Layout(
        HSplit([
            VSplit([
                line_numbers_window,
                text_window,
            ]),
            status_window,
        ])
    )

    return layout, status_control

