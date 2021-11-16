#!/bin/bash
#
# Download images from a given website and extract metadata 
#
import argparse 
import os
import requests 
import bs4
from PIL import Image
from PIL.ExifTags import TAGS


def writeMetadata(metadata: dict, cwd):
    os.chdir(cwd)
    
    for key,value in metadata.items():
        # Slicing to change from original extension to txt extension
        filename = f'{key[:-4]}.txt' # Metadata will be saved with file name into txt file

        with open(filename, 'w') as fl:
            if type(value) == dict:
                fl.write('%s\n' %key)

                for k,v in value.items():
                    fl.write('\t%s : %s\n' %(k,v))
            else:
                fl.write('%s : %s\n' %(key,value))    


metadata = dict()
def getMetadata(cwd):
    print('\n[*] Getting metadata from downloaded images...')
    path = cwd+'\Images'

    os.chdir(path) #change to images dir
    for file in os.listdir():
        info = dict()
        
        image = Image.open(file)
        image_info = image._getexif() # get image bytes

        if image_info is not None:
            for tag,value in image_info.items():
                decoded = TAGS.get(tag, tag) # maps 16-bit integers to descriptive string names
                info[decoded] = value

        if len(info) > 0:
            print('\t[*] Extracting metadata for: %s' %file)        

            metadata[file] = info


def downloadImages(src: str):
    os.makedirs('Images', exist_ok=True)

    try:
        request = requests.get(src)
        
        if request.status_code == 200:
            print('\t[*] Downloading image: %s' %src)
            
            if '?' in src: 
                # delete query string and fragments from url
                image = open(os.path.join('Images', os.path.basename(src[:src.find('?')])), 'wb')
            else:
                image = open(os.path.join('Images', os.path.basename(src)), 'wb')

            for chunk in request.iter_content(100000):
                image.write(chunk)

            image.close()
    
    except requests.RequestException as e: 
        print('\t\t[ERROR] %s' %e)


def getSrc(request: str, url: str):
    print('[*] Searching for images in website...')

    soup = bs4.BeautifulSoup(request.text, "html.parser")

    img = soup.select('div img', class_='newpage')

    if img ==[]:
        print('\t[*] No images found')
    else:
        for i in range(len(img)):
            try:
                if not "es." in img[i]:
                    src = (img[i].get('src')) # if error occurs analyze source code and change src

                    if not src.startswith('http'):
                        src = url+src

                    downloadImages(src) # source image (link)

            except:
                print('\t[ERROR] Can not get src %s' %src)


def doRequest(url: str):
    try:
        request = requests.get(url)

        if request.status_code == 200:
            getSrc(request,url)

    except requests.RequestException as e:
        print('\t[ERROR] %s' %e)

 
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser .add_argument('-u', '--url',
                        help='url to analyze',
                        required=True
                        )

    params = parser.parse_args()
    
    url = params.url
    cwd = os.getcwd()

    doRequest(url)
    #getMetadata(cwd)
    #writeMetadata(metadata, cwd)
    print('\n[*] Script executed successfully')