from pathlib import Path
from tkinter import Tk, Canvas, StringVar
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow is used for image processing

# ---------------------------------------------------------------------------
# Resource Paths Configuration
# ---------------------------------------------------------------------------
# Set up the asset path for the conflict page (frame3). Adjust the path as needed.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame3")


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
    orig_width, orig_height = img.size  # Retrieve original image dimensions.
    new_size = (int(orig_width * scale_x), int(orig_height * scale_y))  # Calculate new size.
    # Resize the image using high-quality LANCZOS resampling.
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

# Calculate scaling factors for horizontal and vertical directions.
scale_x = new_width / orig_width
scale_y = new_height / orig_height

# Create the main Tkinter window and configure its size and background.
window = Tk()
window.geometry(f"{new_width}x{new_height}")
window.configure(bg="#FFFFFF")

# Create a Canvas widget using the original dimensions.
# Canvas items (e.g., rectangles and text) will be defined with original coordinates.
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=orig_height,
    width=orig_width,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# ---------------------------------------------------------------------------
# Canvas Background and Graphics (Original Coordinates)
# ---------------------------------------------------------------------------
# Draw a right-side background rectangle.
canvas.create_rectangle(
    1070.0,  # x1 (top-left)
    0.0,  # y1 (top-left)
    1455.0,  # x2 (bottom-right)
    1041.0,  # y2 (bottom-right)
    fill="#79BCF7",
    outline=""
)

# Create a title text "Conflict" using original coordinates.
canvas.create_text(
    500.0,  # x-coordinate
    20.0,  # y-coordinate
    anchor="nw",
    text="Conflict",
    fill="#094478",
    font=("Jomolhari Regular", 15)  # Font size will be scaled later.
)

# Draw a rectangle for the conflict summary area.
canvas.create_rectangle(
    34.0,  # x1 (top-left)
    104.0,  # y1 (top-left)
    1034.0,  # x2 (bottom-right)
    194.0,  # y2 (bottom-right)
    fill="#DAEBF9",
    outline=""
)

# Add descriptive text for conflict details.
canvas.create_text(
    42.0,  # x-coordinate
    140.0,  # y-coordinate
    anchor="nw",
    text="Conflict 1",
    fill="#094478",
    font=("Jomolhari Regular", 8)
)
canvas.create_text(
    141.0,  # x-coordinate
    140.0,  # y-coordinate
    anchor="nw",
    text="Courses and professors",
    fill="#094478",
    font=("Jomolhari Regular", 8)
)
canvas.create_text(
    400.0,  # x-coordinate
    140.0,  # y-coordinate
    anchor="nw",
    text="conflict reason",
    fill="#094478",
    font=("Jomolhari Regular", 8)
)

# ---------------------------------------------------------------------------
# Sidebar Buttons (Non-canvas Widgets)
# ---------------------------------------------------------------------------
# For buttons (using ttk.Button), we load scaled images and place them with scaled coordinates.

button_image_1 = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
button_1 = ttk.Button(window, image=button_image_1, command=lambda: print("button_1 clicked"))
button_1.place(
    x=1163.0 * scale_x,  # Scaled x-coordinate
    y=47.5 * scale_y,  # Scaled y-coordinate
    width=201.0 * scale_x,  # Scaled width
    height=83.0 * scale_y  # Scaled height
)

button_image_2 = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
button_2 = ttk.Button(window, image=button_image_2, command=lambda: print("button_2 clicked"))
button_2.place(
    x=1163.0 * scale_x,
    y=217.0 * scale_y,
    width=201.0 * scale_x,
    height=83.0 * scale_y
)

button_image_3 = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
button_3 = ttk.Button(window, image=button_image_3, command=lambda: print("button_3 clicked"))
button_3.place(
    x=1163.0 * scale_x,
    y=398.0 * scale_y,
    width=201.0 * scale_x,
    height=83.0 * scale_y
)

button_image_4 = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
button_4 = ttk.Button(window, image=button_image_4, command=lambda: print("button_4 clicked"))
button_4.place(
    x=1163.0 * scale_x,
    y=587.0 * scale_y,
    width=201.0 * scale_x,
    height=83.0 * scale_y
)

# ---------------------------------------------------------------------------
# Combobox Widgets for Conflict Resolution
# ---------------------------------------------------------------------------
# Define dropdown options.
options_5 = ["chooes A", "chooes B", "choose C"]
options_6 = ["choose X", "choose Y", "choose Z"]

# Create StringVar for dropdowns.
dropdown_var_5 = StringVar()
dropdown_var_6 = StringVar()

# Create and place Combobox 5 (for room change) with scaled coordinates.
dropdown_5 = ttk.Combobox(window, textvariable=dropdown_var_5, values=options_5, state="readonly")
dropdown_5.set("room")
dropdown_5.place(
    x=638.0 * scale_x,
    y=128.0 * scale_y,
    width=111.0 * scale_x,
    height=50.0 * scale_y
)
dropdown_5.bind("<<ComboboxSelected>>", lambda e: print(f"Dropdown 5 choose: {dropdown_var_5.get()}"))

# Create and place Combobox 6 (for time change) with scaled coordinates.
dropdown_6 = ttk.Combobox(window, textvariable=dropdown_var_6, values=options_6, state="readonly")
dropdown_6.set("time")
dropdown_6.place(
    x=823.0 * scale_x,
    y=128.0 * scale_y,
    width=111.0 * scale_x,
    height=50.0 * scale_y
)
dropdown_6.bind("<<ComboboxSelected>>", lambda e: print(f"Dropdown 6 choose: {dropdown_var_6.get()}"))

# ---------------------------------------------------------------------------
# Apply Uniform Scaling to Canvas Items
# ---------------------------------------------------------------------------
# Scale all canvas items (rectangles, texts, etc.) using the computed scaling factors.
canvas.scale("all", 0, 0, scale_x, scale_y)

# ---------------------------------------------------------------------------
# Final Window Settings and Main Loop
# ---------------------------------------------------------------------------
# Prevent the window from being resizable and start the Tkinter event loop.
window.resizable(False, False)
window.mainloop()
