import os
from matplotlib import pyplot as pp
import detection


def main():
    current_dir = os.path.dirname(__file__)
    #with open(os.path.join(current_dir, "..", "data", "input")) as in_file:
    with open(os.path.join(current_dir, "..", "data", "result.dat")) as in_file:
        values = in_file.read().split()
        input_signal = [float(x) for x in values]
    result = detection.detect(input_signal, 1000)
    print("Hard Rate = " + str(result))
    pp.plot(input_signal)
    for peak in result:
        pp.axvline(peak, color="r")
    pp.show()

if __name__ == '__main__':
    main()
