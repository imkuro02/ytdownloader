import os
import converter as cr #does not work when executable
from download import *
from time import sleep
from pathlib import Path


def yes_no(answer):
    if answer == "y" : return True
    if answer == "n" : return False

while True: # loop the code
#path_file =  Path(__file__).absolute() #file path
    path = Path().absolute() # folder path
    path_songs = "{}\songs".format(path)

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
    print(file, "  finished Downloading")


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
    download_more = None
    while True:
        download_more = yes_no(input("download more (y/n) : "))
        if download_more == True or image == False:
            break

    if download_more == False:
        break

print ("shutting down :)")
sleep(4)
print("just hold your horses")
sleep(3)
print("aaanyyyy minute now....")
sleep(3)
print("shutting down.. frl")
sleep(1)
print("dont close the window or your pc will EXPLODE")
sleep(20)
print("I was joking, you can close the app idc")
sleep(2)
print("dont do it tho, the pc will explode")
sleep(10)
print(":)")
sleep(3)