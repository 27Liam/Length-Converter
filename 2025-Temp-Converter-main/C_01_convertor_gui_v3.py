from tkinter import *


class Converter:
    """
    Converts temperature between degrees C and Fahrenheit
    """

    def __init__(self):
        # common format for all buttons
        font_12_b = ("Arial", "12", "bold")
        font_16_b = ("Arial", "16", "bold")
        font_14 = ("Arial", "14")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        temp_frame = Frame(padx=10, pady=10)
        temp_frame.grid()

        # Set up Widgets
        heading_label = {"text": "Temperature Converter", "font": font_16_b}
        heading_label_grid = {'row': 0}
        self.heading_label = Label(temp_frame, heading_label).grid(heading_label_grid)

        instructions_label = {"text": "Instructions go here", "wraplength": 350}
        instructions_label_grid = {'row': 1}
        self.instructions_label = Label(temp_frame, instructions_label).grid(instructions_label_grid)

        # Create entry widget
        self.temp_entry = Entry(temp_frame, font=font_14)
        self.temp_entry.grid(row=2, padx=10, pady=10)

        # Conversion, help and history / export buttons
        button_frame = Frame(temp_frame)
        button_frame.grid(row=4)

        # button list (label | bg colour | command | row | column)
        button_details_list = [
            ["To Celsius", "#990099", self.to_celsius, 0, 0],
            ["To Fahrenheit", "#009900", "", 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        self.button_ref_list = []

        for item in button_details_list:
            make_button = {'text': item[0], 'bg': item[1], 'fg': button_fg, 'font': font_12_b, 'width': 12,
                           'command': item[2]}
            make_button_grid = {'row': item[3], 'column': item[4], 'padx': 5, 'pady': 5}
            self.make_button = Button(button_frame, make_button).grid(make_button_grid)

            # add button to reference list
            self.button_ref_list.append(self.make_button)

        self.to_history_button = self.button_ref_list[3]

    def to_celsius(self):
        print("you pushed the celsius button")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
