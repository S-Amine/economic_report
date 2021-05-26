import urllib.request
from urllib.parse import urlparse
import ssl
import json

# open url files
json_file = open('ons_pdf.json')
data = json.load(json_file)
# download pdfs
print("downloading...")
num = 0
for link in data :
    num += 1
    url = link['file_urls'][0]
    parse = urlparse(url)
    print(num , 'the file:', str(parse.path), 'is downloading')
    req = urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' })
    gcontext = ssl.SSLContext()  # Only for gangstars
    info = urllib.request.urlopen(req, context=gcontext)

    # file download
    path = parse.path
    name = path.replace(".pdf", "")
    filename = '.{}'.format(name)
    file = open(filename + ".pdf", 'wb')
    file.write(info.read())
    file.close()
    print('the download of:', str(parse.path), 'is finished')
