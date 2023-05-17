import PyInstaller.__main__

PyInstaller.__main__.run([
    'cli.py',
    '--clean',
    '--noconsole',
    '--windowed',
    '--onedir',
    '--noconfirm',
    '--icon',
    'favicon.ico',
    # '--log-level',
    # 'DEBUG',
    # '-d',
    # 'imports',
    '--add-data',
    'C:/Users/adilo/.pyenv/pyenv-win/versions/3.11.0b4/Lib/site-packages/customtkinter;customtkinter/',
   # '../../../../Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/customtkinter:customtkinter/',
    '--add-data',
    'Flasher/custom_color.json;Flasher/',
    
    '--add-data',
    'Flasher/configuration/*.csv;Flasher/configuration/',
    '--add-data',
    'Flasher/configuration/*.bin;Flasher/configuration/'
])