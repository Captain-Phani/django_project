from PIL import Image, ImageDraw


def crop_triangle(image_path, coordinates, output_path):
    # Open the image using Pillow
    img = Image.open(image_path)
    # rows,cols,_=img.shape
    # print(rows,"Rows")
    # print(cols,"Cols")
    print(img.size)

    # Create a mask with the same size as the image
    mask = Image.new("L", img.size, 0)

    # Define the coordinates of the triangle vertices
    draw = ImageDraw.Draw(mask)
    draw.polygon(coordinates, fill=255)

    # Apply the mask to the image
    result = Image.new("RGBA", img.size)
    result.paste(img, mask=mask)

    # Crop the result image to the size of the triangle
    bbox = result.getbbox()
    cropped_img = result.crop(bbox)

    # Save the cropped image
    cropped_img.save(output_path)


# Path to the input image
input_image_path = "C:/Users/Phani/Pictures/Saved Pictures/wallpaperflare.com_wallpaper.jpg"

# Coordinates of the triangle vertices (change these)
triangle_coordinates = [(900,1000),(100,700),(100,300),(900,100),(1700,300),(1700,700)]

# Path to save the cropped triangle image
output_image_path = "output_triangle.png"

# Call the function to crop the triangle
crop_triangle(input_image_path, triangle_coordinates, output_image_path)