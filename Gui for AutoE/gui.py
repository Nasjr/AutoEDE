
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Pycharm\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x762")
window.configure(bg = "#1E1E1E")


canvas = Canvas(
    window,
    bg = "#1E1E1E",
    height = 762,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    504.0,
    476.00000000000006,
    image=image_image_1
)

canvas.create_text(
    40.0,
    32.0,
    anchor="nw",
    text="Auto-E",
    fill="#FFFFFF",
    font=("SFProDisplay Bold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    940.125,
    38.617645263671875,
    image=image_image_2
)

canvas.create_text(
    59.0,
    90.0,
    anchor="nw",
    text="Consistency And Hard Work Are The Key Aspects Of Success   ",
    fill="#FFFFFF",
    font=("SFProDisplay Bold", 30 * -1)
)

canvas.create_text(
    58.0,
    226.0,
    anchor="nw",
    text="Keep On Editing",
    fill="#FF3465",
    font=("SFProDisplay Bold", 50 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    959.0,
    711.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    860.0,
    714.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    762.0,
    710.0,
    image=image_image_5
)

canvas.create_text(
    611.0,
    28.0,
    anchor="nw",
    text="About Us",
    fill="#FFFFFF",
    font=("SFProDisplay Bold", 20 * -1)
)

canvas.create_text(
    726.0,
    28.0,
    anchor="nw",
    text="Service & Support",
    fill="#FFFFFF",
    font=("SFProDisplay Bold", 20 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    763.0,
    587.0,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1000.0,
    y=12.0,
    width=10.0,
    height=10.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=984.0,
    y=12.113304138183594,
    width=11.0,
    height=9.473684310913086
)

canvas.create_text(
    987.0,
    32.0,
    anchor="nw",
    text="-",
    fill="#000000",
    font=("SFProDisplay Bold", 12 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=169.0,
    y=360.0,
    width=168.0,
    height=41.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    762.5,
    534.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=611.0,
    y=522.0,
    width=303.0,
    height=22.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=932.0,
    y=522.0,
    width=63.0,
    height=24.0
)
window.resizable(False, False)
window.mainloop()
