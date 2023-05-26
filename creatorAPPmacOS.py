#!/usr/bin/env python

import PyInstaller.__main__

PyInstaller.__main__.run([
    'cli.py',
    '--clean',
    '-n',
    'Vbite_Flasher',
    # '--console',
    # '--onedir',
    '--windowed',
    '--onefile',
    '--noconfirm',
    '--icon',
    'favicon.icns',
    # '--log-level',
    # 'DEBUG',
    # '-d',
    # 'all',
    # '--python-executable=/Users/ale2610/.pyenv/shims/python',
    '--add-data',
    'Flasher/GUI/images/favicon.icns:Flasher/GUI/images/',
    '--add-data',
    'Flasher/GUI/mainUI.qml:Flasher/GUI/',
    '--add-data',
    'esp_idf/.:esp_idf/.',
    # INSERIRE IL PATH DOVE E' INSTALLATO ESPTOOL
    '--add-data',
    'Flasher/configuration/*.csv:Flasher/configuration/',
    '--add-data',
    'Flasher/configuration/*.bin:Flasher/configuration/'
])