import json
import sys
from time import strftime

inputFileName = input('enter json file name: ')

timestr = strftime('%Y%m%d-%H%M%S')

sys.stdout = open(timestr+'.json', 'w')

sys.stdout.write('[')

with open(inputFileName+'.json') as data_file:
    data = json.load(data_file)
    for v in data.values():
        try:
            print('{\"filename\":\"' + v['filename'],'\",\"object\":{\"bndbox\":{\"xmin\":' + str(v['regions'][0]['shape_attributes']['x']), ',\"ymin\":' + str(v['regions'][0]['shape_attributes']['y']), ',\"xmax\":' + str(v['regions'][0]['shape_attributes']['x'] + v['regions'][0]['shape_attributes']['width']), ',\"ymax\":' + str(v['regions'][0]['shape_attributes']['y'] + v['regions'][0]['shape_attributes']['height'])+'}}},')
        except Exception:
            pass

sys.stdout.write(']')

sys.stdout.close()
