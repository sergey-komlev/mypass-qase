import os

# пробуем зайти на upass по TOKEN
class MyPass:
    TOKEN = os.getenv('MYPASS_TOKEN') if os.getenv('MYPASS_TOKEN') is not None else False
#    IS_DOC_UPDATE_NEEDED = True if os.getenv('MYPASS_DOC') == 'True' else False