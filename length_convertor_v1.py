from tkinter import *
from functools import partial  # To prevent unwanted windows
import all_constants as c
import conversion_rounding as cr


class Converter:
    """
    Length conversion tool
    """

    def __init__(self):
        """
        Length converter GUI
        """

        self.all_calculations_list = []

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
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
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

        # retrieve to_help button
        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_length(self, min_length):
        """
        Checks temperature is valid and either invokes calculation
         function or shows a custom error
        """

        # Retrieve temperature to be converted
        to_convert = self.length_entry.get()

        # Reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.length_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_length}"
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
        """
        Converts distances and updates answer label.  Also stores
        calculations for Export / History feature
        """

        if min_length == c.ABS_ZERO_KILOMETERS:
            answer = cr.to_miles(to_convert)
            answer_statement = f"{to_convert} Kilometers is {answer} Miles"
        else:
            answer = cr.to_kilometers(to_convert)
            answer_statement = f"{to_convert} Miles is {answer} Kilometers"

        # enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)

    def to_help(self):
        """
        Opens help dialogue box and disables help button
        (so that users can't create multiple help boxes).
        """
        DisplayHelp(self)


class DisplayHelp:
    """
    Displays help dialogue box
    """

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit..  \n\n" \
                    " Note that -273 degrees C " \
                    "(-459 F) is absolute zero (the coldest possible " \
                    "temperature).  If you try to convert a " \
                    "temperature that is less than -273 degrees C, " \
                    "you will get an error message. \n\n " \
                    "To see your " \
                    "calculation history and export it to a text " \
                    "file, please click the 'History / Export' button."

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background colour on
        # everything except the buttons.
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
