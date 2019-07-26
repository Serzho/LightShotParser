import httplib2
import time
import re
url = 'https://prnt.sc/lzpfeg'

start = time.time()

h = httplib2.Http('.cache')
response, content = h.request(url)
pattern = r"([\w\.-]+)((.jpg)|(.png))"
image_name = re.search(pattern, str(content)).group()
print("Image Url: %s" % image_name)
response, content = h.request('https://image.prntscr.com/image/' + image_name)
out = open(image_name, 'wb')
out.write(content)
out.close()

end = time.time() - start
print(end)





