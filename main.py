from pytube import YouTube
from playlist import DL_PlayList
import os


def download_video(url,name):
    output_path = name+"/"
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()

        print(f"{yt.title} .......")
        stream.download(output_path)
        print(f"Downloaded >>>>>>>>>>>>>>>>>>>>>>>>> Done\n")
        
    except Exception as e:
        print(f"Error downloading {url}: {e}")


playlist_url = input("Enter Youtube PlayList link : ")  # Replace with your playlist URL
output_file = input("Enter PlayList Name : ")  # Output file name

DL_PlayList.DL_List(playlist_url,output_file+".txt")


current_directory = os.getcwd()
path=current_directory+"\\"+output_file+".txt"


print("Downloding PLAY LIST >>>>>>>>")
file = open(path, 'r')

for each in file:
    line=each.replace("\n","")
    download_video(line,output_file)

