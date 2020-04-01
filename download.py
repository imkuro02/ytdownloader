from pytube import YouTube
import re
import os
import pathlib

def download(link,image,path):

    yt = YouTube(link)

    t = yt.streams.filter(only_audio=not image).all()


    file_name=(t[0].title)
    file_name = re.sub('[!?@#;:/|$:.,]', '', file_name)
    
    try:
        file = pathlib.Path(f'songs\\{file_name}.mp3')
        if file.exists():
            print('file exists')
            return None
        file = pathlib.Path(f'videos\\{file_name}.mp4')
        if file.exists():
            print('file exists')
            return None
    except:
        pass

    t[0].download(path)

    file_name = file_name+".mp4"
    return(file_name)
