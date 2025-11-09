
import wx
# import qrcode
from qrcode.constants import ERROR_CORRECT_M
from PIL import Image

from constants.qr_code import IMAGE_SIZE
from utils.gui import convert_pil_image_to_wx_bitmap
from utils.qr_code import create_qr_code_image

from gui.qr_code_save_button import QRCodeSaveButton
from gui.qr_code_text_ctrl import QRCodeTextCtrl


class QRGeneratorPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.current_pil_image = None  # store the latest PIL image (512x512)

        self.qr_code_text_ctrl = QRCodeTextCtrl(self, on_change=self.on_text_change)

        self.img_ctrl = wx.StaticBitmap(self, bitmap=wx.BitmapBundle.FromBitmap(wx.Bitmap(IMAGE_SIZE, IMAGE_SIZE)))

        self.qr_code_save_button = QRCodeSaveButton(
            parent=self,
            get_image_callable=lambda: self.current_pil_image,
            get_filename_callable=lambda: self.qr_code_text_ctrl.GetValue(),
            image_size=IMAGE_SIZE
        )

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.qr_code_text_ctrl, 0, wx.EXPAND | wx.ALL, 8)
        sizer.Add(self.img_ctrl, 0, wx.CENTER | wx.BOTTOM, 8)
        sizer.Add(self.qr_code_save_button, 0, wx.ALIGN_CENTER | wx.BOTTOM, 8)
        self.SetSizer(sizer)

        self.on_text_change("")

    def _update_display_with_blank(self):
        # white background placeholder
        img = Image.new("RGB", (IMAGE_SIZE, IMAGE_SIZE), "white")
        self.current_pil_image = img
        bmp = convert_pil_image_to_wx_bitmap(img)
        self.img_ctrl.SetBitmap(wx.BitmapBundle.FromBitmap(bmp))
        self.Layout()

    def on_text_change(self, new_text: str) -> None:
        qr_code_image = create_qr_code_image(new_text, IMAGE_SIZE)
        self.current_pil_image = qr_code_image
        bmp = convert_pil_image_to_wx_bitmap(qr_code_image)
        self.img_ctrl.SetBitmap(wx.BitmapBundle.FromBitmap(bmp))
        self.Layout()
