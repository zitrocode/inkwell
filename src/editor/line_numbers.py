from prompt_toolkit.layout.containers import Window, DynamicContainer
from prompt_toolkit.layout.controls import FormattedTextControl

def create_line_numbers_window(text_buffer, text_window):
    # Create a dynamic container that shows line numbers for the text buffer.
    def get_line_numbers():
        # Generate line numbers based on the text buffer content and the text window's visible lines.
        lines = text_buffer.text.split('\n')
        render_info = text_window.render_info
        if render_info is None:
            first_visible_line = 0
            height = 0
        else:
            first_visible_line = render_info.first_visible_line()
            height = render_info.window_height

        line_numbers = [(f"{i + 1:3d} │") for i, _ in enumerate(lines + [''])][first_visible_line:first_visible_line + height]
        empty_lines = ['~   │'] * (max(0, height - len(line_numbers)))
        formatted_text = '\n'.join(line_numbers + empty_lines)
        return Window(content=FormattedTextControl([('class:line-number', formatted_text)], focusable=False), width=5)

    return DynamicContainer(get_line_numbers)
