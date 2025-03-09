from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk  # Pillow is used for image processing

# ---------------------------------------------------------------------------
# Resource Paths Configuration
# ---------------------------------------------------------------------------
# Set up the asset path for frame4. Adjust the asset directory as needed.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame4")


def relative_to_assets(path: str) -> Path:
    """
    Returns the full path to an asset file based on the provided relative path.

    :param path: Relative path to the asset.
    :return: A Path object representing the full asset path.
    """
    return ASSETS_PATH / Path(path)


# ---------------------------------------------------------------------------
# Image Scaling Function
# ---------------------------------------------------------------------------
def scaled_photoimage(image_path: str, scale_x: float, scale_y: float) -> ImageTk.PhotoImage:
    """
    Opens an image from the specified path, scales it according to the given scaling
    factors, and converts it into a Tkinter-compatible PhotoImage.

    :param image_path: The path to the image file.
    :param scale_x: Scaling factor in the horizontal direction.
    :param scale_y: Scaling factor in the vertical direction.
    :return: A PhotoImage object representing the scaled image.
    """
    img = Image.open(image_path)  # Open the image file.
    orig_width, orig_height = img.size  # Get the original dimensions.
    new_size = (int(orig_width * scale_x), int(orig_height * scale_y))  # Calculate new dimensions.
    # Resize using high-quality LANCZOS resampling.
    img = img.resize(new_size, resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


# ---------------------------------------------------------------------------
# Window and Canvas Setup
# ---------------------------------------------------------------------------
# Define original design dimensions.
orig_width = 1455
orig_height = 1041

# Define new window dimensions (for example: 800x600; modify as needed).
new_width = 800
new_height = 600

# Calculate scaling factors.
scale_x = new_width / orig_width
scale_y = new_height / orig_height

# Create the main window.
window = Tk()
window.geometry(f"{new_width}x{new_height}")  # Set window size to new dimensions.
window.configure(bg="#FFFFFF")

# Create a Canvas using the original design dimensions.
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=orig_height,
    width=orig_width,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)  # Place canvas at the top-left corner.

# ---------------------------------------------------------------------------
# Canvas Background & Graphics (to be scaled uniformly later)
# ---------------------------------------------------------------------------
# Left sidebar background.
canvas.create_rectangle(
    0.0,  # x1
    1.0,  # y1
    235.0,  # x2
    1042.0,  # y2
    fill="#79BCF7",
    outline=""
)

# Top rectangle for "SORT BY:" section.
canvas.create_rectangle(
    1063.0,  # x1
    0.0,  # y1
    1455.0,  # x2
    81.0,  # y2
    fill="#DAEBF9",
    outline=""
)

# ---------------------------------------------------------------------------
# Widgets on Canvas & Window
# ---------------------------------------------------------------------------
# Scale and place button images and other widgets.

# Button 1
button_image_1 = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1.0 * scale_x,
    y=402.0 * scale_y,
    width=235.0 * scale_x,
    height=100.0 * scale_y
)

# Button 2
button_image_2 = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
button_2 = Button(
    window,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0 * scale_x,
    y=302.0 * scale_y,
    width=235.0 * scale_x,
    height=100.0 * scale_y
)

# Button 3
button_image_3 = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
button_3 = Button(
    window,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=0.0 * scale_x,
    y=202.0 * scale_y,
    width=235.0 * scale_x,
    height=100.0 * scale_y
)

# Button 4
button_image_4 = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
button_4 = Button(
    window,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=0.0 * scale_x,
    y=102.0 * scale_y,
    width=235.0 * scale_x,
    height=100.0 * scale_y
)

# Button 5
button_image_5 = scaled_photoimage(str(relative_to_assets("button_5.png")), scale_x, scale_y)
button_5 = Button(
    window,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=0.0 * scale_x,
    y=1.5 * scale_y,
    width=235.0 * scale_x,
    height=100.0 * scale_y
)

# Canvas image (image_1).
image_1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
canvas.create_image(
    118.0 * scale_x,
    993.0 * scale_y,
    image=image_1
)

# Entry background image and entry widget.
entry_image_1 = scaled_photoimage(str(relative_to_assets("entry_1.png")), scale_x, scale_y)
entry_bg_1 = canvas.create_image(
    1301.0 * scale_x,
    40.5 * scale_y,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1167.0 * scale_x,
    y=14.0 * scale_y,
    width=268.0 * scale_x,
    height=51.0 * scale_y
)

# Canvas image (image_2).
image_2 = scaled_photoimage(str(relative_to_assets("image_2.png")), scale_x, scale_y)
canvas.create_image(
    1116.0 * scale_x,
    41.0 * scale_y,
    image=image_2
)

# Canvas text "SORT BY:".
canvas.create_text(
    1067.0 * scale_x,
    113.0 * scale_y,
    anchor="nw",
    text="SORT BY:",
    fill="#094478",
    font=("Jomolhari Regular", int(20 * scale_y))
)

# Button 6
button_image_6 = scaled_photoimage(str(relative_to_assets("button_6.png")), scale_x, scale_y)
button_6 = Button(
    window,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1167.0 * scale_x,
    y=864.0 * scale_y,
    width=200.0 * scale_x,
    height=101.0 * scale_y
)

# Button 7
button_image_7 = scaled_photoimage(str(relative_to_assets("button_7.png")), scale_x, scale_y)
button_7 = Button(
    window,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1204.0 * scale_x,
    y=107.0 * scale_y,
    width=134.0 * scale_x,
    height=41.0 * scale_y
)

# ---------------------------------------------------------------------------
# Uniform Scaling of Canvas Items
# ---------------------------------------------------------------------------
# Scale all canvas items (rectangles, texts, etc.) using the computed scaling factors.
canvas.scale("all", 0, 0, scale_x, scale_y)

# ---------------------------------------------------------------------------
# Final Window Settings and Main Loop
# ---------------------------------------------------------------------------
window.resizable(False, False)
window.mainloop()
