
import qrcode
from qrcode.constants import ERROR_CORRECT_M
from PIL import Image


def create_qr_code_image(text: str, size: int) -> Image.Image:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Resize to desired size using a good resampling filter
    qr_img = qr_img.resize((size, size), Image.LANCZOS)

    return qr_img
