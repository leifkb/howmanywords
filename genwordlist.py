import json

with open('/usr/share/dict/words') as wl:
    words = [word.strip() for word in wl]

with open('wordlist.js', 'w') as wl_js:
    wl_js.write('const ALL_WORDS = ')
    wl_js.write(json.dumps(words))
    wl_js.write(';\n')
