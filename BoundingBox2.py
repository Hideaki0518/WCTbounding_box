import sys
import cv2
import numpy as np

if __name__ == "__main__":
    """
        xmin ymin xmax ymax
    apple, 174, 253, 285, 357  
    winelass, 363, 5, 454, 378
    """
    xmin = 363
    ymin = 5
    xmax = 454
    ymax = 378
    blue_thresh = 60
    red_thresh = 30
    gray_thresh = 60
    img = cv2.imread("yoloimg.png")
    # img = cv2.rectangle(img, (363,5), (454,378 ), (255, 0, 0))


    print(img.shape)

    flag = 0
    before_sum_bgr = 0
    diff = 0
    for x in range(, max):
        sum_b = np.sum(img[xmin:xmax, , 0], 1) #行の和取得
        sum_g = np.sum(img[xmin:xmax, , 1], 1)
        sum_r = np.sum(img[y, xmin:xmax,2], )
        sum_bgr = sum_b + sum_g +sum_r
        if flag < 2:
            sum_bgr += sum_bgr
            flag += 1
        else:
            diff = abs(before_sum_bgr - sum_bgr)
            before_sum_bgr = sum_bgr

            flag = 0
            sum_bgr = 0
        if diff > 4294967100:
            img[y, xmin:xmax] = (0, 0, 0)


        print(diff)

                #print(blue)
                #img.itemset((y, x, 0), 0)
                #img.itemset((y, x, 1), 0)
                #img.itemset((y, x, 2), 0)



    cv2.imwrite("output.png", img)
