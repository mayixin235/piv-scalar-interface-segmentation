from PIL import Image
import os

x = "case3" # case number
y = "train"

for i in range(1, 161):

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/image raw/" + str(i) + ".png")
    #image.show()

    # The file format
    print(image.format)

    # The pixel format
    print(image.mode)

    # Image size
    print(image.size)

    # Colour palette
    print(image.palette)

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/image raw/" + str(i) + ".png")
    new_image = image.resize((256, 256))
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + y + "/image raw/" + str(i) + ".png")

    print(image.size)
    print(new_image.size)

z = "validation"

for i in range(161, 181):

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/image raw/" + str(i) + ".png")
    #image.show()

    print(image.format)

    print(image.mode)

    print(image.size)

    print(image.palette)

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/image raw/" + str(i) + ".png")
    new_image = image.resize((256, 256))
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + z + "/image raw/" + str(i) + ".png")

    print(image.size)
    print(new_image.size)


a = "test"

for i in range(181, 201):

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/image raw/" + str(i) + ".png")
    #image.show()

    print(image.format)

    print(image.mode)

    print(image.size)

    print(image.palette)

    image = Image.open("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/image raw/" + str(i) + ".png")
    new_image = image.resize((256, 256))
    new_image.save("C:/Users/oguri/Desktop/cases/" + x + "/" + a + "/image raw/" + str(i) + ".png")

    print(image.size)
    print(new_image.size)
