import os
import qrcode
import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import Image

################################################### ---GUI Definition--- #####################################################

root = customtkinter.CTk()
root.geometry("400x300")
root.title("QR Code Generator")

##################################################### ---Generator--- ########################################################

def generateQR():
    if (enter_url.get() != ""):
        if (enter_name.get() != ""):
            
            img = qrcode.make(enter_url.get())
            img.save(enter_name.get() + '.jpg')
            image = Image.open(enter_name.get() + '.jpg')
            image.show()

            enter_url.delete(0, "end")
            enter_name.delete(0, "end")
            enter_url.focus()
            CTkMessagebox(title="Success", message= "QR Code generated Successfuly!", icon= "check")
            #display
        else:
            CTkMessagebox(title="Error", message= "Please enter Name!", icon= "warning")
    else:
        CTkMessagebox(title="Error", message= "Please enter URL!", icon= "warning")

######################################################## ---GUI--- ###########################################################

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx= 20, pady= 20, fill= "both", expand= True)

label_url = customtkinter.CTkLabel(master=frame, text= "Enter valid URL:", font= ("Ariel", 20))
label_url.pack(padx= 10, pady= 10)

enter_url = customtkinter.CTkEntry(master= frame, placeholder_text= "www.example.com", font=("Ariel", 15), width= 300)
enter_url.pack(padx= 10, pady= 10)

label_name = customtkinter.CTkLabel(master=frame, text= "Enter file name::", font= ("Ariel", 20))
label_name.pack(padx= 10, pady= 10)

enter_name = customtkinter.CTkEntry(master= frame, placeholder_text= "Your file name here", font=("Ariel", 15), width= 300)
enter_name.pack(padx= 10, pady= 10)

button = customtkinter.CTkButton(master= frame, text= "Generate", command= generateQR, height=200)
button.pack(padx= 10, pady= 10)

###################################################### ---Run GUI--- #########################################################

root.mainloop()