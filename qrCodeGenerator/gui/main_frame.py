
import wx

from constants.gui import WINDOW_TITLE
from gui.qr_generator_panel import QRGeneratorPanel


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title=WINDOW_TITLE, size=wx.Size(600, 700))
        QRGeneratorPanel(self)
        self.Centre()
