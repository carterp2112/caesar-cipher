import customtkinter 
import tkinter as tk



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

selection = tk.StringVar()

def returnCipher(message):
    popup = customtkinter.CTk()
    popup.geometry("500x350")
    
    frame2 = customtkinter.CTkFrame(master=popup)
    frame2.pack(pady=20, padx=60, fill="both", expand=True)
    
    label2 = customtkinter.CTkLabel(master=frame2, text="Encrypted Message")
    label2.pack(pady=12, padx=10)  
    
    label3 = customtkinter.CTkLabel(master=frame2, text=message)
    label3.pack(pady=12, padx=10)   
    
def caesarCipher():
    message = entry1.get()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newMessage = ''
    for i in message.lower():
       if(i != ' '):
            position = alphabet.index(i)
            newMessage += alphabet[position - 3]
       else:
           newMessage += ' '
    returnCipher(newMessage)
    
def caesarDecrypt():
    message = entry1.get()
    alphabet = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newMessage = ''
    for i in message.lower():
       if(i != ' '):
            position = alphabet.index(i)
            newMessage += alphabet[position + 3]
       else:
           newMessage += ' '
    returnCipher(newMessage)
    

def select():
    if selection.get() == "True":
        caesarCipher()
    else:
        caesarDecrypt()

    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Message Encryption System", text_color="white")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Message")
entry1.pack(pady=12, padx=10)


button = customtkinter.CTkButton(master=frame, text="Encrypt", command=select)
button.pack(pady=12, padx=10)

radio = customtkinter.CTkRadioButton(master=frame, text="Encrypt", variable=selection, value="True")
radio.pack(pady=12, padx=10)

radio2 = customtkinter.CTkRadioButton(master=frame, text="Decrypt", variable=selection, value="False")
radio2.pack(pady=12, padx=10)

root.mainloop()