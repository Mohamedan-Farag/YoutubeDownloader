import tkinter
import customtkinter
from msrest import Configuration 

from pytube import YouTube

# download function
def start():
    try:
        yt=link.get()
        url = YouTube(yt)
        video = url.streams.get_highest_resolution()

        title_yt.configure(text=url.title, font=("Arial", 14),text_color="white")
        finisho.configure(text="")
        video.download()
        finisho.configure(text="Download completed",text_color="green")
    except:
        finisho.configure(text="Download failed",text_color="red")
        title_yt.configure(text="Insert a youtube link", font=("Arial", 14),text_color="white")
 

    
        

#SYSTEM
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# FRAME 
app =customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI
title = customtkinter.CTkLabel(app, text="Youtube Downloader", font=("Arial", 24))
title.pack(pady=10, padx=10)

title_yt =  customtkinter.CTkLabel(app, text="Insert a youtube link", font=("Arial", 14))
title_yt.pack(pady=10, padx=10)

# input
url_input = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable=url_input, width=400 ,height=35, font=("Arial", 12))
link.pack(pady=10, padx=10)


# download function
download = customtkinter.CTkButton(app, text="Download", font=("Arial", 16), command=start)
download.pack(pady=10, padx=10)

# finish
finisho = customtkinter.CTkLabel(app, text="")
finisho.pack()

# RUN
app.mainloop()
