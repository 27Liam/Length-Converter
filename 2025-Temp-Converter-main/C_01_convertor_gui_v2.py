from tkinter import *


class Converter:
    """
    Converts temperature between degrees C and Fahrenheit
    """

    def __init__(self):
        """
        Creates converter GUI
        """

        # common format for all buttons
        font_12_b = ("Arial", "12", "bold")
        font_16_b = ("Arial", "16", "bold")
        font_14 = ("Arial", "14")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        # label text and row numbers
        label_text_list = [
            ["Temperature Converter", 0],
            ["Please enter a temperature below and then press "
             "the desired button to convert it to Celsius / Fahrenheit", 1],
            ["Please enter a number", 3]

        ]

        # list to hold labels, so they can be retrieved and configured
        self.label_ref_list = []

        # loop makes labels as per labels list
        for item in label_text_list:
            self.make_label = Label(self.temp_frame, text=item[0])
            self.make_label.grid(row=item[1])

            self.label_ref_list.append(self.make_label)

        self.heading_label = self.label_ref_list[0]
        self.instructions_label = self.label_ref_list[1]
        self.error_label = self.label_ref_list[2]

        # format labels
        self.heading_label.config(font=font_16_b)
        self.instructions_label.config(justify="left", wraplength=250)
        self.error_label.config(fg="#9C0000")

        # Create entry widget
        self.temp_entry = Entry(self.temp_frame, font=font_14)
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (label | bg colour | command | row | column)
        button_details_list = [
            ["To Celsius", "#990099", self.to_celsius, 0, 0],
            ["To Fahrenheit", "#009900", "", 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg=button_fg, font=font_12_b, width=12,
                                      command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            # add button to reference list
            self.button_ref_list.append(self.make_button)

        self.to_history_button = self.button_ref_list[3]

        # Disable history button at start
        self.to_history_button.config(state=DISABLED)

    # check temperature is more than -459 and convert it
    def to_celsius(self):
        print("You pushed to celsius")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
