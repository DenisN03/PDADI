def bb2yolo(box, image_w, image_h):
    x1, y1, x2, y2 = box
    return [((x2 + x1)/(2*image_w)), ((y2 + y1)/(2*image_h)), (x2 - x1)/image_w, (y2 - y1)/image_h]

def yolo2bb(box, dw, dh):
    class_id, x_center, y_center, w, h = box.strip().split()
    x_center, y_center, w, h = float(x_center), float(y_center), float(w), float(h)
    x_center = round(x_center * dw)
    y_center = round(y_center * dh)
    w = round(w * dw)
    h = round(h * dh)
    x = round(x_center - w / 2)
    y = round(y_center - h / 2)

    return class_id, min(max(x,0),dw), min(max(y,0),dh), min(x+w,dw), min(y+h,dh)

def task2bb(cx, cy, r):
    x1 = cx - r
    x2 = cx + r
    y1 = cy - r
    y2 = cy + r
    return x1, y1, x2, y2

def flip_bbox(bbox, size, y_flip=False, x_flip=False):
    """Flip bounding boxes accordingly.
    Args:
        bbox (~numpy.ndarray): See the table below.
        size (tuple): A tuple of length 2. The height and the width
            of the image before resized.
        y_flip (bool): Flip bounding box according to a vertical flip of
            an image.
        x_flip (bool): Flip bounding box according to a horizontal flip of
            an image.
    .. csv-table::
        :header: name, shape, dtype, format
        :obj:`bbox`, ":math:`(R, 4)`", :obj:`float32`, \
        ":math:`(y_{min}, x_{min}, y_{max}, x_{max})`"
    Returns:
        ~numpy.ndarray:
        Bounding boxes flipped according to the given flips.
    """
    H, W = size
    bbox = bbox.copy()
    if y_flip:
        y_max = H - bbox[:, 3]
        y_min = H - bbox[:, 1]
        bbox[:, 3] = y_min
        bbox[:, 1] = y_max
    if x_flip:
        x_max = W - bbox[:, 2]
        x_min = W - bbox[:, 0]
        bbox[:, 2] = x_min
        bbox[:, 0] = x_max
    return bbox
