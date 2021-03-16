import urllib.request
from tqdm import tqdm
from time import sleep


#def download_retry(url, path):
#    while True:
#        try:
#            urllib.request.urlretrieve(url, path)
#        except urllib.error.HTTPError:
#            sleep(10)
#            continue
#        break


def download(data):
    for line in tqdm(data):
        while True:
            try:
                urllib.request.urlretrieve(line[0], line[1])
            except urllib.error.HTTPError:
                sleep(10)
                continue
            break
        #download_retry(line[0], line[1])
