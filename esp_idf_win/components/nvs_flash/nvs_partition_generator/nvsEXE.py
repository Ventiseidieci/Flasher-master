import PyInstaller.__main__

PyInstaller.__main__.run([ 
    'nvs_partition_gen.py',
    '--clean',
    '-n',
    'nvs_gen',
    # '--noconsole',
    '--onefile',
    # '--onedir',
    '--noconfirm',

    # '--log-level',
    # 'DEBUG',
    # '-d',
    # 'imports',
    # '--add-data',
    # 'C:/Users/adilo/.pyenv/pyenv-win/versions/3.11.0b4/Lib/site-packages/customtkinter;customtkinter/',
   # '../../../../Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/customtkinter:customtkinter/',

])