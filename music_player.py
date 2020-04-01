import os
from time import sleep
from os import path
import winsound

def play_from_index(index,songs):
    #playsound(f'songs\\{songs[index]}',False)
    song =  f'songs\\{songs[index]}'
    
    winsound.PlaySound(song, winsound.SND_ASYNC | winsound.SND_ALIAS )
    #os.system(f'songs\\{songs[index]}')
    #sound_file = vlc.MediaPlayer(f'songs\\{songs[index]}')
    a = input('a')
    winsound.PlaySound(None, winsound.SND_ALIAS) 

    return
    

def show_list():
    os.system('cls')
    contents = os.listdir("./songs")

    i = 0
    for content in contents:
        print(i, content)
        i += 1

    song = int(input('song index: '))
    play_from_index(song,contents)
    print(f'going to play {song}')
    

