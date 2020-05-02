import os
from time import sleep
from os import path
import winsound
import commander

def play_from_index(index,songs):
    song =  f'songs\\{songs[index]}'
    print(f'playing - {song}')
    winsound.PlaySound(song, winsound.SND_ASYNC | winsound.SND_ALIAS )
    skip = input('[Enter] to skip')
    winsound.PlaySound(None, winsound.SND_ALIAS) 
    return
    

def main():
    os.system('cls')
    songs = os.listdir("./songs")

    
    song_list_temp = []

    while True:
        os.system('cls')
        print(
'''
r return
a show all songs
p play temp list
s show temp list
c clear temp list

'''
        )
        
        i = 0
        for content in songs:
            print(f'{i} {content}')
            i += 1

        command = input('command: ')
        command = commander.command(command)

        try:
            song_list_temp.append(int(command))
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
                for content in song_list_temp:
                    play_from_index(content,songs)

        if command == 's': # show list
            i = 0

            if len(song_list_temp) == 0:
                print('no songs in current list')
                skip = input('[Enter]')
            else:    
                print('song order:')
                for content in song_list_temp:
                    print(f'{i} - {songs[song_list_temp[i]]}')
                    i += 1
                skip = input('[Enter]')
        
        if command == 'c': # show list
            song_list_temp = []
            print('temp list cleared')
            skip = input('[Enter]')
                
    os.system('cls')

if __name__ == '__main__':
    main()

    
    
    

