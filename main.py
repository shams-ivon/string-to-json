import tkinter as tk 
import json

# Top level window 
frame = tk.Tk() 
frame.title("TextBox Input") 
frame.geometry('800x500') 

# Function for getting input and displaying it
def printJSON(): 
    inp = inputtxt.get(1.0, "end-1c") 
    json_object = json.loads(inp)
    formatted_json = json.dumps(json_object, indent=2)
    outputtxt.delete(1.0, "end")  
    outputtxt.insert(tk.END, formatted_json)  

# TextBox for input 
inputtxt = tk.Text(
    frame, 
    height=5, 
    width=50,
    padx=10,  
    pady=10
) 
inputtxt.pack(pady=20) 

# Button to trigger the conversion 
printButton = tk.Button(
    frame, 
    text="Format JSON", 
    command=printJSON
) 
printButton.pack(pady=10) 

# TextBox for output (with rounded look using padding and background)
outputtxt = tk.Text(
    frame, 
    height=20, 
    width=50,
    padx=20,  
    pady=20, 
    relief=tk.FLAT  # Remove the default border
)
outputtxt.pack(pady=20)

frame.mainloop()
