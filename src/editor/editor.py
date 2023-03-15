from .modes import EditorMode

class Editor:
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.mode = EditorMode.NORMAL
