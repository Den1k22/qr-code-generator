
import wx
from PIL import Image


class QRCodeSaveButton(wx.Button):
    def __init__(self, parent, get_image_callable, get_filename_callable, image_size):
        """
        A reusable Save-as-PNG button.

        :param parent: wx parent window
        :param get_image_callable: function that returns the current PIL.Image
        :param get_filename_callable: function that returns the default file name (string)
        :param image_size: target image size in pixels
        """
        super().__init__(parent, label="Save as PNG")
        self.get_image = get_image_callable
        self.get_filename = get_filename_callable
        self.image_size = image_size

        self.Bind(wx.EVT_BUTTON, self.on_save)

    def on_save(self, event):
        image = self.get_image()
        if image is None:
            wx.MessageBox("No QR image to save.", "Error", wx.ICON_ERROR)
            return

        text_value = self.get_filename().strip() or "qr_code"
        invalid_chars = '<>:"/\\|?*'
        for ch in invalid_chars:
            text_value = text_value.replace(ch, "_")

        default_name = f"{text_value}.png"

        with wx.FileDialog(
            self,
            message="Save QR code as...",
            defaultFile=default_name,
            wildcard="PNG files (*.png)|*.png",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        ) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return

            path = dlg.GetPath()
            if not path.lower().endswith(".png"):
                path += ".png"

            try:
                img_to_save = image
                if img_to_save.size != (self.image_size, self.image_size):
                    img_to_save = img_to_save.resize((self.image_size, self.image_size), Image.LANCZOS)
                img_to_save.save(path, format="PNG")
                wx.MessageBox(f"Saved: {path}", "Saved", wx.ICON_INFORMATION)
            except Exception as e:
                wx.MessageBox(f"Failed to save image:\\n{e}", "Error", wx.ICON_ERROR)
