# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['excel_to_unl_converter.py'],
    pathex=[],
    binaries=[],
    datas=[('version.py', '.'), ('samples\\4.unl', 'samples'), ('samples\\bvov10105000002510160001.unl', 'samples'), ('samples\\bvov23104700002505210001 (1).unl', 'samples'), ('samples\\bvov23104700002505210001.unl', 'samples'), ('samples\\bvov2510210001.unl', 'samples'), ('samples\\CNTR_PRIMAIR.xlsx', 'samples'), ('samples\\cntr.docx', 'samples')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Excel_to_UNL_Converter',
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
)
