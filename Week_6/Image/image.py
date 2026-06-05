from PIL import Image, ImageFilter


def main():
    with Image.open("in.jpg") as img:
        #print(img.size)
        #print(img.format)
        img = img.rotate(180)
        #img = img.filter(ImageFilter.BLUR)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpg")


if __name__ == "__main__":
    main()