# TODO: Files
# TODO: https://youtu.be/zKCckdwwBsU

import ERL

def run():
    while True:
      text = input('ERL >>> ')
      result, error = ERL.run('<stdin>', text)

      if error: print(error.as_string())
      elif result: print(repr(result))

if __name__ == "__main__":
	run()