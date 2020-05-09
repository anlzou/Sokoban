'''
 * @author  anlzou
 * @date  2020/5/9 15:38
 * @version xx
 * @description xx
'''

def mapWrite(n):
    lineEnd = "\n";
    mapFile = open("../resource/map.txt","w")

    for i in range(n):
        mapArray = ""
        for j in range(n):
            mapArray += "0"
            if j != n-1:
                mapArray += ","
        mapArray += lineEnd;
        mapFile.write(mapArray)

    mapFile.close()