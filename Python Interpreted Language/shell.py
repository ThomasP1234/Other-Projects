# TODO: see TODO in ERL.py
#       fix syntax, 
#       add remaining features from file:///D:/Data/Downloads/ocr-exam-reference-language-cheatsheet-poster.pdf
#       sort all error eg. Syntax Error Code output
# TODO config file to edit default keybinds (IDE)
# On finish change to .pyw to hide console

import ERL

def run():
    ERL.cleanup()
    while True:
      text = input('ERL >>> ')
      if text.strip() == "": continue
      result, error = ERL.run('<stdin>', text+"\n")

      if error: 
        print(error.as_string())
      elif result: 
        if len(result.elements) == 1:
          print(repr(result.elements[0]))
        else:
          print(repr(result))

if __name__ == "__main__":
	run()