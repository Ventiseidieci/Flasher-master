# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['cli.py'],
    pathex=[],
    binaries=[],
    datas=[('../../../../Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/customtkinter', 'customtkinter/'), ('Flasher/custom_color.json', 'Flasher/'), ('/Users/ale2610/.pyenv/versions/3.11.2/lib/python3.11/site-packages/esptool', 'esptool/.'), ('Flasher/configuration/*.csv', 'Flasher/configuration/'), ('Flasher/configuration/*.bin', 'Flasher/configuration/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.icns'],
)
app = BUNDLE(
    exe,
    name='cli.app',
    icon='favicon.icns',
    bundle_identifier=None,
)
