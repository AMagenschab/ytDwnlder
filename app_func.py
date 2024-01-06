# ------------------------------------------------------------#
#                                                               #
#      Functions used for the youtube download app              #
#                                                               #
#--------------------------------------------------------------#

import pandas as pd
from pytube import YouTube
from pytube import Search


# ------------------------------------------------------------#
#                                                               #
#      Youtube Download class              #
#                                                               #
#--------------------------------------------------------------#


class pytube_search:
    def __init__(self, search_term):
        self.search_term = search_term

    def y_search(self):
        '''Function to find Videos based on a given search_term
        input: search_term
        output: various infos to found videos as pd.DataFrame
        '''
        sc = Search(self.search_term)
        sr = sc.results

        v_data = []

        for v in sr:
            v_data.append([v.author, v.title, round(v.length / 60, 2), v.rating, v.views, v.watch_url])


        res_frame = pd.DataFrame(v_data, columns=['author', 'title', 'length[min]', 'rating', '# views', 'url'])
        res_frame['Select'] = False # set Select column to False by default
        
        return res_frame
    

class pytube_download:
    def __init__(self, search_url, download_path):
        self.search_url = search_url
        self.download_path = download_path

    def audio_base(self):
        '''Function to Download Audio in Normal quality
        input: YouTube url
        output: Download file to target folder''' 

        yt = YouTube(self.search_url)

        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream
        filename = yt.author + '_' + yt.title + '.mp3'
        audio_stream.download(output_path=self.download_path, filename=filename)


    def audio_best(self):
        '''Function to Download Audio in Best quality
        input: YouTube url
        output: Download file to target folder''' 

        yt = YouTube(self.search_url)

        # Get the audio stream
        audio_stream = yt.streams.get_audio_only()

        # Download the audio stream
        filename = yt.author + '_' + yt.title + '.mp3'
        audio_stream.download(output_path=self.download_path, filename=filename)


    def video_best(self):
        '''Function to Download Video in best quality available
        input: YouTube url
        output: Download file to target folder''' 

        yt = YouTube(self.search_url)

        # Get the audio stream
        video_stream = yt.streams.get_highest_resolution()#filter(only_video=True).first()

        # Download the audio stream
        filename = yt.author + '_' + yt.title + '.mp4'
        video_stream.download(output_path=self.download_path, filename=filename)