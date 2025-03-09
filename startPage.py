from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button
from PIL import Image, ImageTk  # Pillow is used for image processing
from tkinter import ttk

# ---------------------------------------------------------------------------
# Resource Paths Configuration
# ---------------------------------------------------------------------------
# Set up the asset path for the start page (frame2). Adjust the asset directory as needed.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame2")


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

# Calculate scaling factors for horizontal and vertical directions.
scale_x = new_width / orig_width
scale_y = new_height / orig_height

# Create the main Tkinter window and configure its size and background color.
window = Tk()
window.geometry(f"{new_width}x{new_height}")  # Set new window dimensions.
window.configure(bg="#FFFFFF")

# Create a Canvas widget using the original design dimensions.
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=orig_height,
    width=orig_width,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)  # Place the canvas at the top-left corner.

# ---------------------------------------------------------------------------
# Canvas Background Elements
# ---------------------------------------------------------------------------
# Draw a left sidebar background rectangle using original coordinates.
canvas.create_rectangle(
    0.0,  # x-coordinate of top-left
    1.0,  # y-coordinate of top-left
    235.0,  # x-coordinate of bottom-right
    1042.0,  # y-coordinate of bottom-right
    fill="#79BCF7",  # Fill color (light blue)
    outline=""  # No outline
)

# ---------------------------------------------------------------------------
# Sidebar Buttons (Left Side)
# ---------------------------------------------------------------------------
# Create and place sidebar buttons. Coordinates and dimensions are scaled.

# Button 1 (e.g., for navigation): Uses the scaled image.
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

# ---------------------------------------------------------------------------
# Canvas Image (Logo or Additional Graphic)
# ---------------------------------------------------------------------------
# Add a canvas image using a scaled image. Note that the coordinates here are manually scaled.
image_1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
canvas.create_image(
    215.0 * scale_x,  # Scaled x-coordinate for the image position
    1700.0 * scale_y,  # Scaled y-coordinate for the image position
    image=image_1  # The image to be drawn
)

# ---------------------------------------------------------------------------
# Right Side Main Background
# ---------------------------------------------------------------------------
# Draw the main background rectangle on the right side using original coordinates.
canvas.create_rectangle(
    918.0,  # Original x-coordinate (top-left)
    1.0,  # Original y-coordinate (top-left)
    1458.0,  # Original x-coordinate (bottom-right)
    1042.0,  # Original y-coordinate (bottom-right)
    fill="#DAEBF9",  # Fill color
    outline=""
)

# ---------------------------------------------------------------------------
# Right Side Buttons (Upper Area)
# ---------------------------------------------------------------------------
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
    x=942.0 * scale_x,  # Scaled x-coordinate
    y=36.0 * scale_y,  # Scaled y-coordinate
    width=206.0 * scale_x,  # Scaled width
    height=101.0 * scale_y  # Scaled height
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
    x=1224.0 * scale_x,
    y=36.0 * scale_y,
    width=200.0 * scale_x,
    height=112.0 * scale_y
)

# ---------------------------------------------------------------------------
# Canvas Text Items (Status and Conflict Summary)
# ---------------------------------------------------------------------------
# Create a text item for the status label.
canvas.create_text(
    2000.0 * scale_x,  # Scaled x-coordinate
    270.0 * scale_y,  # Scaled y-coordinate
    anchor="nw",
    text="Status:",
    fill="#094478",
    font=("Jomolhari Regular", int(20 * scale_y))
)

# Draw a white rectangle for the conflict summary area.
canvas.create_rectangle(
    935.0,  # Original x-coordinate for top-left
    339.0,  # Original y-coordinate for top-left
    1435.0,  # Original x-coordinate for bottom-right
    818.0,  # Original y-coordinate for bottom-right
    fill="#FFFFFF",
    outline=""
)

# Create a text item for the conflict summary label.
canvas.create_text(
    1064.0,  # Original x-coordinate
    339.0,  # Original y-coordinate
    anchor="nw",
    text="Conflict  Summary：",
    fill="#094478",
    font=("Jomolhari Regular", int(20 * -1))
    # Note: negative font size may be used to indicate a specific style; adjust as needed.
)

# Additional text item for status info.
canvas.create_text(
    1800.0 * scale_x,
    350.0 * scale_y,
    anchor="nw",
    text="status info",
    fill="#000000",
    font=("Jomolhari Regular", int(15 * scale_y))
)

# ---------------------------------------------------------------------------
# Right Side Buttons (Lower Area)
# ---------------------------------------------------------------------------
# Button 8
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
    x=1206.0 * scale_x,
    y=737.0 * scale_y,
    width=200.0 * scale_x,
    height=65.0 * scale_y
)

# Button 9
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
    x=972.0 * scale_x,
    y=741.0 * scale_y,
    width=200.0 * scale_x,
    height=61.0 * scale_y
)

# Button 10
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
    x=942.0 * scale_x,
    y=893.0 * scale_y,
    width=200.0 * scale_x,
    height=101.0 * scale_y
)

# Button 11
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
    x=1224.0 * scale_x,
    y=893.0 * scale_y,
    width=200.0 * scale_x,
    height=101.0 * scale_y
)

# Draw horizontal separator rectangles using original coordinates.
canvas.create_rectangle(
    916.9881591796875,  # Original x-coordinate
    153.47650146484375,  # Original y-coordinate
    1455.0114135742188,  # Original x-coordinate
    154.47650146484375,  # Original y-coordinate
    fill="#094478",
    outline=""
)

canvas.create_rectangle(
    918.0,
    314.0,
    1456.0232543945312,
    315.0,
    fill="#094478",
    outline=""
)

# ============================== #
#        table      #
# ============================== #

# Define column names
columns = ("Course ID", "Course Name", "Time", "Room", "Professor", "Days")
tree = ttk.Treeview(window, columns=columns, show="headings")

# Set column headers
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=30, anchor="center")

# Course Data
courses = [
    ("CS 115", "Intro to Programming", "9:00 AM - 10:30 AM", "Room 341", "Dr. Echo", "Mon, Wed"),
    ("CS 310", "Data Structures", "10:45 AM - 12:15 PM", "Room 243", "Dr. Juliet", "Tue, Thu"),
    ("CS 382", "Algorithms", "1:00 PM - 2:30 PM", "Room 341", "Dr. Lima", "Mon, Wed, Fri"),
    ("CS 419", "Artificial Intelligence", "2:45 PM - 4:15 PM", "Room 134", "Dr. Lima", "Tue, Thu"),
    ("CS 438", "Machine Learning", "4:30 PM - 6:00 PM", "Room 241", "Dr. November", "Mon, Wed"),
    ("CS 452", "Computer Security", "6:15 PM - 7:45 PM", "Room 244", "Dr. Foxtrot", "Tue, Thu"),
    ("CS 501", "Advanced Programming", "8:00 AM - 9:30 AM", "Room 244", "Dr. November", "Mon, Wed"),
    ("CS 558", "Cryptography", "9:45 AM - 11:15 AM", "Room 244", "Dr. Hotel", "Tue, Thu"),
    ("CS 572", "Deep Learning", "11:30 AM - 1:00 PM", "Room 244", "Dr. Dog", "Mon, Wed, Fri"),
]

# Insert data into the table
for course in courses:
    tree.insert("", "end", values=course)

# Adding Scroll Bars
tree_scroll = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scroll.set)

# Put the Treeview into a Canvas
tree_window = canvas.create_window(240, 9, width=671, height=1026, anchor="nw", window=tree)

# 绑定滚动条到表格
tree_scroll.place(x=500, y=6, height=1025)

# ---------------------------------------------------------------------------
# Apply Uniform Scaling to Canvas Items
# ---------------------------------------------------------------------------
# For canvas items created with original coordinates (such as rectangles and text items)
# that were not already manually scaled, apply a uniform scaling transformation.
canvas.scale("all", 0, 0, scale_x, scale_y)

# ---------------------------------------------------------------------------
# Final Window Settings and Main Loop
# ---------------------------------------------------------------------------
# Prevent the window from being resized by the user.
window.resizable(False, False)
# Start the Tkinter event loop.
window.mainloop()
