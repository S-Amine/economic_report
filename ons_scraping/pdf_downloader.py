import urllib.request
from urllib.parse import urlparse
import ssl
import json

# open url files
json_file = open('ons_pdf.json')
data = json.load(json_file)
# download pdfs
for link in data :
    url = link['file_urls'][0]
    req = urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' })
    gcontext = ssl.SSLContext()  # Only for gangstars
    info = urllib.request.urlopen(req, context=gcontext)

    # file download
    parse = urlparse(url)
    test = str(parse.path)
    filename = '.{}'.format(test)
    file = open(filename + ".pdf", 'wb')
    file.write(info.read())
    file.close()
