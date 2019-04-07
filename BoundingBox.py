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

    criterion_xmin =174
    criterion_ymin =253
    criterion_xmax =285
    criterion_ymax =357

    print(img.shape)

    flag = 0
    before_sum_bgr = 0
    diff = 0
    b = 0
    g = 0
    r = 0
    bp = 0
    gp = 0
    rp = 0
    sum_line = 5

    thresh = 50000  # memo 50000

    # 基準についての処理
    cv2.rectangle(img, (criterion_xmin,criterion_ymax), (criterion_xmax, criterion_ymin), (76, 84, 255), 2) #基準を資格で囲む
    cv2.putText(img, 'Criterion', (criterion_xmin-15, criterion_ymin), cv2.FONT_ITALIC, 1, (0, 0, 255))
    cv2.putText(img, 'Target', (xmin - 5, ymax+25), cv2.FONT_ITALIC, 1, (255, 0, 0))


    # ワイングラスについての処理

    cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (255, 139, 0), 2)
    for y in range(ymin, ymax):
        if (ymin - y) % 10 == 0:    # 10行ごとにラインを引く
            img[y, xmin:xmax] = (0, 0, 0)

        count = xmax - xmin  # 横幅のピクセル数
        sum_b = np.sum(img[y, xmin:xmax, 0], 0) / count  # 行の和の平均
        sum_g = np.sum(img[y, xmin:xmax, 1], 0) / count
        sum_r = np.sum(img[y, xmin:xmax, 2], 0) / count

        if flag < sum_line-1:  # sum_line行ずつ 上で求めた行の和を足す。
            b += sum_b
            g += sum_g
            r += sum_r
            flag += 1
        else:
            diff = (bp - b) ** 2 + (gp - g) ** 2 + (rp - r) ** 2  # sum_line行ずつ diffを計算する。
            # print(y , "y")
            # print(diff  ,"diff")
            print("{0:4d}".format(y), "{0:6d}".format(int(diff)), int(bp), int(b), int(gp), int(g), int(rp), int(r))
            bp = b
            gp = g
            rp = r
            if diff > thresh:
                # img[y-sum_line, xmin:xmax] = (255, 255, 255)  # 閾値を超えたら描画
                cv2.line(img,(xmin,(114-sum_line)),(xmax,(114-sum_line)), (255, 255, 255),2)# 閾値を超えたら描画 水面
                cv2.line(img, (xmin, (209 - sum_line)), (xmax, (209 - sum_line)), (255, 255, 255), 2) # 閾値を超えたら描画 ポイント
                #img[114 - sum_line, xmin:xmax] = (255, 255, 255)  # 閾値を超えたら描画 水面
                #img[209 - sum_line, xmin:xmax] = (255, 255, 255)  # 閾値を超えたら描画 ポイント
                #print('over thresh line = ', y)
                m = 1

            b = g = r = 0
            flag = 0
    print('water width: ', xmax-xmin, 'water height: ', 209 - 114)
    # img[378, xmin:xmax] = (255, 255, 255)
    # img[319, xmin:xmax] = (255, 255, 255)
    # img[ymin, xmin:xmax] = (255, 0, 0)


    cv2.imwrite("output.png", img)
