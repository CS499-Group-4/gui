from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button
from PIL import Image, ImageTk  # Pillow is used for image processing

# ---------------------------------------------------------------------------
# Resource Paths Configuration
# ---------------------------------------------------------------------------
# Set up the asset path for frame5. Adjust the asset directory as needed.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame5")


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

# Define new window dimensions (example: 800x600; modify as needed).
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
canvas.place(x=0, y=0)  # Place canvas at top-left.

# ---------------------------------------------------------------------------
# Canvas Background & Graphics (will be scaled uniformly later)
# ---------------------------------------------------------------------------
# Draw the left sidebar background rectangle.
canvas.create_rectangle(
    0.0,  # x1 (top-left)
    1.0,  # y1 (top-left)
    235.0,  # x2 (bottom-right)
    1042.0,  # y2 (bottom-right)
    fill="#79BCF7",
    outline=""
)

# Draw the top rectangle for "Font Setting:" (right side).
canvas.create_rectangle(
    296.0,  # x1
    41.0,  # y1
    1403.0,  # x2
    148.0,  # y2
    fill="#DAEBF9",
    outline=""
)

# Create text for "Font Setting:".
canvas.create_text(
    323.0,  # x
    76.0,  # y
    anchor="nw",
    text="Font Setting:",
    fill="#094478",
    font=("Jomolhari Regular", 10)  # Original font size; will be scaled later.
)

# Draw two rectangles for additional display areas.
canvas.create_rectangle(
    289.0,
    502.0,
    1396.0,
    609.0,
    fill="#DAEBF9",
    outline=""
)
canvas.create_rectangle(
    289.0,
    697.0,
    1403.0,
    804.0,
    fill="#DAEBF9",
    outline=""
)

# Create a rectangle and text for "Font Size:".
canvas.create_rectangle(
    296.0,
    239.0,
    1403.0,
    346.0,
    fill="#DAEBF9",
    outline=""
)
canvas.create_text(
    323.0,
    274.0,
    anchor="nw",
    text="Font Size:",
    fill="#094478",
    font=("Jomolhari Regular", 10)
)

# Create text for the default display mode.
canvas.create_text(
    296.0,
    430.0,
    anchor="nw",
    text="Default display mode of class schedule: ",
    fill="#094478",
    font=("Jomolhari Regular", 16)
)

# Draw a horizontal separator line.
canvas.create_rectangle(
    502.0,
    293.00000002561853,
    1350.0000066752837,
    298.0,
    fill="#094478",
    outline=""
)

# Create additional text for "Font Setting:" below.
canvas.create_text(
    330.0,
    735.0,
    anchor="nw",
    text="Font Setting:",
    fill="#094478",
    font=("Jomolhari Regular", 24)
)

# ---------------------------------------------------------------------------
# Canvas Image (Logo or Other Graphic)
# ---------------------------------------------------------------------------
# Load and add the bottom image using the scaled_photoimage function.
image_1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
canvas.create_image(
    215.0 * scale_x,  # Scaled x-coordinate for the image position
    1700.0 * scale_y,  # Scaled y-coordinate for the image position
    image=image_1  # The image to be drawn
)

# ---------------------------------------------------------------------------
# Sidebar Buttons (Left Side) - Placed on Window with Scaled Coordinates
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Top Buttons on Right Side (Font Setting Controls)
# ---------------------------------------------------------------------------
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
    x=503.0 * scale_x,
    y=64.0 * scale_y,
    width=169.0 * scale_x,
    height=66.0 * scale_y
)

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
    x=503.0 * scale_x,
    y=64.0 * scale_y,
    width=169.0 * scale_x,
    height=66.0 * scale_y
)

button_image_8 = scaled_photoimage(str(relative_to_assets("button_8.png")), scale_x, scale_y)
button_8 = Button(
    window,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=959.0 * scale_x,
    y=64.0 * scale_y,
    width=169.0 * scale_x,
    height=66.0 * scale_y
)

button_image_9 = scaled_photoimage(str(relative_to_assets("button_9.png")), scale_x, scale_y)
button_9 = Button(
    window,
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=1181.0 * scale_x,
    y=64.0 * scale_y,
    width=169.0 * scale_x,
    height=66.0 * scale_y
)

button_image_10 = scaled_photoimage(str(relative_to_assets("button_10.png")), scale_x, scale_y)
button_10 = Button(
    window,
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=727.0 * scale_x,
    y=64.0 * scale_y,
    width=169.0 * scale_x,
    height=66.0 * scale_y
)

# ---------------------------------------------------------------------------
# Lower Buttons for Additional Controls
# ---------------------------------------------------------------------------
canvas.create_rectangle(
    289.0,
    502.0,
    1396.0,
    609.0,
    fill="#DAEBF9",
    outline=""
)
canvas.create_rectangle(
    289.0,
    697.0,
    1403.0,
    804.0,
    fill="#DAEBF9",
    outline=""
)

button_image_11 = scaled_photoimage(str(relative_to_assets("button_11.png")), scale_x, scale_y)
button_11 = Button(
    window,
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=342.0 * scale_x,
    y=525.0 * scale_y,
    width=226.0 * scale_x,
    height=66.0 * scale_y
)

button_image_12 = scaled_photoimage(str(relative_to_assets("button_12.png")), scale_x, scale_y)
button_12 = Button(
    window,
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=729.0 * scale_x,
    y=525.0 * scale_y,
    width=226.0 * scale_x,
    height=66.0 * scale_y
)

button_image_13 = scaled_photoimage(str(relative_to_assets("button_13.png")), scale_x, scale_y)
button_13 = Button(
    window,
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=1116.0 * scale_x,
    y=525.0 * scale_y,
    width=226.0 * scale_x,
    height=66.0 * scale_y
)

canvas.create_rectangle(
    296.0,
    239.0,
    1403.0,
    346.0,
    fill="#DAEBF9",
    outline=""
)
canvas.create_text(
    323.0,
    274.0,
    anchor="nw",
    text="Font Size:",
    fill="#094478",
    font=("Jomolhari Regular", 14)
)

canvas.create_rectangle(
    502.0,
    293.00000002561853,
    1350.0000066752837,
    298.0,
    fill="#094478",
    outline=""
)
canvas.create_text(
    330.0,
    735.0,
    anchor="nw",
    text="Font Setting:",
    fill="#094478",
    font=("Jomolhari Regular", 10)
)

button_image_14 = scaled_photoimage(str(relative_to_assets("button_14.png")), scale_x, scale_y)
button_14 = Button(
    window,
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=551.0 * scale_x,
    y=718.0 * scale_y,
    width=298.0 * scale_x,
    height=66.0 * scale_y
)

button_image_15 = scaled_photoimage(str(relative_to_assets("button_15.png")), scale_x, scale_y)
button_15 = Button(
    window,
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=979.0 * scale_x,
    y=718.0 * scale_y,
    width=298.0 * scale_x,
    height=66.0 * scale_y
)

button_image_16 = scaled_photoimage(str(relative_to_assets("button_16.png")), scale_x, scale_y)
button_16 = Button(
    window,
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=377.0 * scale_x,
    y=888.0 * scale_y,
    width=348.0 * scale_x,
    height=94.0 * scale_y
)

button_image_17 = scaled_photoimage(str(relative_to_assets("button_17.png")), scale_x, scale_y)
button_17 = Button(
    window,
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=979.0 * scale_x,
    y=888.0 * scale_y,
    width=348.0 * scale_x,
    height=94.0 * scale_y
)

# ---------------------------------------------------------------------------
# Uniform Scaling of Canvas Items
# ---------------------------------------------------------------------------
canvas.scale("all", 0, 0, scale_x, scale_y)

# ---------------------------------------------------------------------------
# Final Window Settings and Main Loop
# ---------------------------------------------------------------------------
window.resizable(False, False)
window.mainloop()
