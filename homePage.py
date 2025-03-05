
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk


class HomePage():

    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.geometry("1000x600")
        self.root.title("COURSE")
        

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\fuzhe\OneDrive\Desktop\cs hw\gui\assets\frame0")

        #self.canvas = Canvas(self.root, height = 1000, width = 600, bg = "#FF8000")
        #self.canvas.pack(fill = "both", expand = False)

        self.mainFrame = tk.Frame(self.root, bg = "#79BCF7")
        self.mainFrame.pack(fill = "both", expand = True)

        self.fillWindow()

        
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def fillWindow(self):

        
        
        image = Image.open(self.relative_to_assets("button_1.png"))
        self.button_image_1 = ImageTk.PhotoImage(image)
        #self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=1.0,
            y=402.0,
            width=235.0,
            height=100.0
        )
        
        image = Image.open(self.relative_to_assets("button_2.png"))
        self.button_image_2 = ImageTk.PhotoImage(image)
        #self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=0.0,
            y=302.0,
            width=235.0,
            height=100.0
        )
        image = Image.open(self.relative_to_assets("button_3.png"))
        self.button_image_3 = ImageTk.PhotoImage(image)
        #self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=0.0,
            y=202.0,
            width=235.0,
            height=100.0
        )
        image = Image.open(self.relative_to_assets("button_4.png"))
        self.button_image_4 = ImageTk.PhotoImage(image)
        #self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=0.0,
            y=102.0,
            width=235.0,
            height=100.0
        )
        image = Image.open(self.relative_to_assets("button_5.png"))
        self.button_image_5 = ImageTk.PhotoImage(image)
        #self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=1.5,
            width=235.0,
            height=100.0
        )
        image = Image.open(self.relative_to_assets("image_1.png"))
        self.image_image_1 = ImageTk.PhotoImage(image)
        #self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            118.0,
            993.0,
            image=self.image_image_1
        )
        self.canvas.create_rectangle(
            257.0,
            13.0,
            1434.0,
            1023.0,
            fill="#DAEBF9",
            outline="")

        self.canvas.create_text(
            486.2366027832031,
            95.02468872070312,
            anchor="nw",
            text="Welcome to Course Scheduling System",
            fill="#094478",
            font=("Roboto Black", 40 * -1)
        )

        self.canvas.create_text(
            366.4584655761719,
            234.9700164794922,
            anchor="nw",
            text="""                                                           System Description:

        Make a compatible easy-to-use user interface within an application that allows 
        the automated scheduling of university courses by the dean of a given department
        from imported data.

        User Instruction
        1. Go to the `Input Data` module to enter course, faculty, and classroom details.
        2. Select `Generate Schedule` from the main dashboard to create the course schedule.
        3. View the generated schedule in `View Schedule` for a detailed overview.
        4. Use the `Conflict Resolution` module to address any detected issues.
        5. Generate reports in the `Reports` module for printing or sharing.
        6. Adjust system settings in the `Settings` module if needed.

        For additional help, click the `Help` button in the navigation bar.
        """,
            fill="#094478",
            font=("Roboto Regular", 24 * -1)
        )


