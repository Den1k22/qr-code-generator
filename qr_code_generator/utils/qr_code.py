
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image
from qrcode.image.pil import PilImage
import os
import sys


_LOGO_CACHE = None

def _load_logo() -> Image.Image | None:
    """Load the logo image once and cache it."""
    global _LOGO_CACHE
    if _LOGO_CACHE is None:
        # For Nuitka builds, use __file__ which is preserved and reliable
        # __file__ points to this actual .py file location even in compiled mode
        try:
            if hasattr(sys, '_MEIPASS'):
                # PyInstaller path
                base_path = sys._MEIPASS
            else:
                # Use __file__ - works in both dev and Nuitka compiled mode
                base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            
            logo_path = os.path.join(base_path, "resources", "favicon-32x32.png")
            
            if os.path.exists(logo_path):
                _LOGO_CACHE = Image.open(logo_path)
        except Exception:
            pass
    return _LOGO_CACHE


_load_logo()


def create_qr_code_image(text: str, size: int, logo_module_size: int = 5) -> Image.Image:
    """
    Create a QR code with a logo in the center.
    
    Args:
        text: The text to encode in the QR code
        size: The final image size in pixels
        logo_module_size: Size of the logo area in QR modules (e.g., 5 means 5x5 modules + 1 module border = 7x7 total cleared area)
    """
    # Use high error correction to ensure QR code works with logo
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    # Clear center area of QR data matrix before image generation
    modules = qr.modules
    module_count = len(modules)
    
    # Add 1-module border around logo area (5x5 becomes 7x7 total)
    total_clear_size = logo_module_size + 2
    center = module_count // 2
    half_size = total_clear_size // 2
    
    for i in range(center - half_size, center + half_size + 1):
        for j in range(center - half_size, center + half_size + 1):
            if 0 <= i < module_count and 0 <= j < module_count:
                modules[i][j] = False
    
    qr_img = qr.make_image(fill_color="black", back_color="white", image_factory=PilImage).convert("RGB")
    qr_img = qr_img.resize((size, size), Image.LANCZOS)

    if _LOGO_CACHE is not None:
        # Calculate logo size: each module = (size / module_count) pixels
        pixels_per_module = size / module_count
        logo_size = int(logo_module_size * pixels_per_module * 0.85)
        logo_resized = _LOGO_CACHE.resize((logo_size, logo_size), Image.LANCZOS)
        logo_pos = ((size - logo_size) // 2, (size - logo_size) // 2)
        qr_img.paste(logo_resized, logo_pos, logo_resized if logo_resized.mode == 'RGBA' else None)

    return qr_img
