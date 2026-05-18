from tkinter import *


class Converter:

    def __init__(self):

        # common format for all buttons
        # Arial size 14 bold, with white text
        font_12_b = ("Arial", "12", "bold")
        font_16_b = ("Arial", "16", "bold")
        font_14 = ("Arial", "14")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.length_frame = Frame(padx=10, pady=10)
        self.length_frame.grid()

        self.length_heading = Label(self.length_frame,
                                    text="Length Convertor",
                                    font=font_16_b
                                    )
        self.length_heading.grid(row=0)

        instructions = "Please enter a length below and " \
                       "then press one of the buttons to convert " \
                       "it from kilometers to miles."
        self.length_instructions = Label(self.length_frame,
                                         text=instructions,
                                         wraplength=250, width=40,
                                         justify="left")
        self.length_instructions.grid(row=1)

        self.length_entry = Entry(self.length_frame,
                                  font=font_14
                                  )
        self.length_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.length_error = Label(self.length_frame, text="",
                                  fg="#9C0000")
        self.length_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.length_frame)
        self.button_frame.grid(row=4)

        self.to_kilometers_button = Button(self.button_frame,
                                           text="To Kilometers",
                                           bg="#990099",
                                           fg=button_fg,
                                           font=font_12_b, width=12,
                                           command=self.to_celsius)
        self.to_kilometers_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_miles_button = Button(self.button_frame,
                                      text="To Miles",
                                      bg="#009900",
                                      fg=button_fg,
                                      font=font_12_b, width=12)
        self.to_miles_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                        text="Help / Info",
                                        bg="#CC6600",
                                        fg=button_fg,
                                        font=font_12_b, width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=font_12_b, width=12,
                                        state=DISABLED)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)


    def to_kilometers(self):
        print("you pushed to kilometers")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Length Converter")
    Converter()
    root.mainloop()
