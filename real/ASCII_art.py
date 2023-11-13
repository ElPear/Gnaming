from PIL import Image as __Image
from PIL import ImageDraw as __ImageDraw
from PIL import ImageFont as __ImageFont
import os as __os

# Define a list of symbols and set up image dimensions and font details
# most of these values are freeballed and i retried until it worked well enough
__grays = []
__symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890+-.,;:/([{#!%&= "
__width, __height = 60, 70
__font_path = "Cascadia.ttf" #important to use a monospaced font, otherwise it gets the dimensions wrong, i think
__font_size = 100
__font = __ImageFont.truetype(__font_path, __font_size)
__position = (0, -26)

# Generate images for each symbol and calculate the percentage of non-black pixels
for __item in __symbols:
    __letterimage = __Image.new("RGB", (__width, __height), "black")
    __draw = __ImageDraw.Draw(__letterimage)
    __draw.text(__position, __item, font=__font, fill="white")
    __counter = 0
    for __i in range(__width):
        for __j in range(__height):
            if __letterimage.getpixel((__i,__j)) != (0, 0, 0):
                __counter += 1
    __percentage = __counter / (__width * __height)
    __grays.append((__percentage, __item))

# Function to calculate average grayscale intensity of an image
def __average_gray(img):
    pixels = list(img.getdata())
    average_intensity = sum(pixels) / len(pixels)
    normalized_intensity = average_intensity / 255.0
    return normalized_intensity

# Function to find the closest match in a list to a given value
def __closest(lst, value):
    away = 255
    list_value = ""

    for item in lst:
        temp_away = abs(item[0] - value)
        if temp_away <= away:
            away = temp_away
            list_value = item

    return (away, list_value)

# Function to resize an image to a set aspect ratio
def __resize_image(input_path, output_path):
    img = __Image.open(input_path)

    target_width = round((img.width / __width)) * __width
    target_height = round((img.height / __height)) * __height

    target_ratio = target_width / target_height

    current_width, current_height = img.size
    current_ratio = current_width / current_height

    if target_ratio == current_ratio:
        return

    if current_ratio > target_ratio:
        new_width = int(target_width)
        new_height = int(target_width / current_ratio)
    else:
        new_width = int(target_height * current_ratio)
        new_height = int(target_height)

    resized_img = img.resize((new_width, new_height), __Image.ANTIALIAS)
    resized_img.save(output_path)

# Function to convert an image to ASCII art
def convertImage(imageFilePath):
    __os.system("cls")
    __resize_image(imageFilePath, imageFilePath)
    newImage = __Image.open(imageFilePath).convert("L")

    block = ""
    text = ""
    for j in range(0, newImage.height, 7):
        for i in range(0, newImage.width, 6):
            cropped = newImage.crop((i, j, i + 6, j + 7))
            perc = __average_gray(cropped)

            closestLetter = __closest(__grays, perc)[1][1]
            text += closestLetter
        block = block + text + "\n"
        text = ""
    print(block)

# example: convertImage("placeholder.png") will print it into the terminal
