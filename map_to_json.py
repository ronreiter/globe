import json
from PIL import Image
import numpy as np

# Open the world map image
img = Image.open('worldmap.png')

# Resize to 195x105
img = img.resize((195, 105))

# Ensure we have alpha channel (RGBA mode)
img_rgba = img.convert('RGBA')

# Convert to binary (0 and 1)
# Any pixel with alpha > 0 is considered 1, transparent pixels (alpha = 0) are 0
binary_data = []

for y in range(img_rgba.height):
    row = ""
    for x in range(img_rgba.width):
        # Get RGBA values
        r, g, b, a = img_rgba.getpixel((x, y))
        # If alpha is 0 (completely transparent), it's 0, otherwise it's 1
        if a == 0:
            row += "0"
        else:
            row += "1"
    binary_data.append(row)

# Verify dimensions
assert len(binary_data) == 105, f"Expected 105 rows, got {len(binary_data)}"
for i, row in enumerate(binary_data):
    assert len(row) == 195, f"Row {i} expected length 195, got {len(row)}"

# Save to JSON file
with open('worldmap.json', 'w') as f:
    json.dump(binary_data, f)

print("Conversion complete. JSON file created with dimensions 195x105.")