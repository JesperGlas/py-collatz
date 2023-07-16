import sys
import numpy as np
import matplotlib.pyplot as plt

def main():
    # make sure that a value is included in call
    if len(args := sys.argv) != 2:
        sys.exit("Please provide a value for the Collatz problem!")

    # validate that argument is an integer
    #   if so, save it
    try:
        value: int = int(args[1])
    except ValueError:
        sys.exit("Please provide an integer!")

    # populate Collatz data
    data: list[int] = [value]
    while value != 1:
        value = value // 2 if (value % 2) == 0 else 3 * value + 1
        data.append(value)

    # create plot data
    xaxis = np.array([x for x in range(len(data))])
    yaxis = np.array(data)

    # create plot
    plt.plot(xaxis, yaxis)
    plt.xlabel(f"Step (total {len(xaxis)})")
    plt.ylabel(f"Value (max {max(data)})")
    plt.show()



if __name__ == "__main__":
    main()
