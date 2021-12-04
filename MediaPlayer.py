import tkinter as tk
import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog

interface = tk.Tk()
interface.title('Vyacheslav Player')
interface.iconbitmap("goodicon.ico")
interface.geometry('600x600')
interface.config(bg = 'black')

way_to_music = "D:/Python/Django/djsite/MusicPlayer/MusicPlayerNeighbors/Музика"
pattern = "*.mp3"

pygame.mixer.init()

prev_img = tk.PhotoImage(file = "prev.png")
stop_img = tk.PhotoImage(file = "stop.png")
play_img = tk.PhotoImage(file = "play.png")
pause_img = tk.PhotoImage(file = "pause.png")
next_img = tk.PhotoImage(file = "next.png")

def play():
    label.config(text=soundBox.get(ACTIVE))
    music = soundBox.get(ACTIVE)
    song = f"D:/Python/Django/djsite/MusicPlayer/MusicPlayerNeighbors/Музика/{music}.mp3"
    pygame.mixer.music.load(song)
    mixer.music.play()

def stop():
    mixer.music.stop()
    soundBox.select_clear('active')

def pause():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

def next():
    next_song = soundBox.curselection()
    next_song = next_song[0] + 1
    music = soundBox.get(next_song)
    label.config(text = music)
    song = f"D:/Python/Django/djsite/MusicPlayer/MusicPlayerNeighbors/Музика/{music}.mp3"
    pygame.mixer.music.load(song)
    mixer.music.play()

    soundBox.select_clear(0, "end")
    soundBox.activate(next_song)
    soundBox.select_set(next_song)

def back():
    back_song = soundBox.curselection()
    back_song = back_song[0] - 1
    music = soundBox.get(back_song)
    song = f"D:/Python/Django/djsite/MusicPlayer/MusicPlayerNeighbors/Музика/{music}.mp3"
    pygame.mixer.music.load(song)
    mixer.music.play()

    soundBox.select_clear(0, "end")
    soundBox.activate(back_song)
    soundBox.select_set(back_song)


def add_music():
    music = filedialog.askopenfilename(initialdir = "Музика/", title = "Виберіть пісню", filetypes = (("MP3 file", "*.mp3"),))
    music = music.replace("D:/Python/Django/djsite/MusicPlayer/MusicPlayerNeighbors/Музика/", "")
    music = music.replace(".mp3", "")
    soundBox.insert(END, music)
    print(music)


menu_for_music = Menu(interface)
interface.config(menu=menu_for_music)

add_music_menu = Menu(menu_for_music, tearoff = 0)
add_music_menu.add_command(label="Добавити пісню", command = add_music)


author_menu = Menu(menu_for_music, tearoff = 0)
author_menu.add_command(label = "В'ячеслав Денисюк")

menu_for_music.add_cascade(label = "Файл", menu = add_music_menu)
menu_for_music.add_cascade(label = "Автор", menu = author_menu)


soundBox = tk.Listbox(interface, fg = "cyan", bg = "black", width = 100, height = 15, font = ('Times New Roman', 14))
soundBox.pack(padx = 15, pady = 15)

label = tk.Label(interface, text = "", bg = "black", fg = "yellow", font = ('Crystal', 12))
label.pack(pady = 15)

top = tk.Frame(interface, bg = "black")
top.pack(padx = 10, pady = 5, anchor = "center")

prevButton = tk.Button(interface, text = "Попередня", image = prev_img, bg = "black", borderwidth = 6, command = back)
prevButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(interface, text = "Стоп", image = stop_img, bg = "black", borderwidth = 6, command = stop)
stopButton.pack(pady = 15, in_ = top, side = "left")

playButton = tk.Button(interface, text = "Початок", image = play_img, bg = "black", borderwidth = 12, command = play)
playButton.pack(pady = 15, in_ = top, side = "left")

pauseButton = tk.Button(interface, text = "Пауза", image = pause_img, bg = "black", borderwidth = 6, command = pause)
pauseButton.pack(pady = 15, in_ = top, side = "left")

nextButton = tk.Button(interface, text = "Наступна", image = next_img, bg = "black", borderwidth = 6, command = next)
nextButton.pack(pady = 15, in_ = top, side = "left")

interface.mainloop()