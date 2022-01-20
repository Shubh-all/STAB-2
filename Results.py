
import datetime
from operator import itemgetter
from tkinter import *
from tkinter import ttk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def result_fn(root,possibleSolutions):

    window =Toplevel(root)
    window.geometry("1280x720")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        66.0,
        247.0,
        1214.0,
        659.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        80.0,
        fill="#3888FF",
        outline="")

    canvas.create_text(
        63.0,
        121.0,
        anchor="nw",
        text="Result",
        fill="#3888FF",
        font=("Inter Medium", 28 * -1)
    )

    canvas.create_text(
        70.0,
        23.0,
        anchor="nw",
        text="STAB Calculator",
        fill="#FFFFFF",
        font=("Inter Bold", 28 * -1)
    )

    canvas.create_text(
        1176.0,
        28.0,
        anchor="nw",
        text="Version 2.3",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        1129.0,
        48.0,
        anchor="nw",
        text="All Rights Reserved",
        fill="#FFFFFF",
        font=("Inter Medium", 12 * -1)
    )

    canvas.create_text(
        989.0,
        263.0,
        anchor="nw",
        text="Legends/Instructions:",
        fill="#273340",
        font=("OpenSansRoman Regular", 16 * -1)
    )

    canvas.create_text(
        82.0,
        259.0,
        anchor="nw",
        text="Values",
        fill="#273340",
        font=("OpenSansRoman Regular", 16 * -1)
    )

    canvas.create_text(
        63.0,
        99.0,
        anchor="nw",
        text="Define Stocks & Sieves",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        205.0,
        99.0,
        anchor="nw",
        text="Enter Values",
        fill="#273340",
        font=("OpenSansRoman Regular", 12 * -1)
    )

    canvas.create_text(
        342.0,
        259.0,
        anchor="nw",
        text="Graph",
        fill="#273340",
        font=("OpenSansRoman Regular", 16 * -1)
    )

    canvas.create_rectangle(
        342.0,
        291.0,
        937.0,
        643.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        636.0,
        678.0,
        anchor="nw",
        text="1",
        fill="#273340",
        font=("Inter Regular", 16 * -1)
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
        x=659.0,
        y=675.0,
        width=25.0,
        height=25.0
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
        x=596.0,
        y=675.0,
        width=25.0,
        height=25.0
    )

    canvas.create_text(
        1001.0,
        296.0,
        anchor="nw",
        text="Please use percentage values",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_text(
        1001.0,
        323.0,
        anchor="nw",
        text="Graph is to scale of such.",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_rectangle(
        82.0,
        296.0,
        184.0,
        325.0,
        fill="#C1D6FF",
        outline="")

    canvas.create_rectangle(
        82.0,
        444.0,
        184.0,
        473.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        82.0,
        370.0,
        184.0,
        399.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        82.0,
        518.0,
        184.0,
        547.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        82.0,
        333.0,
        184.0,
        362.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        82.0,
        481.0,
        184.0,
        510.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        82.0,
        407.0,
        184.0,
        436.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        188.0,
        296.0,
        290.0,
        325.0,
        fill="#C1D6FF",
        outline="")

    canvas.create_rectangle(
        188.0,
        444.0,
        290.0,
        473.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        188.0,
        370.0,
        290.0,
        399.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        188.0,
        518.0,
        290.0,
        547.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        188.0,
        333.0,
        290.0,
        362.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        188.0,
        481.0,
        290.0,
        510.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        188.0,
        407.0,
        290.0,
        436.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        90.0,
        301.0,
        anchor="nw",
        text="Stock",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    canvas.create_text(
        196.0,
        301.0,
        anchor="nw",
        text="Percentage",
        fill="#273340",
        font=("OpenSansRoman Regular", 14 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        194.0,
        108.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        280.0,
        108.0,
        image=image_image_2
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
        x=20.0,
        y=124.0,
        width=28.0,
        height=28.0
    )

    canvas.create_text(
        78.0,
        175.0,
        anchor="nw",
        text="No. of Possible Solutions:",
        fill="#273340",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_rectangle(
        66.0,
        185.0,
        72.0,
        191.0,
        fill="#000000",
        outline="")

    canvas.create_text(
        300.0,
        173.0,
        anchor="nw",
        text="16",
        fill="#273340",
        font=("OpenSansRoman SemiBold", 20 * -1)
    )

    canvas.create_text(
        78.0,
        212.0,
        anchor="nw",
        text="Best Solution (1)",
        fill="#273340",
        font=("OpenSansRoman Regular", 18 * -1)
    )

    canvas.create_rectangle(
        66.0,
        222.0,
        72.0,
        228.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        991.0,
        304.0,
        995.0,
        308.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        991.0,
        331.0,
        995.0,
        335.0,
        fill="#000000",
        outline="")

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        35.0,
        40.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        1118.0,
        55.0,
        image=image_image_4
    )
    window.resizable(False, False)
