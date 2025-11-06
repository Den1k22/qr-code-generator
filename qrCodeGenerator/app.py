
import wx

from qrCodeGenerator.gui.main_frame import MainFrame


class QRCodeGeneratorApp(wx.App):
    def OnInit(self):
        frame = MainFrame()
        frame.Show()
        return True
