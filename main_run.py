## Main file to be executed: Add all required imports here ##
## Eg. 

import pandas as pd
import pytube
import streamlit as st
import os

from app_func import pytube_search, pytube_download 

import subprocess

if __name__ == '__main__':
    subprocess.run("streamlit run app_strlit.py")