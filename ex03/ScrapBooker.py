import numpy as np


class ScrapBooker:
    def crop(self, array, dim, pos=(0,0)):
        if dim[0] + pos[0] > len(array) or dim[1] + pos[1] > len(array[0]):
            raise Exception
        new_arr = arr.tolist()
        new_arr = new_arr[pos[0]:]
        for i in range(len(new_arr)):
            new_arr[i] = new_arr[i][pos[1]:]
        new_arr = new_arr[:dim[0]]
        for i in range(len(new_arr)):
            new_arr[i] = new_arr[i][:dim[1]]
        return np.array(new_arr)

    def thin(self, array, n, axis):
        return np.delete(array, list(range(0, array.shape[0], n)), axis)

    def juxtapose(self, array, n, axis=0):
        res = array
        while (n > 1):
            res = np.concatenate((res, array), axis)
            n -= 1
        return res

    def mosaic(self, array, dim):
        res = self.juxtapose(array, dim[0], 1)
        res = self.juxtapose(res, dim[1], 0)
        return res
