
try:
    import os, html2text
except Exception as e:
    print(e.args[-1].upper())
    if 'NO MODULE' in e.args[-1].upper():
        os.system('pip install '+e.args[-1].split(' ')[-1].replace("'",''))
    