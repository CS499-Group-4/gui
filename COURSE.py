import tkinter as tk
from tkinter import Canvas, Button, Entry, Label, ttk
from tkinter.filedialog import askopenfilename
from pathlib import Path
from PIL import Image, ImageTk
import os

# ---------------------------
# Common helper functions and resource paths
# ---------------------------
OUTPUT_PATH = Path(__file__).parent
# Other pages can be adjusted as needed
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def scaled_photoimage(image_path: str, scale_x: float, scale_y: float) -> ImageTk.PhotoImage:
    img = Image.open(image_path)
    orig_width, orig_height = img.size
    new_size = (int(orig_width * scale_x), int(orig_height * scale_y))
    img = img.resize(new_size, resample=Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# ---------------------------
# Main application: manage the jump of each page# ---------------------------
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("course")
        self.geometry("800x600")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (homePage, StartPage, UploadPage, SettingPage, ConflictPage, ViewPage):
            page = F(parent=container, controller=self)
            self.frames[F] = page
            page.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(homePage)
    
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

# ---------------------------
# Home page: homePage
# ---------------------------
class homePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        orig_width = 1455
        orig_height = 1041
        new_width = 800
        new_height = 600
        scale_x = new_width / orig_width
        scale_y = new_height / orig_height

        canvas = Canvas(self, bg="#FFFFFF", height=orig_height, width=orig_width,
                        bd=0, highlightthickness=0, relief="ridge")
        canvas.pack(fill="both", expand=True)
        
        canvas.create_rectangle(0.0, 1.0, 235.0, 1042.0, fill="#79BCF7", outline="")

# Navigation button: switch page
        btn1_img = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
        btn1 = Button(self, image=btn1_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(SettingPage), relief="flat")
        btn1.image = btn1_img
        btn1.place(x=1.0 * scale_x, y=402.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn2_img = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
        btn2 = Button(self, image=btn2_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(ViewPage), relief="flat")
        btn2.image = btn2_img
        btn2.place(x=0.0 * scale_x, y=302.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn3_img = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
        btn3 = Button(self, image=btn3_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(StartPage), relief="flat")
        btn3.image = btn3_img
        btn3.place(x=0.0 * scale_x, y=202.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn4_img = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
        btn4 = Button(self, image=btn4_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(UploadPage), relief="flat")
        btn4.image = btn4_img
        btn4.place(x=0.0 * scale_x, y=102.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn5_img = scaled_photoimage(str(relative_to_assets("button_5.png")), scale_x, scale_y)
        btn5 = Button(self, image=btn5_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(homePage), relief="flat")
        btn5.image = btn5_img
        btn5.place(x=0.0 * scale_x, y=1.5 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        img1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
        canvas.create_image(215.0 * scale_x, 1700.0 * scale_y, image=img1)
        canvas.image = img1
        canvas.create_rectangle(257.0, 13.0, 1434.0, 1023.0, fill="#DAEBF9", outline="")
        canvas.scale("all", 0, 0, scale_x, scale_y)
        canvas.create_text(486.2366 * scale_x, 95.0247 * scale_y,
                           anchor="nw", text="Welcome to Course Scheduling System",
                           fill="#094478", font=("Roboto Black", int(30 * scale_y)))
        desc_text = (
            "                                                           System Description:\n\n"
            "Make a compatible easy-to-use user interface within an application that allows\n"
            "the automated scheduling of university courses by the dean of a given department\n"
            "from imported data.\n\n"
            "User Instruction：\n"
            "1. Go to the `Input Data` module to enter course, faculty, and classroom details.\n"
            "2. Select `Generate Schedule` from the main dashboard to create the course schedule.\n"
            "3. View the generated schedule in `View Schedule` for a detailed overview.\n"
            "4. Use the `Conflict Resolution` module to address any detected issues.\n"
            "5. Generate reports in the `Reports` module for printing or sharing.\n"
            "6. Adjust system settings in the `Settings` module if needed.\n\n"
            "For additional help, click the `Help` button in the navigation bar."
        )
        canvas.create_text(366.4585 * scale_x, 234.97 * scale_y,
                           anchor="nw", text=desc_text, fill="#094478",
                           font=("Roboto Regular", int(20 * scale_y)))

# ---------------------------
# UploadPage
# ---------------------------
class UploadPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        orig_width = 1455
        orig_height = 1041
        new_width = 800
        new_height = 600
        scale_x = new_width / orig_width
        scale_y = new_height / orig_height

        self.canvas = Canvas(self, bg="#FFFFFF", height=orig_height, width=orig_width,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        
        self.canvas.create_rectangle(0.0, 1.0, 235.0, 1042.0, fill="#79BCF7", outline="")

        # Navigation button: switch page
        btn1_img = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
        btn1 = Button(self, image=btn1_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(SettingPage), relief="flat")
        btn1.image = btn1_img
        btn1.place(x=1.0 * scale_x, y=402.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn2_img = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
        btn2 = Button(self, image=btn2_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(ViewPage), relief="flat")
        btn2.image = btn2_img
        btn2.place(x=0.0 * scale_x, y=302.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn3_img = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
        btn3 = Button(self, image=btn3_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(StartPage), relief="flat")
        btn3.image = btn3_img
        btn3.place(x=0.0 * scale_x, y=202.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn4_img = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
        btn4 = Button(self, image=btn4_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(UploadPage), relief="flat")
        btn4.image = btn4_img
        btn4.place(x=0.0 * scale_x, y=102.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn5_img = scaled_photoimage(str(relative_to_assets("button_5.png")), scale_x, scale_y)
        btn5 = Button(self, image=btn5_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(homePage), relief="flat")
        btn5.image = btn5_img
        btn5.place(x=0.0 * scale_x, y=1.5 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
       # File upload part: display the selected file name
        self.selected_file_text_id = self.canvas.create_text(
            481.0 * scale_x, 299.0 * scale_y,
            anchor="nw", text="File name", fill="#094478",
            font=("Roboto Black", int(20 * scale_y))
        )
        
        def upload_file():
            file_path = askopenfilename(
                title="choose file",
                filetypes=(("all file", "*.*"), ("text file", "*.txt"), ("Excel file", "*.xlsx"))
            )
            if file_path:
                selected_name = os.path.basename(file_path)
                print("choosed file path:", file_path)
                self.canvas.itemconfig(self.selected_file_text_id, text=selected_name)
        
        # File upload button: covers a large area, click to trigger upload
        btn6_img = scaled_photoimage(str(relative_to_assets("button_6.png")), scale_x, scale_y)
        btn6 = Button(self, image=btn6_img, borderwidth=0, highlightthickness=0,
                      command=upload_file, relief="flat")
        btn6.image = btn6_img
        btn6.place(x=250.0 * scale_x, y=25.0 * scale_y, width=1177.0 * scale_x, height=211.0 * scale_y)
        
        self.canvas.create_text(481.0 * scale_x, 452.0 * scale_y, anchor="nw",
                           text="File name", fill="#094478", font=("Roboto Black", int(20 * scale_y)))
        self.canvas.create_text(482.0 * scale_x, 615.0 * scale_y, anchor="nw",
                           text="File name", fill="#094478", font=("Roboto Black", int(20 * scale_y)))
        img1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
        self.canvas.create_image(215.0 * scale_x, 1700.0 * scale_y, image=img1)
        self.canvas.image = img1
        img2 = scaled_photoimage(str(relative_to_assets("image_2.png")), scale_x, scale_y)
        self.canvas.create_image(372.0 * scale_x, 322.0 * scale_y, image=img2)
        img3 = scaled_photoimage(str(relative_to_assets("image_3.png")), scale_x, scale_y)
        self.canvas.create_image(372.0 * scale_x, 467.0 * scale_y, image=img3)
        img4 = scaled_photoimage(str(relative_to_assets("image_4.png")), scale_x, scale_y)
        self.canvas.create_image(372.0 * scale_x, 633.0 * scale_y, image=img4)
        img5 = scaled_photoimage(str(relative_to_assets("image_5.png")), scale_x, scale_y)
        self.canvas.create_image(1239.0 * scale_x, 317.0 * scale_y, image=img5)
        
        self.canvas.scale("all", 0, 0, scale_x, scale_y)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame2")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        orig_width, orig_height = 1455, 1041
        new_width, new_height = 800, 600
        scale_x, scale_y = new_width / orig_width, new_height / orig_height

        canvas = Canvas(self, bg="#FFFFFF", height=orig_height, width=orig_width,
                        bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        
        canvas.create_rectangle(0.0, 1.0, 235.0, 1042.0, fill="#79BCF7", outline="")
        
        # Navigation Buttons
        btn1_img = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
        btn1 = Button(self, image=btn1_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(SettingPage), relief="flat")
        btn1.image = btn1_img
        btn1.place(x=1.0 * scale_x, y=402.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn2_img = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
        btn2 = Button(self, image=btn2_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(ViewPage), relief="flat")
        btn2.image = btn2_img
        btn2.place(x=0.0 * scale_x, y=302.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn3_img = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
        btn3 = Button(self, image=btn3_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(StartPage), relief="flat")
        btn3.image = btn3_img
        btn3.place(x=0.0 * scale_x, y=202.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn4_img = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
        btn4 = Button(self, image=btn4_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(UploadPage), relief="flat")
        btn4.image = btn4_img
        btn4.place(x=0.0 * scale_x, y=102.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn5_img = scaled_photoimage(str(relative_to_assets("button_5.png")), scale_x, scale_y)
        btn5 = Button(self, image=btn5_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(homePage), relief="flat")
        btn5.image = btn5_img
        btn5.place(x=0.0 * scale_x, y=1.5 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        # Canvas（Logo）
        image_1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
        canvas.create_image(215.0 * scale_x, 1700.0 * scale_y, image=image_1)
        
        canvas.create_rectangle(918.0, 1.0, 1458.0, 1042.0, fill="#DAEBF9", outline="")
        
        # Upper right button
        button_image_6 = scaled_photoimage(str(relative_to_assets("button_6.png")), scale_x, scale_y)
        button_6 = Button(self, image=button_image_6, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_6 clicked"), relief="flat")
        button_6.image = button_image_6
        button_6.place(x=942.0 * scale_x, y=36.0 * scale_y, width=206.0 * scale_x, height=101.0 * scale_y)
        
        button_image_7 = scaled_photoimage(str(relative_to_assets("button_7.png")), scale_x, scale_y)
        button_7 = Button(self, image=button_image_7, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_7 clicked"), relief="flat")
        button_7.image = button_image_7
        button_7.place(x=1224.0 * scale_x, y=36.0 * scale_y, width=200.0 * scale_x, height=112.0 * scale_y)
        
       # Status and conflict summary text
        canvas.create_text(2000.0 * scale_x, 270.0 * scale_y, anchor="nw",
                           text="Status:", fill="#094478",
                           font=("Jomolhari Regular", int(20 * scale_y)))
        canvas.create_rectangle(935.0, 339.0, 1435.0, 818.0, fill="#FFFFFF", outline="")
        canvas.create_text(1064.0, 339.0, anchor="nw",
                           text="Conflict  Summary：", fill="#094478",
                           font=("Jomolhari Regular", int(20 * -1)))
        canvas.create_text(1800.0 * scale_x, 350.0 * scale_y, anchor="nw",
                           text="status info", fill="#000000",
                           font=("Jomolhari Regular", int(15 * scale_y)))
        
        # Lower right button
        button_image_8 = scaled_photoimage(str(relative_to_assets("button_8.png")), scale_x, scale_y)
        button_8 = Button(self, image=button_image_8, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_8 clicked"), relief="flat")
        button_8.image = button_image_8
        button_8.place(x=1206.0 * scale_x, y=737.0 * scale_y, width=200.0 * scale_x, height=65.0 * scale_y)
        
        button_image_9 = scaled_photoimage(str(relative_to_assets("button_9.png")), scale_x, scale_y)
        button_9 = Button(self, image=button_image_9, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(ConflictPage), relief="flat")
        button_9.image = button_image_9
        button_9.place(x=972.0 * scale_x, y=741.0 * scale_y, width=200.0 * scale_x, height=61.0 * scale_y)
        
        button_image_10 = scaled_photoimage(str(relative_to_assets("button_10.png")), scale_x, scale_y)
        button_10 = Button(self, image=button_image_10, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_10 clicked"), relief="flat")
        button_10.image = button_image_10
        button_10.place(x=942.0 * scale_x, y=893.0 * scale_y, width=200.0 * scale_x, height=101.0 * scale_y)
        
        button_image_11 = scaled_photoimage(str(relative_to_assets("button_11.png")), scale_x, scale_y)
        button_11 = Button(self, image=button_image_11, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_11 clicked"), relief="flat")
        button_11.image = button_image_11
        button_11.place(x=1224.0 * scale_x, y=893.0 * scale_y, width=200.0 * scale_x, height=101.0 * scale_y)
        
        # Divider
        canvas.create_rectangle(916.98816, 153.4765, 1455.01141, 154.4765, fill="#094478", outline="")
        canvas.create_rectangle(918.0, 314.0, 1456.02325, 315.0, fill="#094478", outline="")
        
        # Table section
        columns = ("Course ID", "Course Name", "Time", "Room", "Professor", "Days")
        tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=30, anchor="center")
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
        for course in courses:
            tree.insert("", "end", values=course)
        tree_scroll = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=tree_scroll.set)
        canvas.create_window(240, 9, width=671, height=1026, anchor="nw", window=tree)
        tree_scroll.place(x=500, y=6, height=1025)
        
        canvas.scale("all", 0, 0, scale_x, scale_y)

class SettingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame5")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        orig_width, orig_height = 1455, 1041
        new_width, new_height = 800, 600
        scale_x, scale_y = new_width / orig_width, new_height / orig_height
        
        canvas = Canvas(self, bg="#FFFFFF", height=orig_height, width=orig_width,
                        bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        
        canvas.create_rectangle(0.0, 1.0, 235.0, 1042.0, fill="#79BCF7", outline="")
        
        canvas.create_rectangle(296.0, 41.0, 1403.0, 148.0, fill="#DAEBF9", outline="")
        
        canvas.create_text(323.0, 76.0, anchor="nw", text="Font Setting:",
                           fill="#094478", font=("Jomolhari Regular", 10))
        
        canvas.create_rectangle(289.0, 502.0, 1396.0, 609.0, fill="#DAEBF9", outline="")
        canvas.create_rectangle(289.0, 697.0, 1403.0, 804.0, fill="#DAEBF9", outline="")
        
        canvas.create_rectangle(296.0, 239.0, 1403.0, 346.0, fill="#DAEBF9", outline="")
        canvas.create_text(323.0, 274.0, anchor="nw", text="Font Size:",
                           fill="#094478", font=("Jomolhari Regular", 10))
        
        canvas.create_text(296.0, 430.0, anchor="nw", text="Default display mode of class schedule: ",
                           fill="#094478", font=("Jomolhari Regular", 16))
        
        canvas.create_rectangle(502.0, 293.00000002561853, 1350.0000066752837, 298.0,
                                fill="#094478", outline="")
        
        canvas.create_text(330.0, 735.0, anchor="nw", text="Font Setting:",
                           fill="#094478", font=("Jomolhari Regular", 24))
        
        image_1 = scaled_photoimage(str(relative_to_assets("image_1.png")), scale_x, scale_y)
        canvas.create_image(215.0 * scale_x, 1700.0 * scale_y, image=image_1)
        
        # Navigation Buttons
        btn1_img = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
        btn1 = Button(self, image=btn1_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(SettingPage), relief="flat")
        btn1.image = btn1_img
        btn1.place(x=1.0 * scale_x, y=402.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn2_img = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
        btn2 = Button(self, image=btn2_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(ViewPage), relief="flat")
        btn2.image = btn2_img
        btn2.place(x=0.0 * scale_x, y=302.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn3_img = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
        btn3 = Button(self, image=btn3_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(StartPage), relief="flat")
        btn3.image = btn3_img
        btn3.place(x=0.0 * scale_x, y=202.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn4_img = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
        btn4 = Button(self, image=btn4_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(UploadPage), relief="flat")
        btn4.image = btn4_img
        btn4.place(x=0.0 * scale_x, y=102.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        btn5_img = scaled_photoimage(str(relative_to_assets("button_5.png")), scale_x, scale_y)
        btn5 = Button(self, image=btn5_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(homePage), relief="flat")
        btn5.image = btn5_img
        btn5.place(x=0.0 * scale_x, y=1.5 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        
        # Top right button (font setting control)
        button_image_6 = scaled_photoimage(str(relative_to_assets("button_6.png")), scale_x, scale_y)
        button_6 = Button(self, image=button_image_6, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_6 clicked"), relief="flat")
        button_6.image = button_image_6
        button_6.place(x=503.0 * scale_x, y=64.0 * scale_y, width=169.0 * scale_x, height=66.0 * scale_y)
        
        button_image_7 = scaled_photoimage(str(relative_to_assets("button_7.png")), scale_x, scale_y)
        button_7 = Button(self, image=button_image_7, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_7 clicked"), relief="flat")
        button_7.image = button_image_7
        button_7.place(x=503.0 * scale_x, y=64.0 * scale_y, width=169.0 * scale_x, height=66.0 * scale_y)
        
        button_image_8 = scaled_photoimage(str(relative_to_assets("button_8.png")), scale_x, scale_y)
        button_8 = Button(self, image=button_image_8, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_8 clicked"), relief="flat")
        button_8.image = button_image_8
        button_8.place(x=959.0 * scale_x, y=64.0 * scale_y, width=169.0 * scale_x, height=66.0 * scale_y)
        
        button_image_9 = scaled_photoimage(str(relative_to_assets("button_9.png")), scale_x, scale_y)
        button_9 = Button(self, image=button_image_9, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_9 clicked"), relief="flat")
        button_9.image = button_image_9
        button_9.place(x=1181.0 * scale_x, y=64.0 * scale_y, width=169.0 * scale_x, height=66.0 * scale_y)
        
        button_image_10 = scaled_photoimage(str(relative_to_assets("button_10.png")), scale_x, scale_y)
        button_10 = Button(self, image=button_image_10, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_10 clicked"), relief="flat")
        button_10.image = button_image_10
        button_10.place(x=727.0 * scale_x, y=64.0 * scale_y, width=169.0 * scale_x, height=66.0 * scale_y)
        
        # Lower button area
        canvas.create_rectangle(289.0, 502.0, 1396.0, 609.0, fill="#DAEBF9", outline="")
        canvas.create_rectangle(289.0, 697.0, 1403.0, 804.0, fill="#DAEBF9", outline="")
        
        button_image_11 = scaled_photoimage(str(relative_to_assets("button_11.png")), scale_x, scale_y)
        button_11 = Button(self, image=button_image_11, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_11 clicked"), relief="flat")
        button_11.image = button_image_11
        button_11.place(x=342.0 * scale_x, y=525.0 * scale_y, width=226.0 * scale_x, height=66.0 * scale_y)
        
        button_image_12 = scaled_photoimage(str(relative_to_assets("button_12.png")), scale_x, scale_y)
        button_12 = Button(self, image=button_image_12, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_12 clicked"), relief="flat")
        button_12.image = button_image_12
        button_12.place(x=729.0 * scale_x, y=525.0 * scale_y, width=226.0 * scale_x, height=66.0 * scale_y)
        
        button_image_13 = scaled_photoimage(str(relative_to_assets("button_13.png")), scale_x, scale_y)
        button_13 = Button(self, image=button_image_13, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_13 clicked"), relief="flat")
        button_13.image = button_image_13
        button_13.place(x=1116.0 * scale_x, y=525.0 * scale_y, width=226.0 * scale_x, height=66.0 * scale_y)
        
        canvas.create_rectangle(296.0, 239.0, 1403.0, 346.0, fill="#DAEBF9", outline="")
        canvas.create_text(323.0, 274.0, anchor="nw", text="Font Size:", fill="#094478", font=("Jomolhari Regular", 14))
        
        canvas.create_rectangle(502.0, 293.00000002561853, 1350.0000066752837, 298.0, fill="#094478", outline="")
        canvas.create_text(330.0, 735.0, anchor="nw", text="Font Setting:", fill="#094478", font=("Jomolhari Regular", 10))
        
        button_image_14 = scaled_photoimage(str(relative_to_assets("button_14.png")), scale_x, scale_y)
        button_14 = Button(self, image=button_image_14, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_14 clicked"), relief="flat")
        button_14.image = button_image_14
        button_14.place(x=551.0 * scale_x, y=718.0 * scale_y, width=298.0 * scale_x, height=66.0 * scale_y)
        
        button_image_15 = scaled_photoimage(str(relative_to_assets("button_15.png")), scale_x, scale_y)
        button_15 = Button(self, image=button_image_15, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_15 clicked"), relief="flat")
        button_15.image = button_image_15
        button_15.place(x=979.0 * scale_x, y=718.0 * scale_y, width=298.0 * scale_x, height=66.0 * scale_y)
        
        button_image_16 = scaled_photoimage(str(relative_to_assets("button_16.png")), scale_x, scale_y)
        button_16 = Button(self, image=button_image_16, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_16 clicked"), relief="flat")
        button_16.image = button_image_16
        button_16.place(x=377.0 * scale_x, y=888.0 * scale_y, width=348.0 * scale_x, height=94.0 * scale_y)
        
        button_image_17 = scaled_photoimage(str(relative_to_assets("button_17.png")), scale_x, scale_y)
        button_17 = Button(self, image=button_image_17, borderwidth=0, highlightthickness=0,
                           command=lambda: print("button_17 clicked"), relief="flat")
        button_17.image = button_image_17
        button_17.place(x=979.0 * scale_x, y=888.0 * scale_y, width=348.0 * scale_x, height=94.0 * scale_y)
        
        # 对所有 Canvas 项目进行统一缩放
        canvas.scale("all", 0, 0, scale_x, scale_y)

class ConflictPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame3")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        orig_width, orig_height = 1455, 1041
        new_width, new_height = 800, 600
        scale_x, scale_y = new_width / orig_width, new_height / orig_height

        canvas = tk.Canvas(self, bg="#FFFFFF", height=orig_height, width=orig_width,
                           bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        canvas.create_rectangle(
            1070.0, 0.0, 1455.0, 1041.0,
            fill="#79BCF7", outline=""
        )

        canvas.create_text(
            500.0, 20.0,
            anchor="nw",
            text="Conflict",
            fill="#094478",
            font=("Jomolhari Regular", 15)
        )

        canvas.create_rectangle(
            34.0, 104.0, 1034.0, 194.0,
            fill="#DAEBF9", outline=""
        )

        canvas.create_text(
            42.0, 140.0,
            anchor="nw",
            text="Conflict 1",
            fill="#094478",
            font=("Jomolhari Regular", 8)
        )
        canvas.create_text(
            141.0, 140.0,
            anchor="nw",
            text="Courses and professors",
            fill="#094478",
            font=("Jomolhari Regular", 8)
        )
        canvas.create_text(
            400.0, 140.0,
            anchor="nw",
            text="conflict reason",
            fill="#094478",
            font=("Jomolhari Regular", 8)
        )

        button_image_1 = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
        button_1 = ttk.Button(self, image=button_image_1, command=lambda: print("button_1 clicked"))
        button_1.image = button_image_1  # 保存引用
        button_1.place(
            x=1163.0 * scale_x, y=47.5 * scale_y,
            width=201.0 * scale_x, height=83.0 * scale_y
        )

        button_image_2 = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
        button_2 = ttk.Button(self, image=button_image_2, command=lambda: print("button_2 clicked"))
        button_2.image = button_image_2
        button_2.place(
            x=1163.0 * scale_x, y=217.0 * scale_y,
            width=201.0 * scale_x, height=83.0 * scale_y
        )

        button_image_3 = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
        button_3 = ttk.Button(self, image=button_image_3, command=lambda: print("button_3 clicked"))
        button_3.image = button_image_3
        button_3.place(
            x=1163.0 * scale_x, y=398.0 * scale_y,
            width=201.0 * scale_x, height=83.0 * scale_y
        )

        button_image_4 = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
        button_4 = Button(self, image=button_image_4, command=lambda: controller.show_frame(StartPage), relief="flat")
        button_4.image = button_image_4
        button_4.place(x=1163.0 * scale_x, y=587.0 * scale_y, width=201.0 * scale_x, height=83.0 * scale_y)


        options_5 = ["chooes A", "chooes B", "choose C"]
        options_6 = ["choose X", "choose Y", "choose Z"]
        dropdown_var_5 = tk.StringVar()
        dropdown_var_6 = tk.StringVar()

        dropdown_5 = ttk.Combobox(self, textvariable=dropdown_var_5, values=options_5, state="readonly")
        dropdown_5.set("room")
        dropdown_5.place(
            x=638.0 * scale_x, y=128.0 * scale_y,
            width=111.0 * scale_x, height=50.0 * scale_y
        )
        dropdown_5.bind("<<ComboboxSelected>>", lambda e: print(f"Dropdown 5 choose: {dropdown_var_5.get()}"))

        dropdown_6 = ttk.Combobox(self, textvariable=dropdown_var_6, values=options_6, state="readonly")
        dropdown_6.set("time")
        dropdown_6.place(
            x=823.0 * scale_x, y=128.0 * scale_y,
            width=111.0 * scale_x, height=50.0 * scale_y
        )
        dropdown_6.bind("<<ComboboxSelected>>", lambda e: print(f"Dropdown 6 choose: {dropdown_var_6.get()}"))

        canvas.scale("all", 0, 0, scale_x, scale_y)

class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\cs499\gui\assets\frame4")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        orig_width, orig_height = 1455, 1041
        new_width, new_height = 800, 600
        scale_x, scale_y = new_width / orig_width, new_height / orig_height
        canvas = tk.Canvas(self, bg="#FFFFFF", height=orig_height, width=orig_width,
                           bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0.0, 1.0, 235.0, 1042.0, fill="#79BCF7", outline="")
        canvas.create_rectangle(1063.0, 0.0, 1455.0, 81.0, fill="#DAEBF9", outline="")
        btn1_img = scaled_photoimage(str(relative_to_assets("button_1.png")), scale_x, scale_y)
        btn1 = Button(self, image=btn1_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(SettingPage), relief="flat")
        btn1.image = btn1_img
        btn1.place(x=1.0 * scale_x, y=402.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        btn2_img = scaled_photoimage(str(relative_to_assets("button_2.png")), scale_x, scale_y)
        btn2 = Button(self, image=btn2_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(ViewPage), relief="flat")
        btn2.image = btn2_img
        btn2.place(x=0.0 * scale_x, y=302.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        btn3_img = scaled_photoimage(str(relative_to_assets("button_3.png")), scale_x, scale_y)
        btn3 = Button(self, image=btn3_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(StartPage), relief="flat")
        btn3.image = btn3_img
        btn3.place(x=0.0 * scale_x, y=202.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        btn4_img = scaled_photoimage(str(relative_to_assets("button_4.png")), scale_x, scale_y)
        btn4 = Button(self, image=btn4_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(UploadPage), relief="flat")
        btn4.image = btn4_img
        btn4.place(x=0.0 * scale_x, y=102.0 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        btn5_img = scaled_photoimage(str(relative_to_assets("button_5.png")), scale_x, scale_y)
        btn5 = Button(self, image=btn5_img, borderwidth=0, highlightthickness=0,
                      command=lambda: controller.show_frame(homePage), relief="flat")
        btn5.image = btn5_img
        btn5.place(x=0.0 * scale_x, y=1.5 * scale_y, width=235.0 * scale_x, height=100.0 * scale_y)
        entry_image_1 = scaled_photoimage(str(relative_to_assets("entry_1.png")), scale_x, scale_y)
        entry_bg_1 = canvas.create_image(1301.0 * scale_x, 40.5 * scale_y, image=entry_image_1)
        entry_1 = Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        entry_1.place(x=1167.0 * scale_x, y=14.0 * scale_y, width=268.0 * scale_x, height=51.0 * scale_y)
        image_2 = scaled_photoimage(str(relative_to_assets("image_2.png")), scale_x, scale_y)
        canvas.create_image(1116.0 * scale_x, 41.0 * scale_y, image=image_2)
        canvas.create_text(1067.0 * scale_x, 113.0 * scale_y, anchor="nw",
                           text="SORT BY:", fill="#094478",
                           font=("Jomolhari Regular", int(20 * scale_y)))
        button_image_6 = scaled_photoimage(str(relative_to_assets("button_6.png")), scale_x, scale_y)
        button_6 = Button(self, image=button_image_6, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_6 clicked"), relief="flat")
        button_6.image = button_image_6
        button_6.place(x=1167.0 * scale_x, y=864.0 * scale_y, width=200.0 * scale_x, height=101.0 * scale_y)
        button_image_7 = scaled_photoimage(str(relative_to_assets("button_7.png")), scale_x, scale_y)
        button_7 = Button(self, image=button_image_7, borderwidth=0, highlightthickness=0,
                          command=lambda: print("button_7 clicked"), relief="flat")
        button_7.image = button_image_7
        button_7.place(x=1204.0 * scale_x, y=107.0 * scale_y, width=134.0 * scale_x, height=41.0 * scale_y)
        canvas.scale("all", 0, 0, scale_x, scale_y)
# ---------------------------
# Program entry
# ---------------------------
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
