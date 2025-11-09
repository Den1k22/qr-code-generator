
import wx
from PIL import Image


def convert_pil_image_to_wx_bitmap(pil_img: Image.Image) -> wx.Bitmap:
    """Convert a PIL Image (mode RGB) to wx.Bitmap using FromBuffer.
    Assumes image size matches pil_img.size.
    """
    if pil_img.mode != "RGB":
        pil_img = pil_img.convert("RGB")
    w, h = pil_img.size
    buffer = pil_img.tobytes()

    # Preferred: create a wx.Bitmap directly from the raw buffer
    try:
        return wx.Bitmap.FromBuffer(w, h, buffer)
    except Exception:
        # Fallback: create wx.Image and set its RGB data then convert
        img = wx.Image(w, h)
        img.SetData(buffer)
        return wx.Bitmap(img)
