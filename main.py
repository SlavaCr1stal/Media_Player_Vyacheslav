import tkinter as tk
import fnmatch
import os
import pygame
from pygame import mixer

interface = tk.Tk()
interface.title('Vyacheslav Player')
interface.iconbitmap("goodicon.ico")
interface.geometry('600x600')
interface.config(bg = 'black')

way_to_music = "D:\\Python\Django\djsite\MusicPlayer\MusicPlayerNeighbors\Музика"
pattern = "*.mp3"

pygame.mixer.init()

prev_img = tk.PhotoImage(file = "prev.png")
stop_img = tk.PhotoImage(file = "stop.png")
play_img = tk.PhotoImage(file = "play.png")
pause_img = tk.PhotoImage(file = "pause.png")
next_img = tk.PhotoImage(file = "next.png")

def play():
    label.config(text = soundBox.get("anchor"))
    mixer.music.load(way_to_music + "\\" + soundBox.get("anchor"))
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
    next_song_name = soundBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(way_to_music + "\\" + next_song_name)
    mixer.music.play()

    soundBox.select_clear(0, "end")
    soundBox.activate(next_song)
    soundBox.select_set(next_song)

def back():
    back_song = soundBox.curselection()
    back_song = back_song[0] - 1
    back_song_name = soundBox.get(back_song)
    label.config(text = back_song_name)

    mixer.music.load(way_to_music + "\\" + back_song_name)
    mixer.music.play()

    soundBox.select_clear(0, "end")
    soundBox.activate(back_song)
    soundBox.select_set(back_song)

soundBox = tk.Listbox(interface, fg = "cyan", bg = "black", width = 100, height = 15, font = ('Crystal', 14))
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

for root, dirs, files in os.walk(way_to_music):
    for i in fnmatch.filter(files, pattern):
        soundBox.insert("end", i)

interface.mainloop()