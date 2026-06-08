# === Pillow (PIL) Image Processing ===


# ========== TABLE OF CONTENTS ==========
#
# 1. OPENING AND SAVING (WITH 'with')
# 2. BASIC INFORMATION
# 3. ROTATING AND FLIPPING
# 4. FILTERS (ImageFilter)
# 5. RESIZING AND THUMBNAILS
# 6. CROPPING
# 7. COLOR CONVERSION
# 8. DRAWING ON IMAGES
# 9. CREATING ANIMATED GIFS (MULTI‑FRAME)
# 10. EXTRACTING FRAMES FROM A GIF
# 11. QUICK REFERENCE
#
# ========================================


# Definition: Pillow is the modern fork of PIL (Python Imaging Library).
# It allows you to open, manipulate, and save many image formats.


# ---------- 1. OPENING AND SAVING (WITH 'with') ----------

# Definition: The 'with' statement opens the image and automatically closes the file when done,
# preventing memory leaks. Use this pattern whenever possible.

with Image.open("in.jpg") as img:
    # Work with the image here
    img.save("out.jpg")   # Saves in the same format as original (or specify extension)

# Without 'with' (still works, but you must close manually)
img = Image.open("in.jpg")
img.close()   # Don't forget!


# ---------- 2. BASIC INFORMATION ----------

# Definition: You can retrieve metadata from an open image object.

with Image.open("photo.jpg") as img:
    print(img.size)          # Tuple: (width, height) in pixels
    print(img.format)        # File format, e.g., 'JPEG', 'PNG', 'GIF'
    print(img.mode)          # Color mode: 'RGB', 'L' (grayscale), 'RGBA', etc.


# ---------- 3. ROTATING AND FLIPPING ----------

# Definition: rotate() returns a new image rotated clockwise by the given degrees.

with Image.open("in.jpg") as img:
    rotated_90 = img.rotate(90)
    rotated_180 = img.rotate(180)
    rotated_270 = img.rotate(270)
    rotated_180.save("rotated.jpg")

# Definition: transpose() flips the image horizontally or vertically.

with Image.open("in.jpg") as img:
    flip_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
    flip_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)


# ---------- 4. FILTERS (ImageFilter) ----------

# Definition: ImageFilter provides pre‑made convolution filters for effects like blurring,
# sharpening, and edge detection.

from PIL import ImageFilter

with Image.open("in.jpg") as img:
    blurred = img.filter(ImageFilter.BLUR)
    blurred.save("blurred.jpg")

    sharpened = img.filter(ImageFilter.SHARPEN)
    sharpened.save("sharpened.jpg")

    edges = img.filter(ImageFilter.FIND_EDGES)
    edges.save("edges.jpg")

    embossed = img.filter(ImageFilter.EMBOSS)
    embossed.save("embossed.jpg")

# Other useful filters:
# ImageFilter.CONTOUR, ImageFilter.SMOOTH, ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE


# ---------- 5. RESIZING AND THUMBNAILS ----------

# Definition: resize() returns a new image with the exact dimensions you give
# (may distort aspect ratio).

with Image.open("large.jpg") as img:
    resized = img.resize((300, 200))   # width=300, height=200
    resized.save("resized.jpg")

# Definition: thumbnail() resizes the image in place, preserving aspect ratio
# so it fits inside the given box.

with Image.open("large.jpg") as img:
    img.thumbnail((200, 200))   # Fits within 200x200, keeps proportions
    img.save("thumbnail.jpg")   # Saves the modified original


# ---------- 6. CROPPING ----------

# Definition: crop() takes a box tuple (left, upper, right, lower) and returns a new image
# of that rectangular region. Coordinates: (0,0) is the top‑left corner.

with Image.open("photo.jpg") as img:
    # Crop a 200x200 square from top‑left
    cropped = img.crop((0, 0, 200, 200))
    cropped.save("cropped.jpg")


# ---------- 7. COLOR CONVERSION ----------

# Definition: convert() changes the image's color mode.

with Image.open("color.jpg") as img:
    gray = img.convert("L")          # Grayscale
    gray.save("grayscale.jpg")

    rgb = img.convert("RGB")         # Remove alpha channel if present
    rgba = img.convert("RGBA")       # Add alpha channel for transparency


# ---------- 8. DRAWING ON IMAGES ----------

# Definition: ImageDraw allows you to draw shapes, lines, and text on an image.

from PIL import ImageDraw, ImageFont

with Image.new("RGB", (400, 200), "white") as img:
    draw = ImageDraw.Draw(img)
    draw.rectangle([(50, 50), (150, 100)], fill="blue", outline="black")
    draw.ellipse([(200, 50), (300, 120)], fill="red")
    draw.text((50, 30), "Hello Pillow", fill="black")
    img.save("drawn.jpg")


# ---------- 9. CREATING ANIMATED GIFS (MULTI‑FRAME) ----------

# Definition: Save a list of images as an animated GIF by using save_all=True and append_images.

frames = []
for i in range(1, 4):
    with Image.open(f"frame{i}.jpg") as f:
        frames.append(f.copy())   # Copy needed because 'with' will close

# Save the first frame with the rest appended
frames[0].save(
    "animation.gif",
    save_all=True,
    append_images=frames[1:],
    duration=200,    # milliseconds per frame
    loop=0           # 0 = infinite loop
)


# ---------- 10. EXTRACTING FRAMES FROM A GIF ----------

# Definition: Iterate through frames of an existing GIF using seek().

with Image.open("animation.gif") as gif:
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        gif.save(f"frame_{frame_index}.png")


# ---------- 11. QUICK REFERENCE ----------

# | Operation                 | Code                                              |
# |---------------------------|---------------------------------------------------|
# | Open with 'with'          | `with Image.open("in.jpg") as img:`              |
# | Get size                  | `img.size`                                        |
# | Get format                | `img.format`                                      |
# | Rotate 180°               | `img.rotate(180)`                                 |
# | Find edges filter         | `img.filter(ImageFilter.FIND_EDGES)`              |
# | Blur filter               | `img.filter(ImageFilter.BLUR)`                    |
# | Save image                | `img.save("out.jpg")`                             |
# | Resize                    | `img.resize((new_w, new_h))`                      |
# | Thumbnail (aspect‑aware)  | `img.thumbnail((max_w, max_h))`                   |
# | Crop                      | `img.crop((left, top, right, bottom))`            |
# | Convert to grayscale      | `img.convert("L")`                                |