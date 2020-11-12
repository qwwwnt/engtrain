import pathlib
import shutil
import os
import requests

path = str(pathlib.Path().absolute()) + '\\maps'
print(path)

try:
    shutil.rmtree(path)
except OSError:
    print("Detection of the directory %s failed" % path)    
else:
    print("Successfully deleted the directory %s" % path)    

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)    
else:
    print("Successfully deleted the directory %s" % path) 

# https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST4/L3/2020/0902/AQUA_MODIS.20200902.L3m.DAY.SST4.sst4.4km.NRT.nc.png

namesp = {'4km':'4km','9km': '9km'}

namesk = []
    
dates = []
i = 0
while i < 18:
    dates.append(903+i)
    namesk.append(20200903+i)
    i += 1

for key in namesp:

    namesPath = path + '\\' + key

    try:
       shutil.rmtree(namesPath)
    except OSError:
       print("Detection of the directory %s failed" % namesPath)    
    else:
       print("Successfully deleted the directory %s" % namesPath)    

    while i < 18:
        name = str(namesk[i]) + '.png'
        r = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST4/L3/2020/0' + str(dates[i]) + '/AQUA_MODIS.20200' + str(dates[i]) + '.L3m.DAY.SST4.sst4.' + namesp[key] + '.NRT.nc.png', allow_redirects=True)
        open(namesPath + '/' + name, 'wb' ).write(r.content)
        i += 1

