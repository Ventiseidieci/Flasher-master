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
    'Flasher/GUI/mainUI.qml:Flasher/GUI/',
    '--add-data',
    '/Users/ale2610/esp/esp-idf_4.0.0/components/esptool_py/esptool/.:esptool/.',
    # INSERIRE IL PATH DOVE E' INSTALLATO ESPTOOL
    '--add-data',
    'Flasher/configuration/*.csv:Flasher/configuration/',
    '--add-data',
    'Flasher/configuration/*.bin:Flasher/configuration/'
])