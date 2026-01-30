import tkinter


window = tkinter.Tk()
window.minsize(width=500, height=300)

# Left grid
left_label = tkinter.Label(text="is equal to")
left_label.grid(column=1, row=2)

# Middle grid
entry = tkinter.Entry()
entry.grid(column=2, row=1)

result_label = tkinter.Label("0")
result_label.grid(column=2, row=2)

calculate_button = tkinter.Button(text="Calculate")
calculate_button.grid(column=2, row=3)

# Right grid
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=3, row=2)

window.mainloop()