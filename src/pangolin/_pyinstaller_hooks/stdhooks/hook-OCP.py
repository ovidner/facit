from PyInstaller.compat import is_pure_conda

if is_pure_conda:
    from PyInstaller.utils.hooks import conda_support

    binaries = [(f.locate(), ".") for f in conda_support.files("ocp")]

else:
    import importlib

    binaries = [(importlib.util.find_spec("OCP").origin, ".")]
