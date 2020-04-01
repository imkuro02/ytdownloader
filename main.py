import os
import converter as cr #does not work when executable
from download import *
import music_player as player
from time import sleep
from pathlib import Path

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

setup(["videos","songs"]) #folders to setup

def yes_no(answer):
    if answer == "y" : return True
    if answer == "n" : return False


def play():
    player.show_list()
    return

def download_file():
    print('downloading')
    age_restriction = False
    link = input("link to video: ")
    if(not age_restriction):
        link = link.replace("watch?v=","embed/") #this takes away the age restriction

    image = None
    while True:
        image = yes_no(input("download image (y/n) : "))
        if image == True or image == False:
            break

    #downloading file
    print("downloading: ", link)
    file = download(link,image,path)
    print(file, " finished Downloading")


    if not image:
        #convert file
        converted_file = cr.convert(file)
        os.rename("{}\\{}".format(path,converted_file),"{}{}{}".format(path,"\\songs\\",converted_file))
        #file converted

        #remove file
        sleep(1)
        os.remove(file)
    else:
        os.rename("{}\\{}".format(path, file), "{}{}{}".format(path, "\\videos\\", file))

    print("process finished")

    '''
    download_more = None
    while True:
        download_more = yes_no(input("download more (y/n) : "))
        if download_more == True or download_more == False:
            break
        
    if download_more == False:
            break
    '''

    return


while True: # loop the code
    #os.system('cls')
#path_file =  Path(__file__).absolute() #file path
    print(
'''
1 download  
2 play 
'''
)
    try:
        command = int(input('command:'))
        if command == 0:
            quit()
        if command == 1:
            download_file()
        if command == 2:
            play()
    except Exception as e:
        print(e)


    
        

        