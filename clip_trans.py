import googletrans
import clipboard
import keyboard

# create a Translator object
translator = googletrans.Translator()

# define the hotkey
hotkey = 'cmd+space'

# define the function to run when the hotkey is pressed
def translate():
    # get the text from the clipboard
    text = clipboard.paste()

    # detect the source language of the text
    src_lang = translator.detect(text).lang

    # define the target language
    if src_lang == 'en':
        dest_lang = 'ru'
    elif src_lang == 'ru':
        dest_lang = 'en'
    else:
        # use English as the default target language
        dest_lang = 'en'

    # translate the text
    translation = translator.translate(text, src=src_lang, dest=dest_lang)

    # print the translation
    print(translation.text)

    # copy the translation to the clipboard
    clipboard.copy(translation.text)

# register the hotkey
keyboard.add_hotkey(hotkey, translate)

# wait for the hotkey to be pressed
keyboard.wait()