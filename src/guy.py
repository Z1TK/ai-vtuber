import tkinter as tk


class AssistanGui:
    def __init__(self, root):
        self.root = root

    def setup(
        self,
        title: str,
        width: str,
        height: str,
        bg_color: str,
        borderless: bool = False,
        on_top: bool = False,
    ):
        self.root.title(title)
        self.root.geometry(width + 'x' + height)
        self.root.overrideredirect(borderless)
        self.root.configure(bg=bg_color)
        self.root.wm_attributes("-topmost", on_top)
