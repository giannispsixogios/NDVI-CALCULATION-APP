# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 02:06:05 2023

@author: giannisps
"""

import tkinter as tk
import rasterio as rs
import numpy as np
from matplotlib import cm
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import *


root = tk.Tk()
root.geometry("650x650")
root.title("NDVI CALCULATION")


frame = tk.Frame(root, bg='#45aaf2')

lbl_pic_path = tk.Label(frame, text='Image Path:', padx=25, pady=25, font=('verdana',16), bg='#45aaf2')
lbl_show_pic = tk.Label(frame, bg='#45aaf2')
lbl_show_pic2 = tk.Label(frame, bg='#45aaf2')
lbl_show_pic3 = tk.Label(frame, bg='#45aaf2')

entry_pic_path = tk.Entry(frame, font=('verdana',16))
btn_browse = tk.Button(frame, text='Select Image',bg='grey', fg='#ffffff', font=('verdana',16))

def selectPic():
    global img
    global ndvi_img
    global ndvi_thres
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image", filetypes=( (("All files", ".*"),("TIFF files", ".tif"))))
    with rs.open(filename) as src:
        red = src.read(8)
        nir = src.read(4)
        ndvi = (nir - red) / (nir + red)
        ndvi_thres = ndvi > 0.2;
        
        ndvi_thres = Image.fromarray(((ndvi_thres))).resize((200,200))
        #ndvi_img = Image.fromarray(np.uint8(cm.gist_earth(ndvi)*255)).resize((200,200))
        ndvi_img = Image.fromarray(((ndvi))).resize((200,200))

    img = Image.open(filename).resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic['image'] = img
    entry_pic_path.insert(0, filename)
    
def displayPic():
    global ndvi_img
    ndvi_tk = ImageTk.PhotoImage(ndvi_img)
    lbl_show_pic2['image'] = ndvi_tk
    lbl_show_pic2.image = ndvi_tk
    
def displayPic2():
    global ndvi_thres
    thres_tk = ImageTk.PhotoImage(ndvi_thres)
    lbl_show_pic3['image'] = thres_tk
    lbl_show_pic3.image = thres_tk
    

def savefile():
    global ndvi_img
    global ndvi_thres
    #filename2 = filedialog.asksaveasfile(filetypes = [('TIFF files', '*.tif')], mode='w', defaultextension= (("TIFF files", ".tif")))
    filename2 = filedialog.asksaveasfile(filetypes = [('TIFF files', '*.tif')], mode='w', defaultextension= (("TIFF files", ".tif")))
    if not filename2:
         return
    edge.save(filename2)

btn_browse.config(command=selectPic)
btn_ndvi = tk.Button(frame, text='Display NDVI',bg='grey', fg='#ffffff', font=('verdana',16), command=displayPic)
btn_thres = tk.Button(frame, text='Display Thres',bg='grey', fg='#ffffff', font=('verdana',16), command=displayPic2)

button = tk.Button(root, text='Save', command=savefile)

frame.pack(fill=BOTH, expand=1)
lbl_pic_path.grid(row=0, column=0)
entry_pic_path.grid(row=0, column=1)
btn_browse.grid(row=0, column=2)
lbl_show_pic.grid(row=1, column=0, columnspan=3)
btn_ndvi.grid(row=2, column=0, columnspan=3)
btn_thres.grid(row=5, column=0, columnspan=3)

lbl_show_pic2.grid(row=3, column=0, columnspan=3)
lbl_show_pic3.grid(row=4, column=0, columnspan=3)

root.mainloop()