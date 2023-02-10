from tkinter import *
import subprocess
from tkinter import messagebox
from tkinter.ttk import Combobox
import pandas as pd


# Creating the window
window_1 = Tk()
window_1.title("Whatsapp Chat")
window_1.geometry("1000x500")
window_1.resizable(
                   height=False,
                   width=False
                  )
window_1.config(bg="#189dc9")


# Labels
label_1 = Label(
                window_1, 
                text="Open a Whatsapp Chat without Add the Contact",
                bg="#189dc9",
                fg="#610cc9",
                font=("arial", 20)
               )
label_1.place(x=220, y=40)

label_2 = Label(
                window_1, 
                text="Choose a navigator",
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_2.place(x=420, y=100)

label_3 = Label(
                window_1, 
                text="Enter the Phone Number",
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_3.place(x=380, y=280)

label_4 = Label(
                window_1, 
                text='Choose a Country',
                bg="#189dc9",
                fg="#4f4e52",
                font=("arial", 18)
               )
label_4.place(x=425, y=190)

label_5 = Label(
                window_1, 
                text="By Bryan Quille",
                bg="#189dc9",
                fg="#800575",
                font=("arial", 15)
               )
label_5.place(x=435, y=460)


# Creating the function with code
def wcwac():

    # Choosing a navigator
    # Dictionary with navigators
    nav = {
           'Microsoft Edge':'microsoftedge.exe',
           'Google Chrome':'chrome.exe',
           'Mozilla Firefox':'firefox.exe'
          }
    na_choose = combo_1.get()
    n_choose = nav[na_choose]

    # Choosing a country
    #Getting data
    dcc = pd.read_excel(
                        'E:/COURSES/Programming Courses/Python Courses/Projects/whatsapp_chat_project/data/country_code.xlsx', 
                        index_col=False, 
                        engine='openpyxl'
                       )
    dcc_df = pd.DataFrame(dcc)  # Convert to DataFrame
    dcc_list = dcc_df.to_numpy().tolist()  # Convert rows on lists
    # Convert a list on a dictionary
    dcc_dic = {}
    for i in range(0, len(dcc_list)):
        dcc_dic[dcc_list[i][0]] = dcc_list[i][1]
    cc_choose = combo_2.get()
    c_choose = dcc_dic[cc_choose]

    # Getting The phone number
    p_n = entry_1.get()

    # Opening the chat on choosen navigator
    if p_n.isnumeric():
        # url_c: whatsapp chat url
        url_c = 'http://wa.me/'

        # Country code choosen
        country_code = str(c_choose)
        
        # Concatenate url
        url_cw = url_c + country_code + p_n
        
        subprocess.call(
                        f'start {n_choose} {url_cw}', 
                        shell=True
                       )
    else:
        entry_1.delete(0, END)
        messagebox.showerror(
                             "Error", 
                             "The phone number is wrong!"
                            )


# Creating a combobox with navigators
combo_1 = Combobox(
                   window_1, 
                   font=("arial", 20),
                   justify="center"
                  )
combo_1["values"] = (
                     'Microsoft Edge', 
                     'Google Chrome', 
                     'Mozilla Firefox'
                    )
combo_1.current(0)
combo_1.place(x=355, y=140)


# Creating a combobox with countries
combo_2 = Combobox(
                   window_1, 
                   font=("arial", 20),
                   justify="center"
                  )
combo_2["values"] = (
                     'Afghanistan', 'Albania', 'Algeria', 
                     'Andorra', 'Angola', 'Antigua and Barbuda', 
                     'Argentina', 'Armenia', 'Australia', 
                     'Austria', 'Azerbaijan', 'Bahamas', 
                     'Bahrain', 'Bangladesh', 'Barbados', 
                     'Belarus', 'Belgium', 'Belize', 
                     'Benin', 'Bhutan', 'Bolivia', 
                     'Bosnia and Herzegovina', 'Botswana', 'Brazil', 
                     'Brunei', 'Bulgaria', 'Burkina Faso', 
                     'Burundi', 'Cabo Verde', 'Cambodia', 
                     'Cameroon', 'Canada', 'Central African Republic', 
                     'Chad', 'Chile', 'China', 
                     'Colombia', 'Comoros', 'Costa Rica', 
                     'Croatia', 'Cuba', 'Cyprus', 
                     'Czech Republic', 'Democratic Republic of the Congo', 'Denmark', 
                     'Djibouti', 'Dominica', 'Dominican Republic', 
                     'East Timor', 'Ecuador', 'Egypt', 
                     'El Salvador', 'Equatorial Guinea', 'Eritrea', 
                     'Estonia', 'Ethiopia', 'Fiji', 
                     'Finland', 'France', 'Gabon', 
                     'Gambia', 'Georgia', 'Germany', 
                     'Ghana', 'Greece', 'Grenada', 
                     'Guatemala', 'Guinea', 'Guinea-Bissau', 
                     'Guyana', 'Haiti', 'Honduras', 
                     'Hungary', 'Iceland', 'India', 
                     'Indonesia', 'Iran', 'Iraq', 
                     'Ireland', 'Israel', 'Italy', 
                     'Ivory Coast', 'Jamaica', 'Japan', 
                     'Jordan', 'Kazakhstan', 'Kenya', 
                     'Kiribati', 'Kuwait', 'Kyrgyzstan', 
                     'Laos', 'Latvia', 'Lebanon', 
                     'Lesotho', 'Liberia', 'Libya', 
                     'Liechtenstein', 'Lithuania', 'Luxembourg', 
                     'Macedonia', 'Madagascar', 'Malawi', 
                     'Malaysia', 'Maldives', 'Mali', 
                     'Malta', 'Marshall Islands', 'Mauritania', 
                     'Mauritius', 'Mexico', 'Micronesia', 
                     'Moldova', 'Monaco', 'Mongolia', 
                     'Montenegro', 'Morocco', 'Mozambique', 
                     'Myanmar', 'Namibia', 'Nauru', 'Nepal', 
                     'Netherlands', 'New Zealand', 'Nicaragua', 
                     'Niger', 'Nigeria', 'North Korea', 
                     'Norway', 'Oman', 'Pakistan', 
                     'Palau', 'Panama', 'Papua New Guinea', 
                     'Paraguay', 'Peru', 'Philippines', 
                     'Poland', 'Portugal', 'Qatar', 
                     'Republic of the Congo', 'Romania', 'Russia', 
                     'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 
                     'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 
                     'São Tomé and Príncipe', 'Saudi Arabia', 'Senegal', 
                     'Serbia', 'Seychelles', 'Sierra Leone', 
                     'Singapore', 'Slovakia', 'Slovenia', 
                     'Solomon Islands', 'Somalia', 'South Africa', 
                     'South Korea', 'South Sudan', 'Spain', 
                     'Sri Lanka', 'Sudan', 'Suriname', 
                     'Swaziland', 'Sweden', 'Switzerland', 
                     'Syria', 'Tajikistan', 'Tanzania', 
                     'Thailand', 'Togo', 'Tonga', 
                     'Trinidad and Tobago', 'Tunisia', 'Turkey', 
                     'Turkmenistan', 'Tuvalu', 'Uganda', 
                     'Ukraine', 'United Arab Emirates', 'United Kingdom', 
                     'United States', 'Uruguay', 'Uzbekistan', 
                     'Vanuatu', 'Venezuela', 'Vietnam', 
                     'Yemen', 'Zambia', 'Zimbabwe'
                    )
combo_2.current(49)
combo_2.place(x=355, y=230)


#Creating the entry
entry_1 = Entry(
                window_1, 
                font=("arial", 25),
                justify="center"
               )
entry_1.place(x=325, y=320)


# Creating the Button
button_1 = Button(
                  window_1, 
                  text="Open Chat", 
                  font=("arial", 20), 
                  justify="center",
                  bg="#0fd655",
                  command=wcwac
                 )
button_1.place(x=430, y=380)


window_1.mainloop()