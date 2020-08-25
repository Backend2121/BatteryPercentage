from PIL import Image, ImageDraw,ImageFont
from infi.systray import SysTrayIcon
from zipfile import ZipFile
import psutil
import time
import requests
import os

download_path = "C:\\Users\\" + os.getlogin() + "\\Documents\\BatteryViewer\\"

def download_font():
    if os.path.isfile(download_path + "8-BIT WONDER.TTF"):
        print("Font Exists")
        return download_path + "8-BIT WONDER.TTF"
    else:
        print("Font doens't exists")
        r = requests.get("https://dl.dafont.com/dl/?f=8bit_wonder")
        with open(download_path + "8bit_wonder.zip", "wb") as code:
            code.write(r.content)
        with ZipFile("8bit_wonder.zip", 'r') as zip_ref:
            zip_ref.extractall(download_path)
        return download_path + "8-BIT WONDER.TTF"

image = "C:\\Users\\" + os.getlogin() + "\\Documents\\BatteryViewer\\battery.ico"
start = True

# d.rectangle([(0, 0), (50, 50)], fill=(255, 255, 255), outline=None)               #To color stuff
font = download_font()
font = font.replace("\\","\\\\")
font_type  = ImageFont.truetype(download_font(), 25)                                #8-bit font cool af
n = 0
while True:
    # create image
    img = Image.new('RGBA', (50, 50))                                                   #Create ico with 50x50 size
    d = ImageDraw.Draw(img)                                                             #Draw the image
    a = str(psutil.sensors_battery().percent)                                           #Get battery percentage
    d.text((0,10), f"{a}", fill=(255,255,255), font = font_type)                        #Set white battery percentage as text in ico image

    img.save(image)                                                                     #Save image

    if start:                                                                           #Instantiate systray application
        start = False
        systray = SysTrayIcon(image, "Systray")
        systray.start()
    else:                                                                               #Update systray application
        systray.update(icon=image)
    time.sleep(10)                                                                      #Chill 10s