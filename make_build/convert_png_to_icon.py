from PIL import Image

png_file = "icon.png"
ico_file = "icon.ico"

img = Image.open(png_file)
sizes = [(16, 16), (32, 32), (48, 48), (256, 256)]
img.save(ico_file, format='ICO', sizes=sizes)

print(f"Saved ICO as {ico_file}")
