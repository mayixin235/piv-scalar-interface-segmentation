from PIL import Image
import os

x = "case2"
y = "train"

for i in range(1, 161):
    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/mask raw/" + str(i) + ".png")
    # image.show()

    print(image.format)

    print(image.mode)

    print(image.size)

    print(image.palette)

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/mask raw/" + str(i) + ".png")
    new_image = image.resize((256, 256))
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/mask raw/" + str(i) + ".png")
    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/mask raw/" + str(i) + ".png")
    new_image = image.convert("1")
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/mask raw/" + str(i) + ".png")

    print(image.size)
    print(new_image.size)
    print(new_image.mode)

z = "validation"
for i in range(161, 181):
    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/mask raw/" + str(i) + ".png")

    print(image.format)

    print(image.mode)

    print(image.size)

    print(image.palette)

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/mask raw/" + str(i) + ".png")
    new_image = image.resize((256, 256))
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/mask raw/" + str(i) + ".png")
    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/mask raw/" + str(i) + ".png")
    new_image = image.convert("1")
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/mask raw/" + str(i) + ".png")

    print(image.size)
    print(new_image.size)
    print(new_image.mode)

a = "test"
for i in range(181, 201):
    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/mask raw/" + str(i) + ".png")

    print(image.format)

    print(image.mode)

    print(image.size)

    print(image.palette)

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/mask raw/" + str(i) + ".png")
    new_image = image.resize((256, 256))
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/mask raw/" + str(i) + ".png")
    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/mask raw/" + str(i) + ".png")
    new_image = image.convert("1")
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/mask raw/" + str(i) + ".png")

    print(image.size)
    print(new_image.size)
    print(new_image.mode)
