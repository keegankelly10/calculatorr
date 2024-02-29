import tkinter as tk
#Use this as a starter GUI\

root = tk.Tk()
root.title("Calculator by Keegan")



def calculate():
    expression = label.cget("text")
    try:

        result = eval(expression)
        label.config(text="")
        label.config(text=str(result))
    except ZeroDivisionError:
        print("Error: Cant divide by zero")
    except ValueError:
        print("Error:Invalid Equation")

def printExp(value):
    text= label.cget("text")+value
    label.config(text=text)

def clear():
    label.config(text="")










#Set characteristics for GUI
root.geometry("300x400")
root.configure(bg="lavender")

label= tk.Label(root, bg= "light yellow", fg="Black", padx= "2", pady= '1', width = "20")
buttonZero= tk.Button(root, text = "0",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("0"))
buttonOne= tk.Button(root, text = "1",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("1"))
buttonTwo= tk.Button(root, text = "2",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple",command=lambda:printExp("2"))
buttonThree= tk.Button(root, text = "3",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("3"))
buttonFour= tk.Button(root, text = "4",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("4"))
buttonFive= tk.Button(root, text = "5",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("5"))
buttonSix= tk.Button(root, text = "6",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("6"))
buttonSeven= tk.Button(root, text = "7",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("7"))
buttonEight= tk.Button(root, text = "8",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("8"))
buttonNine= tk.Button(root, text = "9",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple" , command=lambda:printExp("9"))
buttonPlus= tk.Button(root, text = "+",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("+"))
buttonMinus= tk.Button(root, text = "-",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp("-"))
buttonTimes= tk.Button(root, text = "*",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple" , command=lambda:printExp("*"))
buttonDivide= tk.Button(root, text = "/",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple" , command=lambda:printExp("/"))
buttonEquals= tk.Button(root, text = "=",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command = calculate)
buttonClear= tk.Button(root, text = "C",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple" , command=clear )
buttonDecimal= tk.Button(root, text = ".",padx="2", pady="4", height= "3", width= "3", bd= "5", bg= "medium purple", command=lambda:printExp(".")  )

#create GUI
label.grid(row=0, column=0, columnspan= 3)
buttonZero.grid(column=1,row=4)
buttonOne.grid(column=0,row=1)
buttonTwo.grid(column=1,row=1)
buttonThree.grid(column=2,row=1)
buttonFour.grid(column=0,row=2)
buttonFive.grid(column=1,row=2)
buttonSix.grid(column=2,row=2)
buttonSeven.grid(column=0,row=3)
buttonEight.grid(column=1,row=3)
buttonNine.grid(column=2,row=3)
buttonPlus.grid(column=3,row=4)
buttonMinus.grid(column=3,row=3)
buttonTimes.grid(column=3,row=1)
buttonDivide.grid(column=3,row=2)
buttonEquals.grid(column=2,row=4)
buttonDecimal.grid(column=0,row=4)
buttonClear.grid(column=3,row=0)


root.mainloop()