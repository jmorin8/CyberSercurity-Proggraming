from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os
from geopy.geocoders import Nominatim


def decodeBytes(var):
    var = var.strip(b'\x00')
    var = var.decode('utf-8')
    
    return var


def get_Exif(var):
    info = dict()
    
    image = Image.open(var)
    image_info = image._getexif() # get image bytes

    if image_info is not None:
        for tag,value in image_info.items():
            decoded = TAGS.get(tag, tag) # maps 16-bit integers to descriptive string names
            info[decoded] = value
        
        if 'MakerNote' in info.keys():
            del info['MakerNote'] # unuseful info (too long)


        # decode GPS INFO
        if  'GPSInfo' in info.keys():
            Nsec = info['GPSInfo'][2][2] 
            Nmin = info['GPSInfo'][2][1]
            Ndeg = info['GPSInfo'][2][0]
            Wsec = info['GPSInfo'][4][2]
            Wmin = info['GPSInfo'][4][1]
            Wdeg = info['GPSInfo'][4][0]
            
            if info['GPSInfo'][1] == 'N':
                Nmult = 1
            else:
                Nmult = -1
            
            if info['GPSInfo'][3] == 'E':
                Wmult = 1
            else:
                Wmult = -1
            
            Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
            Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
            info['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

            geloc = Nominatim(user_agent="GetLoc")
            lat = info['GPSInfo']['Lat']
            long= info['GPSInfo']['Lng']
            
            location = geloc.reverse(f"{lat},{long}")

            print(f'Image was taken in: {location}')

    
    # print gained metadata if values are in bytes decode it 
    for key, value in info.items():
        if type(value) == bytes:
            print('\t%s : %s' %(key,decodeBytes(value)))

        elif type(value) == dict:
            print('\t%s:' %key)
            
            for k,v in value.items():
                if type(v) == bytes:
                    print('\t\t%s : %s' %(k,decodeBytes(v)))
                else:
                    print('\t\t%s : %s' %(k,v))
        
        else:
            print('\t%s : %s' %(key,value))

    




def metadata():
    path = input("Ruta de imagenes: ")
    os.chdir(path) #change to given path

    for images in os.listdir():
        print('Metadata for: %s' %images)
        get_Exif(images)
        print('\n')



if __name__=="__main__":
    metadata()
