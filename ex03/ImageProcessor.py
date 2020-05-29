import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:
    def load(self, path):
        arr = mpimg.imread(path)
        print("Loading image of dimensions %d x %d" % (len(arr), len(arr[0])))
        return arr

    def display(self, array):
        plt.imshow(array, interpolation='nearest')
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("./42AI.png")
    print(arr)
    imp.display(arr)
