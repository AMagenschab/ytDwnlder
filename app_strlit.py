# ------------------------------------------------------------#
#                                                               #
#      Streamlit App UI                                           #
#                                                               #
#--------------------------------------------------------------#

import streamlit as st
from app_func import pytube_search, pytube_download

import pandas as pd
import numpy as np
import os
#import logging

st.set_page_config(
    page_title="YouTube Downloader App",
    page_icon=":music:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:andreas.magenschab@gmail.com',
        'Report a bug': 'mailto:andreas.magenschab@gmail.com',
        'About': "With this app you can download videos from YouTube. Either only Audio or the whole video."
    }
)

@st.cache_data # using cashing otherwise the function is triggered every time the page is upated
def sr_cache(search_term):
    return pytube_search(search_term = search_term).y_search() # search in YTube

# ------------------------------------------------------------#
#                                                               #
#      Search                                            #
#                                                               #
#--------------------------------------------------------------#

st.title ("Andi's famous Youtube Downloader")

# setting inital values
#confirm_trigger = False
download_trigger = False
#sel_vids = pd.DataFrame(np.zeros(shape = (0,0)))

# Search for videos
with st.form('1) Search for Videos:'):
    search_term = st.text_input(label = 'Search for video:', value = "your input...") # input

    if search_term != 'your input...':
        with st.status('Searching on YouTube...'):
            search_res = sr_cache(search_term = search_term) # search in YTube
            edited_search = search_res # done because of error

    search_trigger = st.form_submit_button('Search')

# show hits and allow selection
if (search_term != 'your input...'):
    with st.form('2) Do your selection:'):
        st.write('Found ' + str(search_res.shape[0]) + ' hits -> Do your selection in the table (use the check-box)!')
        edited_search = st.data_editor(search_res[['author', 'title', 'length[min]', '# views', 'Select','url']], hide_index = True) # show output
            
        confirm_trigger = st.form_submit_button('Confirm Selection')

#st.stop()

        # show selected videos
        #if confirm_trigger == True:
        #if search_term != 'your input...':
    with st.form('show selection'):
        sel_vids = edited_search[edited_search['Select']==True] # selected videos only
        st.write('You selected  ' + str(sel_vids.shape[0]) + ' File(s):') # info on nr. of vids selected

        if sel_vids.shape[0] < 1: # case no selection was made
            st.write('No Selection Done -> please do your selection!')

        else:
            st.dataframe(sel_vids, hide_index = True) # show selectd videos
            
            download_choice = st.radio("Select Download Option 👇",["Audio-NormalQuality", "Audio-BestQuality", "Video-BestQuality"],
                    horizontal=True)
            
            download_path = os.path.normpath(st.text_input('Give the upload path here: (copy from File Explorer)'))
            
        download_trigger = st.form_submit_button('Download selected Files') # Final submission button


@st.cache_data # using cashing otherwise the function is triggered every time the page is upated
def download_cache(sel_vids:pd.DataFrame, download_path:str, download_choice: str):
    '''Function to Dowload selected videos for given choice into given download_path
    param sel_vids: Pandas DF of selected videos
    download Path: string of path where file should be downloaded
    download choice: given the 3 options above'''

    if sel_vids.shape[0] < 1:
        st.error('No Selection made - Download not started!')
        #print('###########################size error########################')
        raise ('error')

    if len(str(download_path)) < 2 or os.path.exists(download_path) == False:
        st.error('Incorrect Download path given - Download not started!')        
        #print('###########################folder error########################')
        raise ('error')

    if download_choice == "Audio-NormalQuality":

        for index, row in sel_vids.iterrows(): # perform download for all selected videos
            pytube_download(search_url = row['url'], download_path = download_path).audio_base() # base audio download
            return True

    elif download_choice == "Audio-BestQuality":

        for index, row in sel_vids.iterrows(): # perform download for all selected videos
            pytube_download(search_url = row['url'], download_path = download_path).audio_best() # best audio download
            return True

    elif download_choice == "Video-BestQuality":

        for index, row in sel_vids.iterrows(): # perform download for all selected videos
            pytube_download(search_url = row['url'], download_path = download_path).video_best() # video best download
            return True

# Finally download given the user input
if download_trigger == True: # Download button is hit
    st.write('Download button triggered')
    with st.status('Downloading selected file(s) given the requirements:'):
        try:
            download_cache(sel_vids = sel_vids, download_path = download_path, download_choice = download_choice) # perform the download
            st.write('Donwload completed - Downloaded ' + str(sel_vids.shape[0]) + ' File(s) in ' + str(download_choice))
        except:
            st.error('Download could not be performed - check your settings!')             