import os
import cv2
import numpy as np
import time


# get how far we should move the slide block
def get_move_step(icon_path=None, background_path=None):

    if not os.path.exists(icon_path):
        raise Exception('icon path does not exist %s' % str(icon_path))

    if not os.path.exists(background_path):
        raise Exception('icon path does not exist %s' % str(background_path))

    img_icon = cv2.imread(icon_path, 0)
    w_icon, h_icon = img_icon.shape[::-1]

    # we need to remove the icon part from the original background
    img_background_original = cv2.imread(background_path)
    (h_bg, w_bg, d_bg) = img_background_original.shape
    img_background = img_background_original[:, w_icon:w_bg]
    # img_background = img_background_original

    # change the background to grey one.
    img_background_gray = cv2.cvtColor(img_background, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_background_gray, img_icon, cv2.TM_CCOEFF_NORMED)

    # 使用二分法查找阈值的精确值
    run = 1
    L = 0
    R = 1
    while run < 20:
        run += 1
        threshold = (R + L) / 2
        # print(threshold)
        if threshold < 0:
            print('Error')
            return None
        loc = np.where(res >= threshold)
        # print(len(loc[1]))
        if len(loc[1]) > 1:
            L += (R - L) / 2
        elif len(loc[1]) == 1:
            print('目标区域起点x坐标为：%d' % (loc[1][0] + w_icon))
            return loc[1][0] + w_icon
            # break
        elif len(loc[1]) < 1:
            R -= (R - L) / 2
    if run == 20:
        print('failed to recognize the img %s' % icon_path)
        return
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_background, pt, (pt[0] + w_icon, pt[1] + h_icon), (7, 279, 151), 2)
    cv2.imshow('Dectected', img_background)
    # cv2.waitKey(0)
    time.sleep(2)
    cv2.destroyAllWindows()
    return loc[1][0] + w_icon

if __name__ == '__main__':
    icon_path = "icon.png"
    background_path = "bg.png"

    x = get_move_step(icon_path, background_path)
    print(x)



