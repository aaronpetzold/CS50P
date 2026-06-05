import csv
import numpy as np
from PIL import Image


def main():
    # Open the input CSV file for reading and the output CSV file for writing
    with open("views.csv", "r") as views, open(
        "analysis.csv", "w", newline=""
    ) as analysis:
        reader = csv.DictReader(views)

        # Create the headers for the new file (old headers + "brightness")
        fieldnames = reader.fieldnames + ["brightness"]
        writer = csv.DictWriter(analysis, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through each row, calculate brightness, and write to analysis.csv
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),
                }
            )


def calculate_brightness(filename):
    # Open the image, convert to grayscale ("L"), and calculate the average value
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


if __name__ == "__main__":
    main()
