import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from BOT import dmc_menu
    dmc_menu()
elif bit == '32bit':
    from BOT import dmc_menu
    dmc_menu()
