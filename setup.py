from cx_Freeze import setup, Executable

base = None    

executables = [Executable("atm.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ATM",
    options = options,
    version = "0.1",
    description = 'ATM With Python',
    executables = executables
)