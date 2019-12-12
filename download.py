from pytube import YouTube
import re

def download(link,image,path):

    yt = YouTube(link)

    t = yt.streams.filter(only_audio=not image).all()


    file_name=(t[0].title)
    file_name = re.sub('[!?@#;:/|$:.,]', '', file_name)
    file_name = file_name+".mp4"

    t[0].download(path)

    return(file_name)
