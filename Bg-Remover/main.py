from rembg import remove
from PIL import Image
img = Image.open("F:\\Projects\\Python\\Bg-Remover\\Images\\parrot.jpg")
R = remove(img)
R.save("parrot1.png")