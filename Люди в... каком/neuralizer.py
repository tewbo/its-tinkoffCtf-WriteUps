from PIL import Image


def make_pic():
    im = Image.open("clear.png")  # clear image with needed size
    for i in range(256):
        for j in range(256):
            for k in range(256):
                summ = i * (256 ** 2) + j * 256 + k
                x, y = summ % 777, summ // 777
                if y >= 437:
                    break
                im.putpixel((x, y), (i, j, k))
    im.save("mod.png")


def check_pic():
    mapa = dict()
    im = Image.open("saved.png")  # mod.png after encrypting
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = im.getpixel((x, y))
            summ = r * (256 ** 2) + g * 256 + b
            x1, y1 = summ % 777, summ // 777
            mapa[(x, y)] = (x1, y1)
    return mapa


def decrypt_pic():
    decrypt_map = check_pic()
    im = Image.open("flashied.png")
    clear = Image.open("clear.png")
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            clear.putpixel(decrypt_map[(x, y)],
                           im.getpixel((x, y)))
    clear.save("flag.png")


if __name__ == "__main__":
    # make_pic()
    decrypt_pic()
