from pytube import YouTube
from playlist import DL_PlayList

def download_video(url):
    output_path = "PlayList_Videos/"
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        print(f"Downloading {yt.title}...")
        stream.download(output_path)
        print(f"{yt.title} downloaded successfully!")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


DL_PlayList.DL_List()


#here you need to add playlist_viedo.txt file path, please note before that path
#you should add your project path like project path\playlist_viedo.txt
path=r"F:\C & C++\New folder (2)\python\playlist_videos.txt" 


print("Downloding PLAY LIST >>>>>>>>")
file = open(path, 'r')
for each in file:
    line=each.replace("\n","")
    download_video(line)

