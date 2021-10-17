import tkinter as tk
from functools import partial
from tkinter import ttk

from countryinfo import CountryInfo


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the Details
        self.check_frame = ttk.LabelFrame(self, text="Details", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew", rowspan=2, columnspan=1
        )

        # Add label into Frame Details
        self.label = ttk.Label(
            self.check_frame,
            text="The capital of country is:",
            justify="center",
            font=("-size", 20, "-weight", "bold"),
        )
        self.label.grid(row=1, column=0, pady=10, columnspan=2)


        # Create a Frame for input widgets
        self.widgets_frame = ttk.LabelFrame(self, text="Search", padding=(20, 10))
        #self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=2
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)


        # Entry
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Entry")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.entry.bind("<Return>", self.button_pressed, "Submit")

        # Buttons
        ttk.Button(
                self.widgets_frame,
                text="Submit",
                style="Accent.TButton",
                command=partial(self.button_pressed, "Submit", self.entry, self.label),
            ).grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        ttk.Button(
                self.widgets_frame,
                text='Clear',
                style="TButton",
                command=partial(self.clear_text, self.label),
            ).grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

    # Action on press buttons
    def button_pressed(self, key, entryObj, labelObj):
        if key == "Submit":
            #capital
            country = entryObj.get()
            print(f"Country is {country}")
            capital = CountryInfo(country).capital()
            print(f"Capital is {capital}")
            print("Bingo")
            message = f"The capital of country is:\n {capital}"
            labelObj.config(text = message)
        else:
            pass

    # Clear Entity content
    def clear_text(self, labelObj):
        self.entry.delete(0, 'end')
        labelObj.config(text = "The capital of country is:")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Find Capital")
    root.geometry("600x300")
    root.attributes("-topmost", True)  # It stays always on top of other windows

    # Simply set the theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()