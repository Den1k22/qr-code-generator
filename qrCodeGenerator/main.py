
import wx

from gui.main_frame import MainFrame


class QRCodeGeneratorApp(wx.App):
    def OnInit(self):
        frame = MainFrame()
        frame.Show()
        return True


if __name__ == "__main__":
    app = QRCodeGeneratorApp()
    app.MainLoop()
