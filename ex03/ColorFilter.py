from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker
import numpy as np

class ColorFilter:
    def invert(self, array):
        return 1 - array

    def to_blue(self, array):
        res = np.zeros(array.shape)
        for y in range(len(res)):
            for x in range(len(res[y])):
                res[y][x][2] = array[y][x][2]
        return res

    def to_green(self, array):
        res = np.zeros(array.shape)
        for y in range(len(res)):
            for x in range(len(res[y])):
                res[y][x][1] = array[y][x][1]
        return res

    def to_red(self, array):
        res = np.zeros(array.shape)
        for y in range(len(res)):
            for x in range(len(res[y])):
                res[y][x][0] = array[y][x][0]
        return res

    def celluloid(self, array):
        res = array.copy()
        tmp = np.linspace(0.0,1.0, num=4, retstep=True)
        for y in range(len(res)):
            for x in range(len(res[y])):
                for z in range(len(res[y][x])):
                    if abs(res[y][x][z] - tmp[0][0]) < abs(res[y][x][z] - tmp[0][1]):
                        res[y][x][z] = tmp[0][0]
                    elif abs(res[y][x][z] - tmp[0][1]) < abs(res[y][x][z] - tmp[0][2]):
                        res[y][x][z] = tmp[0][1]
                    elif abs(res[y][x][z] - tmp[0][2]) < abs(res[y][x][z] - tmp[0][3]):
                        res[y][x][z] = tmp[0][2]
                    else:
                        res[y][x][z] = tmp[0][3]
        return res

if __name__ == "__main__":
    imp = ImageProcessor()
    cf = ColorFilter()
    sb = ScrapBooker()

    arr = imp.load("./elonmusk.png")

    #invert = cf.invert(arr)
    celluloid = cf.celluloid(arr)
    #blue_arr = cf.to_blue(arr)
    #green_arr = cf.to_green(arr)
    #red_arr = cf.to_red(arr)

    resa = np.concatenate((arr, celluloid), 1)
    #resb = np.concatenate((invert, blue_arr), 1)
    #resc = np.concatenate((green_arr, red_arr), 1)
    #res = np.concatenate((resa, resb, resc), 0)
    imp.display(resa)
