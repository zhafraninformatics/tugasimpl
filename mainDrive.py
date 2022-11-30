#libary tkinter GUI
import tkinter as tk

#Import File Dari MetodeKNNAI
import MetodeKNNAI 

import numpy as np

#Module Untuk Menggambar dan Merubah
from PIL import Image, ImageTk, ImageDraw


model = MetodeKNNAI.load_ai()

#Membuat Pop Up Window
window = tk.Tk()

#Membuat Canvas
img = Image.new(mode="1", size=(500, 500), color=0)

#Convert Object agar bisa dibaca oleh TkInter
tkimage = ImageTk.PhotoImage(img) 
canvas = tk.Label(window, image=tkimage)
canvas.pack()

#Modul Untuk  Menggambar
draw = ImageDraw.Draw(img)

last_point = (0, 0)
#Menampilkan Label Hasil Gambar 
prediction = tk.StringVar()
label = tk.Label(window, textvariable=prediction)

#Event Titik Kordinat di Canvas
def draw_image(event):
    global last_point, tkimage, prediction
    current_point = (event.x, event.y)
    
    #Membuat Garis di canvas
    draw.line([last_point, current_point], fill=255, width=60)
    last_point = current_point
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()
    
    #Klasifikasi Gambar
    img_temp = img.resize((28, 28)) 
    img_temp = np.array(img_temp) #Jadikan Array
    img_temp = img_temp.flatten()
    
    #Hitung Hasil Dan Tampilkan Hasil
    output = model.predict([img_temp])
    if(output[0] == 0):
        prediction.set("Gambar Ini Menghasilkan kotak") 
    elif(output[0] == 1):
        prediction.set("Gambar Ini Menghasilkan lingkaran")
    elif(output[0] == 2):
        prediction.set("Gambar Ini menghasilkan Segitiga")
    elif(output[0] == 3):
        prediction.set("Gambar ini Menghasilkan bergelombang")
    else:
        prediction.set("Gambar Ini Menghasilkan zigzag")
    label.pack()

# Callback Titik Awal Garis
def start_draw(event):
    global last_point
    last_point = (event.x, event.y)

#Callback Mereset Gambar di Canvas
def reset_canvas(event):
    global tkimage, img, draw
    img = Image.new(mode="1", size=(500, 500), color=0)
    draw = ImageDraw.Draw(img)
    tkimage = ImageTk.PhotoImage(img)
    canvas['image'] = tkimage
    canvas.pack()

#Counter
kotak = 0
lingkaran = 0
segitiga = 0
gbergelombang = 0
gzigzag = 0

#Data Latih Gambar
def save_image(event):
    global kotak, lingkaran, segitiga, gbergelombang, gzigzag
    img_temp = img.resize((28, 28))
    if(event.char == "k"):
        img_temp.save(f"kotak/{kotak}.png")
        kotak += 1
    elif(event.char == "l"):
        img_temp.save(f"lingkaran/{lingkaran}.png")
        lingkaran += 1
    elif(event.char == "s"):
        img_temp.save(f"segitiga/{segitiga}.png")
        segitiga += 1
    elif(event.char == "b"):
        img_temp.save(f"gbergelombang/{gbergelombang}.png")
        gbergelombang += 1 
    elif(event.char == "z"):
        img_temp.save(f"gzigzag/{gzigzag}.png")
        gzigzag  += 1

#Event Motion Kursos
window.bind("<B1-Motion>", draw_image)
window.bind("<ButtonPress-1>", start_draw)
window.bind("<ButtonPress-3>", reset_canvas)
window.bind("<Key>", save_image)


label.pack()

#Menampilkan Window
window.mainloop()