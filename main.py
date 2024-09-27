from PIL import Image

# Abra o arquivo .webp (caminho)
image = Image.open('C:/Users/nome/Downloads/imagem.webp')

# Salve o arquivo como .jpg
image.convert('RGB').save('C:/Users/nome/Downloads/imagem.jpg', 'JPEG')
