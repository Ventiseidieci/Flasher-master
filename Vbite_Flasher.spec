# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['cli.py'],
    pathex=[],
    binaries=[],
    datas=[('Flasher/GUI/images/favicon.icns', 'Flasher/GUI/images/'), ('Flasher/GUI/mainUI.qml', 'Flasher/GUI/'), ('esp_idf/.', 'esp_idf/.'), ('Flasher/configuration/*.csv', 'Flasher/configuration/'), ('Flasher/configuration/*.bin', 'Flasher/configuration/')],
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
    [],
    exclude_binaries=True,
    name='Vbite_Flasher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Vbite_Flasher',
)
app = BUNDLE(
    coll,
    name='Vbite_Flasher.app',
    icon='favicon.icns',
    bundle_identifier=None,
)
