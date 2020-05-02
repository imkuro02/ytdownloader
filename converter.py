from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os.path
#from pydub import AudioSegment
import subprocess
import os

def get_name(video_name):
    name = os.path.splitext(video_name)[0]  # print 0 so first
    extension = os.path.splitext(video_name)[1]  # print 1, second in list, extension
    print("converter : {}{}".format(name, extension))
    return (name)


def convert(video_name): #name and extension
    try:
        clip = AudioFileClip(video_name)
        audio_name = get_name(video_name)  # get name without extension
        #audio_name = "{}{}".format(path,audio_name)
        audio_name = "{}.mp3".format(audio_name)
        clip.write_audiofile(audio_name, verbose=False, logger=None) #write out as mp3
        #print("done")

        final_audio_name = f'{audio_name[:-4]}.wav'
        
        subprocess.call(['ffmpeg', '-i', audio_name,
            final_audio_name])

        os.system('cls') # clear long ffmpeg msg

        print(final_audio_name, ' finished converting.')
        skip = input('[Enter]')

        os.remove(audio_name) # remove mp3 file
        return(final_audio_name)
    except Exception as e: #-----------------------------------------------------------------------------------USELESS
        print(e)

#convert("a.mp4")

if(__name__=="__main__"):
    file_name = input("c : file name : ")
    convert(file_name)