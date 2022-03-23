import os, sys
from PIL import Image
import glob
from tqdm import tqdm
import easygui

def set_path():
    path = easygui.diropenbox()
    return path

def png_to_jpg(file_path):
    im = Image.open(file_path)
    im = im.convert("RGB")
    im = im.save(file_path.replace(".png", ".jpg"))

def do_jpg(file_path):
    im = Image.open(file_path)
    im = im.convert("RGB")
    im = im.save(file_path, quality=28)

path = set_path()
images_png = glob.glob(path + "/**/*.png", recursive = True)
images_jpg = glob.glob(path + "/**/*.jpg", recursive = True)

msg = "Sprawdz poprawność ścieżki: \n" + path
title = "Potwierdzenie"
if easygui.ccbox(msg, title):
    print("Converting PNG to JPG files...")
    for file in tqdm(images_png):
        file = file.replace("\\", "/")
        png_to_jpg(file)

    print("Cleaning job..")
    for file in tqdm(images_png):
        file = file.replace("\\", "/")
        os.remove(file)

    print("Compressing JPG files...")
    for file in tqdm(images_jpg):
        file = file.replace("\\", "/")
        do_jpg(file)

    easygui.msgbox("DONE")
else:
    sys.exit(0)
