""" 
This project executes a program which ask 
for a phone number and opens a navigator 
where starts a chat on Whatsapp without 
add a contact.
"""
import subprocess

def wcwac():
    # wcwac: Whatsapp chat without add a contact.
    
    # p_n: phone number.
    p_n = input("Enter the phone number: ")
    
    # Dictionary with navigators
    nav = {
           'Microsoft Edge':'microsoftedge.exe',
           'Google Chrome':'chrome.exe',
           'Mozilla Firefox':'firefox.exe'
          }
    
    # Choose a navigator
    

    if p_n.isnumeric() and len(p_n) == 10:
        # url_c: whatsapp chat url
        url_c = 'http://wa.me/593'
        
        # Concatenate the url
        url_cw = url_c + p_n
        
        subprocess.call(
                        f'start {nav["Microsoft Edge"]} {url_cw}', 
                        shell=True
                       )
    else:
        print("The phone number is wrong.")

if __name__ == '__main__':
    wcwac()