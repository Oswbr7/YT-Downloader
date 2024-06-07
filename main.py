import tkinter
import customtkinter
from pytube import YouTube

def StartVideo():
    try:
        ytlink =  link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color ="white")
        finishlabel.configure(text="")
        
        video.download()
        finishlabel.configure(text="Downloaded!")
    except:
        finishlabel.configure(text="Download Error", text_color="red")

def StartAudio():
    try:
        ytlink =  link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color ="white")
        finishlabel.configure(text="")
        
        video.download()
        finishlabel.configure(text="Downloaded!")
    except:
        finishlabel.configure(text="Download Error", text_color="red")
    

def on_progress(stream, chunk, bytes_remaining):  
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percenage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percenage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #update progress bar
    progressBar.set(float(percenage_of_completion) / 100)


#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished Downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

#Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.5)
progressBar.pack(padx=10, pady=10)

#Download button
downloadVideo = customtkinter.CTkButton(app, text="Download MP4", command=StartVideo)
downloadVideo.pack(padx=10, pady=10)

downloadAudio = customtkinter.CTkButton(app, text="Download MP3", command=StartAudio)
downloadAudio.pack(padx=10, pady=10)

#Run App
app.mainloop()