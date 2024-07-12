import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0 , "end")
    text_result.insert(1.0 , calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0 , "end")
        text_result.insert(1.0 , result)
    except:
        clear_field()
        text_result.insert(1.0 , "Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0 , "end")

root = tk.Tk()
root.geometry("300x300")
root.title("Modern Calculator")
root.configure(bg="#4b4b4b")  # Darker shade of gray
root.resizable(False, False)  # Disable window resizing

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="white", fg="black", bd=0)
text_result.grid(columnspan=5, padx=5, pady=5)

btn_color_num = "#d3d3d3"
btn_color_op = "#4682b4"
border_color = "white"

button_options = {
    'width': 5, 
    'font': ("Arial", 14), 
    'bd': 0, 
    'highlightthickness': 1, 
    'highlightbackground': border_color, 
    'highlightcolor': border_color, 
    'padx': 5, 
    'pady': 5
}

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), bg=btn_color_num, **button_options)
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), bg=btn_color_num, **button_options)
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), bg=btn_color_num, **button_options)
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), bg=btn_color_num, **button_options)
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), bg=btn_color_num, **button_options)
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), bg=btn_color_num, **button_options)
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), bg=btn_color_num, **button_options)
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), bg=btn_color_num, **button_options)
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), bg=btn_color_num, **button_options)
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), bg=btn_color_num, **button_options)
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), bg=btn_color_op, fg="white", **button_options)
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), bg=btn_color_op, fg="white", **button_options)
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), bg=btn_color_op, fg="white", **button_options)
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), bg=btn_color_op, fg="white", **button_options)
btn_div.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), bg=btn_color_op, fg="white", **button_options)
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), bg=btn_color_op, fg="white", **button_options)
btn_close.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14), bg=btn_color_op, fg="white", bd=0, highlightthickness=1, highlightbackground=border_color, highlightcolor=border_color)
btn_clear.grid(row=6, column=1, columnspan=2, padx=5, pady=5)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14), bg=btn_color_op, fg="white", bd=0, highlightthickness=1, highlightbackground=border_color, highlightcolor=border_color)
btn_equals.grid(row=6, column=3, columnspan=2, padx=5, pady=5)

root.mainloop()
