from tkinter import *
import all_constants as c


class Converter:
    """
    Length conversion tool
    """

    def __init__(self):
        """
        Length converter GUI
        """

        self.length_frame = Frame(padx=10, pady=10)
        self.length_frame.grid()

        self.length_heading = Label(self.length_frame,
                                    text="Length Convertor",
                                    font=("Arial", "16", "bold")
                                    )
        self.length_heading.grid(row=0)

        instructions = ("Please enter a distance below and then press "
                        "one of the buttons to convert it from Kilometers "
                        "to Miles.")
        self.length_instructions = Label(self.length_frame,
                                         text=instructions,
                                         wraplength=250, width=40,
                                         justify="left")
        self.length_instructions.grid(row=1)

        self.length_entry = Entry(self.length_frame,
                                  font=("Arial", "14")
                                  )
        self.length_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.length_frame, text=error,
                                  fg="#004C99", font=("Arial", "12", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.length_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["To Kilometers", "#990099", lambda: self.check_length(c.ABS_ZERO_MILES), 0, 0],
            ["To Miles", "#009900", lambda: self.check_length(c.ABS_ZERO_KILOMETERS), 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)

    def check_length(self, min_length):
        """
        Checks distance is valid and either invokes calculation
         function or shows a custom error
        """

        # Retrieve temperature to be converted
        to_convert = self.length_entry.get()

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.length_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to 0"
        has_errors = "no"

        # checks that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= min_length:
                self.convert(min_length, to_convert)
            else:
                has_errors = "yes"

        except ValueError:
            has_errors = "yes"

        # display the error if necessary
        if has_errors == "yes":
            self.answer_error.config(text=error, fg="#9C0000", font=("Arial", "10", "bold"))
            self.length_entry.config(bg="#F4CCCC")
            self.length_entry.delete(0, END)

    def convert(self, min_length, to_convert):

        if min_length == c.ABS_ZERO_KILOMETERS:
            self.answer_error.config(text=f"Converting {to_convert} Kilometers to Miles")
        else:
            self.answer_error.config(text=f"Converting {to_convert} Miles to Kilometers")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Length Converter")
    Converter()
    root.mainloop()
