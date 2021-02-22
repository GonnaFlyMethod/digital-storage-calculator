from tkinter import *
from converter import Converter
from unit_creator import DataUnitCreator
from all_data_units import *

root = Tk()

value_to_convert_global = StringVar()

root.title("Digital storage calculator")
root.geometry("230x260");
root.resizable(False, False) 

photo = PhotoImage(file = "icon.png")
root.iconphoto(False, photo)

LIST_FROM_POSSIBLE_UNITS = ["b"] + list(Converter.data_units_methods_storage.keys())
LIST_TO_POSSIBLE_UNITS = LIST_FROM_POSSIBLE_UNITS.copy()

LIST_FROM_POSSIBLE_UNITS = tuple(LIST_FROM_POSSIBLE_UNITS)
LIST_TO_POSSIBLE_UNITS = tuple(LIST_TO_POSSIBLE_UNITS)

convert_from = None
convert_to = None
answer = None
answer_text_var = StringVar()
answer_text_var.set("Answer:")

def from_selection_callback(selection):
	global convert_from
	convert_from = selection


def to_selection_callback(selection):
	global convert_to
	convert_to = selection
	
def convertation():
	global answer, value_to_convert_global, answer_text
	from_unit = None
	to_unit = None
	value_to_convert = None

	try:
		value_to_convert = float(value_to_convert_global.get())
	except ValueError:
		answer_text_var.set("Value to convert isn't valid")
		return

	if convert_from == "b":
		from_unit = Bit(value_to_convert)
	else:
		from_unit = DataUnitCreator.data_units_classes_storage[convert_from](value_to_convert)
	
	if convert_to == "b":
		to_unit = Bit(value_to_convert)
	else:
		to_unit = DataUnitCreator.data_units_classes_storage[convert_to](1)
	
	new_converter = Converter()
	res_of_convertation = Converter.convert(from_unit, to_unit)
	
	
	answer_GUI = f"{value_to_convert}({convert_from}) = {res_of_convertation}({convert_to})"
	answer_text_var.set(answer_GUI)


from_text = Label(root, text="Convert from - ").place(x=20, y=10)

default_val_of_option_menu_from = StringVar(root)
# default_val_of_option_menu_from.set(LIST_FROM_POSSIBLE_UNITS[0]) # default value from


optionMenuFrom = OptionMenu(root, default_val_of_option_menu_from, *LIST_FROM_POSSIBLE_UNITS,
                            command=from_selection_callback).place(x=110, y=5)

value_for_convertation = Label(root, text="Value for convertation").place(x=20, y=45)

entry_value_for_convertation = Entry(root, textvariable=value_to_convert_global, width=30).place(x=20, y=80)

to_text = Label(root, text="Convert to - ").place(x=20, y=120)

default_val_of_option_menu_to = StringVar(root)
#default_val_of_option_menu_to.set(LIST_TO_POSSIBLE_UNITS[1]) # default value to

optionMenuTo = OptionMenu(root, default_val_of_option_menu_to, *LIST_TO_POSSIBLE_UNITS,
                          command=to_selection_callback).place(x=110, y=115)

calculate_button = Button(root, text = "Calculate!", command=convertation).place(x=20, y=160)
answer_text = Label(root, textvariable=answer_text_var).place(x=10, y=200)

root.mainloop()