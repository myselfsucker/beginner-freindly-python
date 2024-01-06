from sys import argv
import pyperclip
TEXT = {
         "busy":"""sorry right now i am extremely busy""",
         'hi':'''vaalaykum assalom ha yaxshi raxmat o'zizchi'''
}
keyPhrase = argv[1]

if keyPhrase in TEXT:
         text = pyperclip.copy(TEXT[keyPhrase])
         print(f'the text for {keyPhrase} has been sucessfully copied to the clip board')
else:
        print('there is no such key phrase')
