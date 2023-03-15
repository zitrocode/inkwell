from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.layout.controls import BufferControl
from .line_numbers import create_line_numbers_window

def create_layout(file_content):
    # Create the main layout for the text editor, including the text buffer and line numbers.
    text_buffer = Buffer()
    text_buffer.insert_text(file_content)

    # Create a Window to display the text buffer
    text_window = Window(
        content=BufferControl(buffer=text_buffer),
        width=None,
        wrap_lines=True,
        allow_scroll_beyond_bottom=True
    )

    # Create a Window to display the line numbers
    line_numbers_window = create_line_numbers_window(text_buffer, text_window)

    layout = Layout(
        HSplit([
            VSplit([
                line_numbers_window,
                text_window,
            ])
        ])
    )

    return layout
