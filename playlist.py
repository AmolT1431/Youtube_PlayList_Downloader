import youtube_dl

class DL_PlayList:
    def get_playlist_video_urls(playlist_url):
        try:
            ydl_opts = {
                'quiet': True,
                'extract_flat': True,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(playlist_url, download=False)
                if 'entries' in result:
                    return [entry['url'] for entry in result['entries']]
        except Exception as e:
            print(f"Error fetching playlist: {e}")
            return []

    def save_to_txt(video_urls, output_file):
        try:
            with open(output_file, 'w') as file:
                for url in video_urls:
                    file.write("https://www.youtube.com/watch?v="+url + '\n')
            print(f"Video URLs saved to {output_file} successfully!")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def DL_List(playlist_url,output_file):
        
        video_urls = DL_PlayList.get_playlist_video_urls(playlist_url)
        if video_urls:
            DL_PlayList.save_to_txt(video_urls, output_file)
        


