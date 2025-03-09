from pathlib import Path
from tkinter import Tk, Canvas, Button
from tkinter.filedialog import askopenfilename
import os
from PIL import Image, ImageTk  # Pillow is used for image processing

# ---------------------------------------------------------------------------
# Resource Paths Configuration
# ---------------------------------------------------------------------------
# Set up the paths to your asset directory (for upload page assets).
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame1")


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
    orig_width, orig_height = img.size  # Get the original image dimensions.
    new_size = (int(orig_width * scale_x), int(orig_height * scale_y))  # Calculate new dimensions.
    # Resize the image using high-quality resampling (LANCZOS).
    img = img.resize(new_size, resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


# ---------------------------------------------------------------------------
# Window and Canvas Setup
# ---------------------------------------------------------------------------
# Define original design dimensions.
orig_width = 1455
orig_height = 1041

# Define new window dimensions (for example: 800x600; adjust as needed).
new_width = 800
new_height = 600

# Calculate scaling factors for the horizontal and vertical directions.
scale_x = new_width / orig_width
scale_y = new_height / orig_height

# Create the main window with the new dimensions and set the background color.
window = Tk()
window.geometry(f"{new_width}x{new_height}")
window.configure(bg="#FFFFFF")

# Create a Canvas widget using the original design dimensions.
# This canvas will later be scaled so that all drawn items maintain their relative positions.
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
# Canvas Background Drawing
# ---------------------------------------------------------------------------
# Draw a background rectangle on the canvas using original coordinates.
canvas.create_rectangle(
    0.0,  # x-coordinate of the top-left corner
    1.0,  # y-coordinate of the top-left corner
    235.0,  # x-coordinate of the bottom-right corner
    1042.0,  # y-coordinate of the bottom-right corner
    fill="#79BCF7",  # Fill color (light blue)
    outline=""  # No outline
)

# ---------------------------------------------------------------------------
# Button Creation and Placement (Left Sidebar)
# ---------------------------------------------------------------------------
# For each button on the sidebar, we load a scaled image and then place the button
# with coordinates and dimensions multiplied by the scaling factors.

# Button 1: (e.g., "Setting Page" button)
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
    x=1.0 * scale_x,  # Scaled x-coordinate
    y=402.0 * scale_y,  # Scaled y-coordinate
    width=235.0 * scale_x,  # Scaled width
    height=100.0 * scale_y  # Scaled height
)

# Button 2: (e.g., "View Page" button)
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

# Button 3: (e.g., "Start Page" button)
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

# Button 4: (e.g., "Upload Page" button)
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

# Button 5: (e.g., "Home Page" button)
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
# File Upload Functionality and Text Display
# ---------------------------------------------------------------------------
# Create a canvas text item to display the selected file name.
selected_file_text_id = canvas.create_text(
    481.0 * scale_x,  # Scaled x-coordinate for the text position
    299.0 * scale_y,  # Scaled y-coordinate for the text position
    anchor="nw",
    text="File name",
    fill="#094478",
    font=("Roboto Black", int(20 * scale_y))
)


def upload_file():
    """
    Open a file dialog to select a file, and update the canvas text with the chosen file's name.
    """
    file_path = askopenfilename(
        title="选择文件",
        filetypes=(("所有文件", "*.*"), ("文本文件", "*.txt"), ("Excel文件", "*.xlsx"))
    )
    if file_path:
        selected_name = os.path.basename(file_path)
        print("选择的文件路径:", file_path)
        canvas.itemconfig(selected_file_text_id, text=selected_name)


# ---------------------------------------------------------------------------
# Button 6: File Upload Button (Large Area)
# ---------------------------------------------------------------------------
# This button covers a large area on the canvas to trigger file uploads.
button_image_6 = scaled_photoimage(str(relative_to_assets("button_6.png")), scale_x, scale_y)
button_6 = Button(
    window,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=upload_file,
    relief="flat"
)
button_6.place(
    x=250.0 * scale_x,  # Scaled x-coordinate
    y=25.0 * scale_y,  # Scaled y-coordinate
    width=1177.0 * scale_x,  # Scaled width
    height=211.0 * scale_y  # Scaled height
)

# ---------------------------------------------------------------------------
# Additional Canvas Text Items
# ---------------------------------------------------------------------------
# Create extra text items on the canvas at scaled positions.
canvas.create_text(
    481.0 * scale_x,
    452.0 * scale_y,
    anchor="nw",
    text="File name",
    fill="#094478",
    font=("Roboto Black", int(20 * scale_y))
)

canvas.create_text(
    482.0 * scale_x,
    615.0 * scale_y,
    anchor="nw",
    text="File name",
    fill="#094478",
    font=("Roboto Black", int(20 * scale_y))
)

# ---------------------------------------------------------------------------
# Additional Images on the Canvas
# ---------------------------------------------------------------------------
# Add further images (e.g., icons or decorative elements) to the canvas with scaling.


image_1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
canvas.create_image(
    215.0 * scale_x,  # Scaled x-coordinate for the image position
    1700.0 * scale_y,  # Scaled y-coordinate for the image position
    image=image_1  # The image to be drawn
)

# Image 2:
image_2 = scaled_photoimage(str(relative_to_assets("image_2.png")), scale_x, scale_y)
canvas.create_image(
    372.0 * scale_x,
    322.0 * scale_y,
    image=image_2
)

# Image 3:
image_3 = scaled_photoimage(str(relative_to_assets("image_3.png")), scale_x, scale_y)
canvas.create_image(
    372.0 * scale_x,
    467.0 * scale_y,
    image=image_3
)

# Image 4:
image_4 = scaled_photoimage(str(relative_to_assets("image_4.png")), scale_x, scale_y)
canvas.create_image(
    372.0 * scale_x,
    633.0 * scale_y,
    image=image_4
)

# Image 5:
image_5 = scaled_photoimage(str(relative_to_assets("image_5.png")), scale_x, scale_y)
canvas.create_image(
    1239.0 * scale_x,
    317.0 * scale_y,
    image=image_5
)

# ---------------------------------------------------------------------------
# Scaling All Canvas Items
# ---------------------------------------------------------------------------
# For canvas items created with original coordinates that have not been pre-scaled,
# apply a uniform scaling transformation to ensure consistency.
canvas.scale("all", 0, 0, scale_x, scale_y)

# ---------------------------------------------------------------------------
# Final Window Settings and Main Loop
# ---------------------------------------------------------------------------
# Prevent the window from being resized and start the Tkinter event loop.
window.resizable(False, False)
window.mainloop()
