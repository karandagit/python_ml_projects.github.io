from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *

font = ('Verdana, 20')
file_size = 0

def completeDownload(stream=None, file_path=None):
    print("download completed")
    showinfo("Message", "File has been downloaded.....")
    dBtn['text'] = "Download video"
    dBtn['state'] = "active"
    urlField.delete(0, END)

def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    file_downloaded = (file_size - bytes_remaining)
    per = (file_downloaded / file_size) * 100
    dBtn.config(text="{:00.0f} % downloaded".format(per))

def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_complete_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)
    except Exception as e:
        print(e)

def btnClick():
    try:
        dBtn['text'] = "Please Wait...."
        dBtn['state'] = 'disabled'
        url = urlField.get()
        if url == '':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()
    except Exception as e:
        print(e)

root = Tk()
root.title("My youtube downloader")
root.iconbitmap("img/icon.ico")
root.geometry("500x600")

file = PhotoImage(file="img/youtube.png")
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, pady=3)

urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()

dBtn = Button(root, text="Download Video", font=font, relief='ridge', command=btnClick)
dBtn.pack(side=TOP, pady=20)


root.mainloop()