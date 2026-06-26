# === Pillow (PIL) Image Processing ===


# ========== TABLE OF CONTENTS ==========
#
# 1. OPENING AND SAVING (WITH 'with')
# 2. BASIC INFORMATION & METADATA
# 3. ROTATING, FLIPPING, TRANSFORMING
# 4. FILTERS (ImageFilter)
# 5. RESIZING, THUMBNAILS, RESAMPLING
# 6. CROPPING
# 7. COLOR CONVERSION & MODES
# 8. IMAGE ENHANCEMENT (brightness, contrast, etc.)
# 9. IMAGEOPS (auto contrast, equalize, fit, etc.)
# 10. DRAWING ON IMAGES (shapes, text, fonts)
# 11. PASTING AND COMPOSITING
# 12. CREATING ANIMATED GIFS (MULTI‑FRAME)
# 13. EXTRACTING FRAMES FROM A GIF
# 14. IMAGE CHANNEL OPERATIONS (ImageChops)
# 15. SAVING WITH QUALITY & OPTIMIZATION
# 16. EXIF DATA
# 17. QUICK REFERENCE
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


# ---------- 2. BASIC INFORMATION & METADATA ----------

# Definition: You can retrieve metadata from an open image object.

with Image.open("photo.jpg") as img:
    print(img.size)          # Tuple: (width, height) in pixels
    print(img.format)        # File format, e.g., 'JPEG', 'PNG', 'GIF'
    print(img.mode)          # Color mode: 'RGB', 'L' (grayscale), 'RGBA', 'P' (palette), '1' (b&w)

# Get image information dictionary (EXIF, etc.)
info = img.info
print(info.get('dpi'))       # DPI if available

# Get color palette (for 'P' mode)
if img.mode == 'P':
    palette = img.getpalette()


# ---------- 3. ROTATING, FLIPPING, TRANSFORMING ----------

# Definition: rotate() returns a new image rotated clockwise by the given degrees.
# expand=True enlarges the canvas to fit the rotated image.

with Image.open("in.jpg") as img:
    rotated_90 = img.rotate(90, expand=True)
    rotated_180 = img.rotate(180)
    rotated_270 = img.rotate(270, expand=True)
    rotated_180.save("rotated.jpg")

# transpose() flips the image.
with Image.open("in.jpg") as img:
    flip_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
    flip_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
    # Also available: TRANSPOSE (swap axes), TRANSVERSE (rotate 90 + flip)

# Transform (affine transform)
from PIL import ImageTransform
transform = ImageTransform.AffineTransform((1, 0, 10, 0, 1, 20))  # translate
transformed = img.transform(img.size, transform)


# ---------- 4. FILTERS (ImageFilter) ----------

# Definition: ImageFilter provides pre‑made convolution filters for effects.

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

    # Additional filters
    contour = img.filter(ImageFilter.CONTOUR)
    smooth = img.filter(ImageFilter.SMOOTH)
    detail = img.filter(ImageFilter.DETAIL)
    edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)

# Custom kernel (convolution)
kernel = [1, 0, -1, 1, 0, -1, 1, 0, -1]  # example edge detection
custom = img.filter(ImageFilter.Kernel((3,3), kernel, scale=1, offset=0))


# ---------- 5. RESIZING, THUMBNAILS, RESAMPLING ----------

# Definition: resize() returns a new image with exact dimensions (may distort aspect ratio).

with Image.open("large.jpg") as img:
    resized = img.resize((300, 200))   # width=300, height=200
    resized.save("resized.jpg")

    # Use high‑quality resampling filter
    resized_hq = img.resize((300, 200), resample=Image.LANCZOS)

# thumbnail() resizes in‑place, preserving aspect ratio to fit inside a box.
with Image.open("large.jpg") as img:
    img.thumbnail((200, 200))
    img.save("thumbnail.jpg")

# Available resampling filters: NEAREST, BILINEAR, BICUBIC, LANCZOS, BOX, HAMMING


# ---------- 6. CROPPING ----------

# Definition: crop() takes a box (left, upper, right, lower) and returns a new image.

with Image.open("photo.jpg") as img:
    cropped = img.crop((100, 100, 300, 300))
    cropped.save("cropped.jpg")

# Crop to a rectangle based on aspect ratio
width, height = img.size
box = (0, 0, width, int(height * 0.8))
top_part = img.crop(box)


# ---------- 7. COLOR CONVERSION & MODES ----------

# Definition: convert() changes the image's color mode.

with Image.open("color.jpg") as img:
    gray = img.convert("L")          # Grayscale (luminance)
    gray.save("grayscale.jpg")

    # RGB (remove alpha channel)
    rgb = img.convert("RGB")

    # RGBA (add alpha channel)
    rgba = img.convert("RGBA")

    # Palette mode (P) – quantize to 256 colors
    indexed = img.convert("P", palette=Image.ADAPTIVE)

    # Binary black & white (1‑bit)
    bw = img.convert("1")

# Split and merge channels (RGB only)
r, g, b = img.split()
merged = Image.merge("RGB", (r, g, b))


# ---------- 8. IMAGE ENHANCEMENT (brightness, contrast, etc.) ----------

# Definition: ImageEnhance module adjusts brightness, contrast, sharpness, and color.

from PIL import ImageEnhance

with Image.open("photo.jpg") as img:
    # Brightness
    enhancer = ImageEnhance.Brightness(img)
    brighter = enhancer.enhance(1.5)   # >1 brighter, <1 darker

    # Contrast
    enhancer = ImageEnhance.Contrast(img)
    higher_contrast = enhancer.enhance(1.8)

    # Sharpness
    enhancer = ImageEnhance.Sharpness(img)
    sharper = enhancer.enhance(2.0)

    # Color (saturation)
    enhancer = ImageEnhance.Color(img)
    more_color = enhancer.enhance(1.5)

    # Save results
    brighter.save("brighter.jpg")


# ---------- 9. IMAGEOPS (auto contrast, equalize, fit, etc.) ----------

# Definition: ImageOps contains ready‑made operations like auto‑contrast, equalize, fit, etc.

from PIL import ImageOps

with Image.open("photo.jpg") as img:
    # Auto‑contrast (stretch histogram)
    auto_contrast = ImageOps.autocontrast(img)

    # Equalize histogram
    equalized = ImageOps.equalize(img)

    # Fit into a box (like thumbnail but returns a new image)
    fitted = ImageOps.fit(img, (200, 200), method=Image.LANCZOS, centering=(0.5, 0.5))

    # Expand borders (pad)
    padded = ImageOps.expand(img, border=20, fill='black')

    # Invert colors
    inverted = ImageOps.invert(img)

    # Mirror (horizontal flip)
    mirrored = ImageOps.mirror(img)

    # Flip (vertical flip)
    flipped = ImageOps.flip(img)

    # Grayscale (convert to 'L')
    gray = ImageOps.grayscale(img)

    auto_contrast.save("autocontrast.jpg")


# ---------- 10. DRAWING ON IMAGES (shapes, text, fonts) ----------

# Definition: ImageDraw allows drawing shapes, lines, text, etc.

from PIL import ImageDraw, ImageFont

with Image.new("RGB", (400, 300), "white") as img:
    draw = ImageDraw.Draw(img)

    # Shapes
    draw.rectangle([(50, 50), (150, 100)], fill="blue", outline="black", width=2)
    draw.ellipse([(200, 50), (300, 120)], fill="red", outline="green")
    draw.line([(50, 150), (350, 150)], fill="black", width=3)
    draw.polygon([(50, 200), (100, 250), (30, 250)], fill="yellow", outline="purple")
    draw.arc([(200, 200), (300, 280)], start=0, end=180, fill="orange", width=2)
    draw.chord([(200, 200), (300, 280)], start=0, end=180, outline="brown")
    draw.pieslice([(200, 200), (300, 280)], start=0, end=180, fill="pink")

    # Text with default font
    draw.text((50, 30), "Hello Pillow", fill="black")

    # Text with custom font (provide path to .ttf file)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
        draw.text((50, 260), "Custom font", font=font, fill="darkblue")
    except IOError:
        draw.text((50, 260), "Custom font (default)", fill="darkblue")

    img.save("drawn.jpg")


# ---------- 11. PASTING AND COMPOSITING ----------

# Definition: paste() places an image onto another. composite() blends images using a mask.

# Paste an image onto another
background = Image.new("RGB", (400, 300), "white")
overlay = Image.open("logo.png").convert("RGBA")
background.paste(overlay, (50, 50), mask=overlay)  # mask uses alpha channel
background.save("pasted.jpg")

# Composite (blend two images using a mask)
image1 = Image.open("img1.jpg").convert("RGB")
image2 = Image.open("img2.jpg").convert("RGB")
mask = Image.open("mask.png").convert("L")   # grayscale mask
composite = Image.composite(image1, image2, mask)
composite.save("composite.jpg")

# Blend two images with constant alpha
blended = Image.blend(image1, image2, alpha=0.5)   # 0=image1, 1=image2
blended.save("blended.jpg")


# ---------- 12. CREATING ANIMATED GIFS (MULTI‑FRAME) ----------

# Definition: Save a list of images as an animated GIF using save_all=True and append_images.

frames = []
for i in range(1, 4):
    with Image.open(f"frame{i}.jpg") as f:
        frames.append(f.copy())   # Copy needed because 'with' closes

frames[0].save(
    "animation.gif",
    save_all=True,
    append_images=frames[1:],
    duration=200,        # milliseconds per frame
    loop=0,              # 0 = infinite loop
    optimize=True        # reduce size
)


# ---------- 13. EXTRACTING FRAMES FROM A GIF ----------

# Definition: Iterate through frames of an existing GIF using seek().

with Image.open("animation.gif") as gif:
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        gif.save(f"frame_{frame_index}.png")


# ---------- 14. IMAGE CHANNEL OPERATIONS (ImageChops) ----------

# Definition: ImageChops provides operations on image channels (difference, invert, multiply, etc.)

from PIL import ImageChops

with Image.open("img1.jpg") as img1, Image.open("img2.jpg") as img2:
    # Difference between two images
    diff = ImageChops.difference(img1, img2)
    diff.save("diff.jpg")

    # Invert
    inverted = ImageChops.invert(img1)
    inverted.save("inverted.jpg")

    # Multiply (darken)
    multiplied = ImageChops.multiply(img1, img2)
    multiplied.save("multiplied.jpg")

    # Screen (lighten)
    screened = ImageChops.screen(img1, img2)

    # Add
    added = ImageChops.add(img1, img2, scale=2.0, offset=0)

    # Subtract
    subtracted = ImageChops.subtract(img1, img2, scale=2.0, offset=0)

    # Logical operations (binary images)
    # ImageChops.logical_and, logical_or, logical_xor


# ---------- 15. SAVING WITH QUALITY & OPTIMIZATION ----------

# Definition: You can control compression and quality when saving images.

with Image.open("photo.jpg") as img:
    # JPEG quality (1-95, default 75)
    img.save("high_quality.jpg", quality=95)
    img.save("low_quality.jpg", quality=20)

    # Progressive JPEG (loads in stages)
    img.save("progressive.jpg", progressive=True)

    # Optimize (reduce file size)
    img.save("optimized.jpg", optimize=True)

    # PNG compression (0-9, default 6)
    img.save("compressed.png", compress_level=9)

    # Save as WebP (smaller)
    img.save("image.webp", quality=80)


# ---------- 16. EXIF DATA ----------

# Definition: EXIF contains metadata (camera settings, GPS, date) from JPEGs.

with Image.open("photo.jpg") as img:
    exif = img.getexif()
    if exif:
        for tag_id, value in exif.items():
            tag_name = Image.ExifTags.TAGS.get(tag_id, tag_id)
            print(f"{tag_name}: {value}")

    # Remove EXIF data (privacy)
    img.save("no_exif.jpg", exif=None)


# ---------- 17. QUICK REFERENCE ----------

# | Operation                         | Code                                                      |
# |-----------------------------------|-----------------------------------------------------------|
# | Open with 'with'                  | `with Image.open("in.jpg") as img:`                      |
# | Get size                          | `img.size`                                                |
# | Get format / mode                 | `img.format`, `img.mode`                                  |
# | Rotate 180°                       | `img.rotate(180)`                                         |
# | Find edges filter                 | `img.filter(ImageFilter.FIND_EDGES)`                      |
# | Blur filter                       | `img.filter(ImageFilter.BLUR)`                            |
# | Resize (exact)                    | `img.resize((w, h), resample=Image.LANCZOS)`              |
# | Thumbnail (aspect‑aware)          | `img.thumbnail((max_w, max_h))`                           |
# | Crop                              | `img.crop((left, top, right, bottom))`                    |
# | Grayscale                         | `img.convert("L")`                                        |
# | Brightness adjust                 | `ImageEnhance.Brightness(img).enhance(factor)`            |
# | Contrast adjust                   | `ImageEnhance.Contrast(img).enhance(factor)`              |
# | Auto‑contrast                     | `ImageOps.autocontrast(img)`                              |
# | Fit into box (keep aspect)        | `ImageOps.fit(img, (w, h))`                               |
# | Paste image on another            | `background.paste(overlay, (x,y), mask=overlay)`          |
# | Composite with mask               | `Image.composite(img1, img2, mask)`                       |
# | Create animated GIF               | `frames[0].save(..., save_all=True, append_images=frames[1:])` |
# | Extract frames from GIF           | `gif.seek(index)`                                         |
# | ImageChops difference             | `ImageChops.difference(img1, img2)`                       |
# | Save with JPEG quality            | `img.save("out.jpg", quality=95)`                         |
# | Remove EXIF                       | `img.save("out.jpg", exif=None)`                          |