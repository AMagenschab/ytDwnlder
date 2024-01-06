import sys
from cx_Freeze import setup, Executable

## build v1
# setup( 
#     name = "Youtube Downlader",
#     version = "1.0",
#     description = "Andi's famous YouTube Downloader",
#     executables = [Executable("app_strlit.py")])


## build v2
# productName = "ProductName"
# # if 'bdist_msi' in sys.argv:
# #     sys.argv += ['--initial-target-dir', 'C:\InstallDir\\' + productName]
# #     sys.argv += ['--install-script', 'install.py']

# exe = Executable(
#       script="app_strlit.py",
#       base="Win32GUI"
#      )
# setup(
#       name="Product.exe",
#       version="1.0",
#       author="Me",
#       description="Copyright 2012",
#       executables=[exe],
#       #scripts=[
#       #         'install.py'
#       #         ]
#       ) 

# build v3, v5
# setup( 
#      name = "Youtube Downlader",
#      version = "1.0",
#      description = "Andi's famous YouTube Downloader",
#      executables = [Executable("main_run.py")])

# # build v4, v6
# setup( 
#      name = "Youtube Downloader",
#      version = "1.0",
#      description = "Andi's famous YouTube Downloader",
#      options={"build_exe": {"packages": ["streamlit", "pandas", "os", "pytube"], "excludes": [""]}},
#      executables = [Executable("main_run.py")])

# build v7
setup( 
     name = "Youtube Downloader",
     version = "1.0",
     description = "Andi's famous YouTube Downloader",
     options={"build_exe": {"packages": ["streamlit", "pandas", "os", "pytube"], "excludes": [""]}},
     executables = [Executable("app_strlit.py")])