
from typing import Callable, Optional
import wx


class QRCodeTextCtrl(wx.TextCtrl):
    def __init__(self, parent, on_change: Optional[Callable[[str], None]] = None):
        super().__init__(parent, style=wx.TE_PROCESS_ENTER)
        self._on_change = on_change

        self.SetHint("Type text here — QR updates on each symbol")

        self.Bind(wx.EVT_TEXT, self.on_text_change)

    def on_text_change(self, event):
        if self._on_change:
            try:
                self._on_change(self.GetValue())
            except Exception as e:
                wx.MessageBox(
                    message=f"An error occurred while updating the QR code:\n{e}",
                    caption="QR Generation Error",
                    style=wx.ICON_ERROR | wx.OK
                )
        event.Skip()
