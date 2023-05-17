import PyInstaller.__main__

PyInstaller.__main__.run([
    'cli.py',
    '--clean',
    # '--noconsole',
    '--windowed',
    '--onefile',
    '--noconfirm',
    '--icon',
    'favicon.icns',
    # '--log-level',
    # 'DEBUG',
    # '-d',
    # 'imports',
    '--add-data',
    '../../../../Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/customtkinter:customtkinter/',
    '--add-data',
    'Flasher/custom_color.json:Flasher/',
    '--add-data',
    '/Users/ale2610/.pyenv/versions/3.11.2/lib/python3.11/site-packages/esptool:esptool/.',
    '--add-data',
    'Flasher/configuration/*.csv:Flasher/configuration/',
    '--add-data',
    'Flasher/configuration/*.bin:Flasher/configuration/'
])