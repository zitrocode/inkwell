from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl

def create_status_window():
    status_label = FormattedTextControl([("class:status", "NORMAL mode")], focusable=False)
    status_window = Window(content=status_label, height=1)
    return status_label, status_window
