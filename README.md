# Clipboard Translator
A simple Python program that translates text on the clipboard when a hotkey is pressed.

!WARNING! This project fully created by ChatGPT from Open.AI.

## Installation
To install the necessary Python packages for this program, run the following command:

## Install the necessary Python packages
    pip install -r requirements.txt
This command will install the clipboard, googletrans, and keyboard modules, which are required for the program to run.

## Usage
To use the program, run the following command:

    python translate.py
This will start the program and register the hotkey. To trigger the translation, press the hotkey combination ctrl+shift+a. This will translate the text on the clipboard, print the translation, and copy the translation back to the clipboard.

You can customize the hotkey by modifying the hotkey variable in the translate.py file. You can also modify the source and target languages for the translation by modifying the src_lang and dest_lang variables in the translate() function.

## License
This program is licensed under the MIT License. See LICENSE for more details.
