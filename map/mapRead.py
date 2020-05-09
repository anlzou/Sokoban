'''
 * @author  anlzou
 * @date  2020/5/9 15:30
 * @version xx
 * @description xx
'''

def mapRead():
    mapFile = open("../resource/map.txt")
    mapArray = []

    while True:
        line = mapFile.readline()
        if line == "":
            break
        line = line.replace("\n","")
        mapArray.append(line.split(","))
    mapFile.close()

    for i in range(len(mapArray)):
        print(mapArray[i])