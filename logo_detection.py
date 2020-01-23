import sys
import cv2
import numpy as np

from tests.pythonLogoDetection import video


def get_polygon_Frame(img2):
    # img1 = cv2.imread('images/cup.png', 0)
    img1 = cv2.imread('images/respawn_logo.png', 0)
    # img2 = cv2.imread('sypher_cup.png', 0)

    MIN_MATCH_COUNT = 10

    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        # matchesMask = mask.ravel().tolist()
        h, w = img1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        try:
            dst = cv2.perspectiveTransform(pts, M)
            img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
            return img2
        except:
            print("Error")
            return img2
    else:
        # print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
        # matchesMask = None
        return img2

class App:
    def __init__(self, src):
        self.cap = video.create_capture(src)
        self.frame = None

    def run(self):
        count = 0
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            # self.frame = frame.copy()
            vis = frame.copy()

            # add in polygon
            vis = get_polygon_Frame(vis)

            # cv2.imshow('plane', vis)
            cv2.imwrite("stage/frame{}.png".format(str(count).zfill(4)), vis)
            count += 1

            # ch = cv2.waitKey(1) & 0xFF
            # if ch == 27:
            #     break


if __name__ == '__main__':
    try:
        video_src = sys.argv[1]
        # video_src = '440478286_10sec_show.mp4'
        # video_src = '440478286_short.mp4'
    except:
        video_src = 0
    App(video_src).run()

    # tseting
    # vidcap = cv2.VideoCapture(video_src)
    # success, image = vidcap.read()
    # count = 0
    # while success:
    #     cv2.imwrite("stage/frame{}.png".format(str(count).zfill(4)), image)
    #     success, image = vidcap.read()
    #     count += 1