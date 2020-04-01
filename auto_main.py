import os
import converter as cr #does not work when executable
from download import *
from time import sleep
from pathlib import Path
import sys

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

links = []
f = open("links.txt", "r")
for x in f:
    #print(x)
    links.append(x)

IMAGE = sys.argv[0]

for LINK in links: # loop the code
#path_file =  Path(__file__).absolute() #file path

    try:

        age_restriction = False
        link = LINK
        if(not age_restriction):
            link = link.replace("watch?v=","embed/") #this takes away the age restriction

        image = False

        #downloading file
        # print("downloading: ", link)
        file = download(link,image,path)
        if file != None:
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
    except Exception as e:
        print(e)
    