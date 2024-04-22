import matplotlib.pyplot as plt

def floodfill(map: list, x_pos:int, y_pos: int):
    row_border = map.shape[0]
    column_border = map.shape[1]

    if ((row_border >= x_pos >= 0) and
            column_border >= y_pos >= 0):
        if map[x_pos, y_pos] == 0:
            return map
        elif map[x_pos, y_pos] == 1:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    map[x_pos, y_pos] = 2
                    map = floodfill(map=map, x_pos=x_pos+i, y_pos=y_pos+j)
                    return map
        else:
            return map
    else:
        return map

def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(50)
    plt.clf()


if __name__ == "__main__":
    main()
