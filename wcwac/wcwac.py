from tkinter import *
import subprocess
from tkinter import messagebox
from tkinter.ttk import Combobox

# Creating the window
window_1 = Tk()
window_1.title("Opening a Whatsapp Chat")
window_1.geometry("1000x500")
window_1.resizable(height=False,
                 width=False
                )
window_1.config(bg="#189dc9")

# Label a Title
label_1 = Label(
                window_1, 
                text="Open a Chat on Whatsapp Without Add a Contact",
                bg="#189dc9",
                fg="#610cc9",
                font=("arial", 20)
               )
label_1.place(x=240, y=40)

label_2 = Label(
                window_1, 
                text="Choose a navigator",
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_2.place(x=410, y=100)

label_3 = Label(
                window_1, 
                text="Enter the phone number",
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_3.place(x=380, y=220)

label_4 = Label(
                window_1, 
                text="By Bryan Quille",
                bg="#189dc9",
                fg="#800575",
                font=("arial", 15)
               )
label_4.place(x=435, y=450)

label_5 = Label(
                window_1, 
                bg="#189dc9",
                fg="#f52e27",
                font=("arial", 20)
               )
label_5.place(x=350, y=400)

# Creating the function with code
def wcwac():

    # Choosing a navigator
    # Dictionary with navigators
    nav = {
           'Microsoft Edge':'microsoftedge.exe',
           'Google Chrome':'chrome.exe',
           'Mozilla Firefox':'firefox.exe'
          }
    na_choose = combo.get()
    n_choose = nav[na_choose]

    # Getting The phone number
    p_n = entry_1.get()

    # Opening the chat on choosen navigator
    if p_n.isnumeric() and len(p_n) == 10:
        # url_c: whatsapp chat url
        url_c = 'http://wa.me/593'
        
        # Concatenate the url
        url_cw = url_c + p_n
        
        subprocess.call(
                        f'start {n_choose} {url_cw}', 
                        shell=True
                    )
    else:
        entry_1.delete(0, END)
        messagebox.showerror("Error", "The input value is wrong!")


# Creating a combobox with navigators
combo = Combobox(
                 window_1, 
                 font=("arial", 20),
                 justify="center"
                )
combo["values"] = (
                   'Microsoft Edge', 
                   'Google Chrome', 
                   'Mozilla Firefox'
                  )
combo.current(0)
combo.place(x=355, y=140)

#Creating the button
entry_1 = Entry(
                window_1, 
                font=("arial", 25),
                justify="center"
               )
entry_1.place(x=325, y=260)

# Creating the Button
button_1 = Button(
                  window_1, 
                  text="Open Chat", 
                  font=("arial", 20), 
                  justify="center",
                  bg="#0fd655",
                  command=wcwac
                 )
button_1.place(x=430, y=320)

window_1.mainloop()