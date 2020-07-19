import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading

def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="site-stats-count").find_all("li")
    all_details = ""
    for block in info_div:
        count = block.find("strong").get_text()
        text = block.find("span").get_text()
        all_details = all_details + text + ":" + count + "\n"

    return all_details

def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing.....")
    mainLabel['text'] = newdata

def notification():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=10,
            app_icon='icon.ico'
        )
        time.sleep(30)

root = tk.Tk()
root.geometry("900x800")
root.iconbitmap("Virus.ico")
root.title("CORONA DETAIL TRACKER - INDIA")
root.configure(background='white')
font = ("poppins", 25, "bold")

banner = tk.PhotoImage(file="image.jpg")
bannerLabel = tk.Label(root, image=banner)
bannerLabel.pack()

mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=font, bg='white')
mainLabel.pack()

refreshBtn = tk.Button(root, text="REFRESH", font=font, relief='solid', command=refresh)
refreshBtn.pack()

th1 = threading.Thread(target=notification)
th1.setDaemon(True)
th1.start()

root.mainloop()