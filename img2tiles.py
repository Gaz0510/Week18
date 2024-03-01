import sys
from PIL import Image

def crop_to_4_3(img):
    # Get the dimensions of the original image
    width, height = img.size

    # Calculate the target height for a 4:3 aspect ratio
    target_height = width * 3 // 4

    # Check if the image is not in a 4:3 aspect ratio
    if height > target_height:
        # Calculate the cropping box
        upper = (height - target_height) // 2
        lower = height - upper

        # Crop the image to a 4:3 aspect ratio, maintaining a square aspect ratio
        img = img.crop((0, upper, width, min(lower, target_height)))

    return img

def split_image(input_path, output_path):
    # Open and crop the image if necessary
    img = Image.open(input_path)
    img = crop_to_4_3(img)

    # Get the dimensions of the cropped image
    width, height = img.size

    # Calculate the size of each square
    square_size = min(width // 3, height // 4)

    # Loop through each row and column to crop and save the squares
    for row in range(4):
        for col in range(3):
            left = col * square_size
            upper = row * square_size
            right = left + square_size
            lower = upper + square_size

            # Crop the image and save the square
            square = img.crop((left, upper, right, lower))
            square.save(f"{output_path}/tile_{row * 3 + col}.jpg")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_image_path> <output_directory>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_directory = sys.argv[2]

    split_image(input_image_path, output_directory)
