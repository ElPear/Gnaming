from PIL import Image, ImageDraw, ImageFont
import os

# Define a list of symbols and set up image dimensions and font details
# most of these values are freeballed and i retried until it worked well enough
grays = []
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890+-.,;:/([{#!%&= "
width, height = 60, 70
font_path = "Cascadia.ttf" #important to use a monospaced font, otherwise it gets the dimensions wrong, i think
font_size = 100
font = ImageFont.truetype(font_path, font_size)
position = (0, -26)

# Generate images for each symbol and calculate the percentage of non-black pixels
for item in symbols:
    letterimage = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(letterimage)
    draw.text(position, item, font=font, fill="white")
    counter = 0
    for i in range(width):
        for j in range(height):
            if letterimage.getpixel((i,j)) != (0, 0, 0):
                counter += 1
    percentage = counter / (width * height)
    grays.append((percentage, item))

# Function to calculate average grayscale intensity of an image
def average_gray(img):
    pixels = list(img.getdata())
    average_intensity = sum(pixels) / len(pixels)
    normalized_intensity = average_intensity / 255.0
    return normalized_intensity

# Function to find the closest match in a list to a given value
def closest(lst, value):
    away = 255
    list_value = ""

    for item in lst:
        temp_away = abs(item[0] - value)
        if temp_away <= away:
            away = temp_away
            list_value = item

    return (away, list_value)

# Functions to convert between grayscale values and RGB colors
def value_to_gray(value):
    value = max(0, min(1, value))
    gray_value = int(value * 255)
    return (gray_value, gray_value, gray_value)

def gray_to_value(gray_color):
    gray_value = gray_color[1]
    value = 1 - (gray_value / 255)
    value = max(0, min(1, value))
    return value

# Function to resize an image to a set aspect ratio
def resize_image(input_path, output_path):
    img = Image.open(input_path)

    target_width = round((img.width / width)) * width
    target_height = round((img.height / height)) * height

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

    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    resized_img.save(output_path)

# Function to convert an image to ASCII art
def convertImage(image):
    os.system("cls")
    resize_image(image, image)
    newImage = Image.open(image).convert("L")

    block = ""
    text = ""
    for j in range(0, newImage.height, 7):
        for i in range(0, newImage.width, 6):
            cropped = newImage.crop((i, j, i + 6, j + 7))
            perc = average_gray(cropped)

            closestLetter = closest(grays, perc)[1][1]
            text += closestLetter
        block = block + text + "\n"
        text = ""
    print(block)

#clear the console
os.system("cls") 

convertImage("placeholder.png")
