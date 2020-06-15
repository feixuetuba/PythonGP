import cv2

def show(func):
    def wrapper(*args, **kwargs):
        img = func(*args, **kwargs)
        cv2.namedWindow(func.__name__, cv2.WINDOW_NORMAL)
        cv2.imshow(func.__name__, img)
        cv2.waitKey(0)
        cv2.destroyWindow(func.__name__)
        return img
    return wrapper

def BGR2BGRA(image):
    """
    把图片转成RGBA
    :param image:
    :return:
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

def imopen(fpath):
    image = cv2.imread(fpath)
    if image is None:
        return None
    return  BGR2BGRA(image)