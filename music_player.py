import os
from time import sleep
from os import path
from pathlib import Path
import winsound
import commander
import subprocess
from func_timeout import *

import threading
import keyboard




def play_from_index(songs,song_list_temp):
    #os.system('cls')
    
    for song in song_list_temp:
        os.system('cls')
        song = f'songs\\{song}'.replace('\n','') # remove new line
        print(f'playing - {song}')
        winsound.PlaySound(song, winsound.SND_ASYNC | winsound.SND_ALIAS )

        statbuf = os.stat(f'{song}')
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 170
        #print(int(duration))

        #time_passed = 0

        
        
        class CountdownTask: 
            
            def __init__(self): 
                self._running = True
            
            def terminate(self): 
                self._running = False
                
            def run(self, n): 
                sleep(.2)
                print('')
                while self._running and n < duration: 
                    sleep(.2) 
                    n += .2
                    if self._running:
                        print(f'\r{int(n)} / {int(duration)} ', end="") 
                        # print(f'\r{int(n)} / {int(duration)} | command: ', end="") 
        


        c = CountdownTask()
        def func_skip():
            t = threading.Thread(target = c.run, args =(.2, )) 
            t.start() 
            print('press enter to skip')
            keyboard.wait('enter')
            

        

        try:
            skip = func_timeout(int(duration), func_skip) 
            c.terminate()  
        except FunctionTimedOut:
            c.terminate()  
            pass

        
        winsound.PlaySound(None, winsound.SND_ALIAS) 

    return


def menu_temp_list():
    os.system('cls')
    
    
    song_list_temp = []

    while True:
        os.system('cls')
        print(
'''r return
p play temp list
s show temp list
d delete temp list
c create temp list

'''
        )
        songs = os.listdir("./songs")
        i = 0
        for content in songs:
            print(f'{i} {content}')
            i += 1

        command = input('command: ')
        command = commander.command(command)

        try:
            if command >= 0 and command <= len(songs):
                song =  f'{songs[command]}'
                song_list_temp.append(song)
        except:
            pass

        if command == 'r': # return
            return

        if command == 'p': # play list
            print('- player -')
            if len(song_list_temp) == 0:
                print('no songs in current list')
                skip = input('[Enter]')
                
            else:    
                #for content in song_list_temp:
                play_from_index(songs,song_list_temp)

        if command == 's': # show list
            i = 0

            if len(song_list_temp) == 0:
                print('no songs in current list')
                skip = input('[Enter]')
            else:    
                print('song order:')
                for content in song_list_temp:
                    print(f'{i} - {content}')
                    i += 1
                skip = input('[Enter]')
        
        if command == 'd': # delete temp list
            song_list_temp = []
            print('temp list cleared')
            skip = input('[Enter]')
        
        if command == 'c':
            with open('templist.txt', 'w') as f:
                for item in song_list_temp:
                    f.write("%s\n" % item)

            while True:

                listname = input('name this playlist: ')
                try:
                    os.rename('templist.txt', f'lists\\{listname}.txt')
                    print(f'list saved as {listname}')
                    skip = input('[Enter] to skip')
                    break
                except:
                    print('list already exists, make a new name')
            return
    os.system('cls')

def play_list():
    songs = os.listdir("./songs")
    print(
'''r return
type name of playlist
''')

    i = '-'
    os.system('cls')
    lists = os.listdir("./lists")

    for content in lists:
        print(f'{i} {content[:-4]}')
        # i += 1

    command = input('command: ')
    command = commander.command(command)

    if command == 'r': # return
        return

    listname = f'lists\\{command}.txt' 
    
    list_file = open (listname, "r")

    # Read list of lines
    song_list = list_file.readlines()
    
    # Close file 
    list_file.close()

    play_from_index(songs,song_list)

def menu_main():
    os.system('cls')

    while True:
        os.system('cls')
        print(
'''r return
n new list
p play saved list
d delete saved list
''')
        command = input('command: ')
        command = commander.command(command)

        if command == 'r': # return
            return
        
        if command == 'n': # create new list
            menu_temp_list()

        if command == 'p':
            play_list()
            



def main():
    menu_main()

if __name__ == '__main__':
    main()

    
    
    

