from pathlib import Path
from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk  # Pillow is used for image processing

# ---------------------------------------------------------------------------
# Resource Paths Configuration
# ---------------------------------------------------------------------------
# Set up the paths to your asset directory. Adjust the asset directory as needed.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame0")


def relative_to_assets(path: str) -> Path:
    """
    Construct and return the full path to an asset file based on a relative path.

    :param path: The relative path to the asset file.
    :return: A Path object representing the full asset path.
    """
    return ASSETS_PATH / Path(path)


# ---------------------------------------------------------------------------
# Image Scaling Function
# ---------------------------------------------------------------------------
def scaled_photoimage(image_path: str, scale_x: float, scale_y: float) -> ImageTk.PhotoImage:
    """
    Open an image from the specified path, scale it according to the provided scaling
    factors (both horizontally and vertically), and convert it to a Tkinter-compatible
    PhotoImage.

    :param image_path: The path to the image file.
    :param scale_x: Scaling factor in the horizontal (x) direction.
    :param scale_y: Scaling factor in the vertical (y) direction.
    :return: A PhotoImage object representing the scaled image.
    """
    img = Image.open(image_path)  # Open the image file.
    orig_width, orig_height = img.size  # Get the original width and height.
    # Calculate the new size by multiplying the original dimensions with the scaling factors.
    new_size = (int(orig_width * scale_x), int(orig_height * scale_y))
    # Resize the image using high-quality resampling (LANCZOS method).
    img = img.resize(new_size, resample=Image.Resampling.LANCZOS)
    # Convert the PIL image to a Tkinter PhotoImage and return it.
    return ImageTk.PhotoImage(img)


# ---------------------------------------------------------------------------
# Window and Canvas Setup
# ---------------------------------------------------------------------------
# Define the original design dimensions of the layout.
orig_width = 1455
orig_height = 1041

# Define the new window dimensions (for example: 800x600; adjust as needed).
new_width = 800
new_height = 600

# Calculate scaling factors to convert original dimensions to new dimensions.
scale_x = new_width / orig_width
scale_y = new_height / orig_height

# Create the main Tkinter window and set its size and background color.
window = Tk()
window.geometry(f"{new_width}x{new_height}")  # Set the window size to the new dimensions.
window.configure(bg="#FFFFFF")  # Set the background color to white.

# Create a Canvas widget that uses the original design dimensions.
# This canvas will later be scaled so that all drawn items maintain their relative positions.
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=orig_height,
    width=orig_width,
    bd=0,  # No border
    highlightthickness=0,  # No highlight border
    relief="ridge"  # Flat appearance
)
# Place the canvas at the top-left corner of the window.
canvas.place(x=0, y=0)

# ---------------------------------------------------------------------------
# Canvas Background Drawing
# ---------------------------------------------------------------------------
# Draw a background rectangle on the canvas. The coordinates are based on the original design.
canvas.create_rectangle(
    0.0,  # x-coordinate of the top-left corner
    1.0,  # y-coordinate of the top-left corner
    235.0,  # x-coordinate of the bottom-right corner
    1042.0,  # y-coordinate of the bottom-right corner
    fill="#79BCF7",  # Fill color (light blue)
    outline=""  # No outline around the rectangle
)

# ---------------------------------------------------------------------------
# Button Creation and Placement
# ---------------------------------------------------------------------------
# For each button, we create a scaled image, instantiate a Button widget using that image,
# and then place it on the window with scaled coordinates and dimensions.

# ---------------------------
# Button 1: Setting Page Button
# ---------------------------
button_image_1 = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,  # No border for a flat look
    highlightthickness=0,  # No highlight border when focused
    command=lambda: print("button_1 clicked"),  # Command executed on click
    relief="flat"  # Flat appearance
)
button_1.place(
    x=1.0 * scale_x,  # Scaled x-coordinate for button position
    y=402.0 * scale_y,  # Scaled y-coordinate for button position
    width=235.0 * scale_x,  # Scaled width of the button
    height=100.0 * scale_y  # Scaled height of the button
)

# ---------------------------
# Button 2: View Page Button
# ---------------------------
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

# ---------------------------
# Button 3: Start Page Button
# ---------------------------
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

# ---------------------------
# Button 4: Upload Page Button
# ---------------------------
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

# ---------------------------
# Button 5: Home Page Button
# ---------------------------
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
# Canvas Image Addition
# ---------------------------------------------------------------------------
# Add a scaled image (for example, a course logo) to the canvas.
image_1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
canvas.create_image(
    215.0 * scale_x,  # Scaled x-coordinate for the image position
    1700.0 * scale_y,  # Scaled y-coordinate for the image position
    image=image_1  # The image to be drawn
)

# ---------------------------------------------------------------------------
# Drawing Additional Canvas Graphics
# ---------------------------------------------------------------------------
# Draw the main rectangular area on the canvas.
# Note: The coordinates here are given in original design values.
canvas.create_rectangle(
    257.0,  # Original x-coordinate for the top-left corner
    13.0,  # Original y-coordinate for the top-left corner
    1434.0,  # Original x-coordinate for the bottom-right corner
    1023.0,  # Original y-coordinate for the bottom-right corner
    fill="#DAEBF9",  # Fill color (light blue background for content area)
    outline=""  # No outline
)

# Scale all canvas items (graphics and text) using the computed scaling factors.
# This ensures that items drawn with original coordinates are properly scaled.
canvas.scale("all", 0, 0, scale_x, scale_y)

# ---------------------------------------------------------------------------
# Adding Text Elements to the Canvas
# ---------------------------------------------------------------------------
# Add the welcome text to the canvas.
welcome_text = "Welcome to Course Scheduling System"
welcome_x = 486.2366027832031 * scale_x  # Scaled x-coordinate for the welcome text.
welcome_y = 95.02468872070312 * scale_y  # Scaled y-coordinate for the welcome text.
welcome_font_size = int(30 * scale_y)  # Adjust font size based on vertical scaling.
canvas.create_text(
    welcome_x,
    welcome_y,
    anchor="nw",  # Anchor text at the top-left (northwest) corner.
    text=welcome_text,
    fill="#094478",  # Text color.
    font=("Roboto Black", welcome_font_size)
)

# Add a detailed description text to the canvas.
description_text = """                                                           System Description:

Make a compatible easy-to-use user interface within an application that allows 
the automated scheduling of university courses by the dean of a given department
from imported data.

User Instruction：
1. Go to the `Input Data` module to enter course, faculty, and classroom details.
2. Select `Generate Schedule` from the main dashboard to create the course schedule.
3. View the generated schedule in `View Schedule` for a detailed overview.
4. Use the `Conflict Resolution` module to address any detected issues.
5. Generate reports in the `Reports` module for printing or sharing.
6. Adjust system settings in the `Settings` module if needed.

For additional help, click the `Help` button in the navigation bar.
"""
desc_x = 366.4584655761719 * scale_x  # Scaled x-coordinate for the description text.
desc_y = 234.9700164794922 * scale_y  # Scaled y-coordinate for the description text.
desc_font_size = int(20 * scale_y)  # Adjust the font size based on vertical scaling.
canvas.create_text(
    desc_x,
    desc_y,
    anchor="nw",  # Anchor text at the top-left.
    text=description_text,
    fill="#094478",
    font=("Roboto Regular", desc_font_size)
)

# ---------------------------------------------------------------------------
# Final Window Settings and Main Loop
# ---------------------------------------------------------------------------
# Prevent the window from being resized by the user.
window.resizable(False, False)
# Start the Tkinter event loop to display the window.
window.mainloop()
