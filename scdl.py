import sys
import youtube_dl
import os

def convert(url):


    # create options for ydl
    # check online for more options
    options = {
    'ignoreerrors': True,       # ignores erros
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'outtmpl': savedir + '/%(title)s -- %(uploader)s.%(ext)s',        # name the file the ID of the video
    'noplaylist' : False,}       # only download single song, not playlist
    

    with youtube_dl.YoutubeDL(options) as ydl:
    #info_dict = ydl.extract_info(url, download=False)
    #ydl.prepare_filename(info_dict)
    #print(info_dict)
        ydl.download([url])
    
    return "Download is Complete"



if __name__ == "__main__":
    print(sys.argv)
    savedir = sys.argv[1]
    url = sys.argv[2]
    

    if not os.path.exists(savedir):
        os.makedirs(savedir)

    convert(url)
