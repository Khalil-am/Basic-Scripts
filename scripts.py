# Python Proofreading
# pip install lmproof
import lmproof
import random, os
import tabula
import PIL
from PIL import Image
from tkinter.filedialog import *
import pytube
from pygame import mixer
from gtts import gTTS
import os
import img2pdf
from fpdf import FPDF
from difflib import SequenceMatcher

from torch import res


def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))


proofread("Your Text")



#Automatic PDF to CSV Converter
filename = input("Enter File Path: ")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')
df.to_csv('output.csv')



#random music windows
music_dir = 'E:\\music diretory'
songs = os.listdir(music_dir)

song = random.randint(0,len(songs))

# Prints The Song Name
print(songs[song])

os.startfile(os.path.join(music_dir, songs[0]))


#Automatic Photo Compressor

fl=askopenfilenames()
img = Image.open(fl[0])
img.save("output.jpg", "JPEG", optimize = True, quality = 10)


#Automatic YouTube Video Downloader

link = input('Youtube Video URL')
video_download = pytube.Youtube(link)
video_download.streams.first().download()
print('Video Downloaded', link)


#Automatic Text to Speech



def main():
    tts = gTTS('Like This Article')
    tts.save('output.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()


if __name__ == "__main__":
    main()


#convert a single image to a PDF
with open("output.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir('path to image') if i.endswith(".jpg")]))
#convert multiple images to PDF:
Pdf = FPDF()

list_of_images = ["wall.jpg", "nature.jpg","cat.jpg"]
for i in list_of_images:
   Pdf.add_page()
  # Pdf.image(i,x,y,w,h) #add pictures here
   Pdf.output("result.pdf", "F")

#Automatic Plagiarism Checker


def plagiarism_checker(f1, f2):
    with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
        f1_data = file1.read()
        f2_data = file2.read()
        res = SequenceMatcher(None, f1_data, f2_data).ratio()


print(f"These files are {res * 100} % similar")
f1 = input("Enter file_1 path: ")
f2 = input("Enter file_2 path: ")
plagiarism_checker(f1, f2)

#Make URLs Shorter
from __future__ import with_statement
import contextlib
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	from urllib import urlopen
import sys
def make_tiny(url):
	request_url = ('http://tinyurl.com/app-index.php?' +
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def main():
	for tinyurl in map(make_tiny, sys.argv[1:]):
		print(tinyurl)

if __name__ == '__main__':
	main()

#Internet Speed Tester
# Internet Speed tester
# pip install speedtest-cli
import speedtest as st

# Set Best Server
server = st.Speedtest()
server.get_best_server()

# Test Download Speed
down = server.download()
down = down / 1000000
print(f"Download Speed: {down} Mb/s")

# Test Upload Speed
up = server.upload()
up = up / 1000000
print(f"Upload Speed: {up} Mb/s")

# Test Ping
ping = server.results.ping
print(f"Ping Speed: {ping}")

