import cv2 as cv
import numpy as np


def get_color_mask(image_hsv, hue, range=10):
    # color range to filter
    color_min = np.array([hue - range, 50, 50])
    color_max = np.array([hue + range, 255, 255])
    # create the mask
    mask = cv.inRange(image_hsv, color_min, color_max)
    return mask


def track_color_objects(frame_bgr):
    frame_hsv = cv.cvtColor(frame_bgr, cv.COLOR_BGR2HSV)
    cv.imshow("Cam", frame_bgr)

    def get_mask(hue, color_name):
        color_mask = get_color_mask(frame_hsv, hue)
        color_image = cv.bitwise_and(frame_bgr, frame_bgr, mask=color_mask)
        cv.imshow(f"mask_{color_name}", color_mask)
        cv.imshow(color_name, color_image)
        canny = cv.Canny(color_mask, 100, 200)
        cv.imshow(f"canny_{color_name}", canny)
        return color_mask

    masks = [
        get_mask(120, "blue"),
        get_mask(0, "red")
    ]
    i = iter(masks)
    masks_combined = next(i)
    for m in i:
        masks_combined = cv.bitwise_or(masks_combined, m)
    
    color_image = cv.bitwise_and(frame_bgr, frame_bgr, mask=masks_combined)
    cv.imshow(f"mask_combined", masks_combined)
    cv.imshow("combined", color_image)

    canny = cv.Canny(frame_bgr, 100, 200)
    cv.imshow("canny", canny)
    
    

def track_on_camera():
    camera = cv.VideoCapture(0)
    while True:
        found, frame_bgr = camera.read()
        if found:
            track_color_objects(frame_bgr)
            k = cv.pollKey()
            if k == 27:  # ESC
                cv.destroyAllWindows()
                break
        else:
            print("no frame")
            import time
            time.sleep(0.2)


def track_image(filename):
    img = cv.imread(filename)
    track_color_objects(img)
    while cv.waitKey(0) != 27:
        pass


def main():
    track_on_camera()
    
    # track_image(r"C:\Users\owwwt\OneDrive - HAN\Pictures\aapnootmies.jpg")
    # track_image(r"C:\temp\opencv-python\images\ballenbak.png")
    # track_image(r"C:\temp\opencv-python\images\abcde.jpg")

    # import glob
    # for f in glob.glob(r"C:\temp\opencv-python\images\*.*"):
    #     track_image(f)


if __name__ == '__main__':
    main()
