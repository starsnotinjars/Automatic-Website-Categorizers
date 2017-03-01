# 1. `pip install microsofttranslator` (see https://github.com/openlabs/Microsoft-Translator-Python-API for more info)
# 2. create account per https://www.microsoft.com/en-us/translator/getstarted.aspx
# 3. set environment variables CLIENT_ID / CLIENT_SECRET with details from Microsoft account. ex: export from ~/.bashrc
# 4. call this script with string to translate. ex: `python translation.py Su capital es la Ciudad de México`

import os
import sys

try:
  client_id = os.environ['CLIENT_ID']
except Exception as e:
  print "ERROR: no environment variable set for {0}".format(str(e))
  client_id = ''

try:
  client_secret = os.environ['CLIENT_SECRET']
except Exception as e:
  print "ERROR: no environment variable set for {0}".format(str(e))
  client_secret = ''

if len(sys.argv) < 2:
  sys.exit()

string_to_translate = ' '.join(sys.argv[1:])

try:
  from microsofttranslator import Translator
  translator = Translator(client_id, client_secret)
  response = translator.translate(string_to_translate, 'en')
  print "RESPONSE: {0}".format(str(response))

  # more details available at: https://docs.microsofttranslator.com/text-translate.html

except Exception as e:
  print "ERROR: {0}".format(str(e))
  sys.exit()
