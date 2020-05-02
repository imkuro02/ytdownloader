import os
import converter as cr #does not work when executable
from download import *
import music_player as player
from time import sleep
from pathlib import Path
import commander

path = Path().absolute() # folder path
path_songs = "{}\songs".format(path)

def setup(folders):

    for folder in folders:
        dir = "{}\\{}".format(path, folder)
        dir_exists = os.path.isdir(dir)
        exists = None
        if dir_exists :
            exists = "exists"
        else:
            exists = "does not exist yet, making directory"

        print("directory {}".format(folder), exists)
        if not dir_exists :
            os.mkdir(dir)

setup(['videos','songs','lists']) #folders to setup

def yes_no(answer):
    if answer == "y" : return True
    if answer == "n" : return False


def play():
    player.main() # goes to main of player script
    return

def download_file():
    print('downloading')
    age_restriction = False
    link = input("link to video: ")
    if(not age_restriction):
        link = link.replace("watch?v=","embed/") #this takes away the age restriction

    image = None
    while True:
        image = input('download image (y/n): ')
        image = commander.command(image)
        #image = yes_no(input("download image (y/n) : "))
        if image == 'y' or image == 'n':
            break

    #downloading file
    print("downloading: ", link)
    file = download(link,image,path)
    print(file, " finished Downloading")


    if image == 'n': # if asked to download without image -> convert file
        converted_file = cr.convert(file)
        os.rename("{}\\{}".format(path,converted_file),"{}{}{}".format(path,"\\songs\\",converted_file))
        #sleep(1)
        os.remove(file)
    else:
        os.rename("{}\\{}".format(path, file), "{}{}{}".format(path, "\\videos\\", file))
        
    return


while True: # loop the code
    os.system('cls')
    #os.system('cls')
#path_file =  Path(__file__).absolute() #file path
    print(
'''r return
d download  
p play 
'''
    )
    command = input('command: ')
    command = commander.command(command)

    if command == 'r':
        os.system('cls')
        quit()

    if command == 'd':
        download_file()
    if command == 'p':
        play()
  


    
        

        