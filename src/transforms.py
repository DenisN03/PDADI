from iou import bb_intersection_over_union, contains
from markup_convertors import bb2yolo
import cv2

def crop(image, ROWS, COLS, w_step, h_step, variant, img_path, img_back_path, markup, filename):
    for i in range(0,ROWS):
        for j in range(0,COLS):
            
            y_0 = int(w_step*i)
            y_1 = int(w_step*i + w_step)
            x_0 = int(h_step*j)
            x_1 = int(h_step*j + h_step)
            
            if variant == "C":
                x_0 = int(h_step*j + 0.5 * h_step)
                x_1 = int(h_step*j + 1.5 * h_step)
            elif variant == "R":
                y_0 = int(w_step*i + 0.5 * w_step)
                y_1 = int(w_step*i + 1.5 * w_step)

            cimage = image[y_0:y_1, x_0:x_1]

            mkp2file = []
            accept = []
            for bbox in markup:
                iou = bb_intersection_over_union([x_0, y_0, x_1, y_1], bbox[1:])
                contain = contains([x_0, y_0, x_1, y_1], bbox[1:])
                # print(iou, contain)
                if iou != 0 and contain == True:
                    accept.append(0)
                    resizebbox = [bbox[1] - x_0, bbox[2] - y_0, bbox[3] - x_0, bbox[4] - y_0]
                    mkp2file.append(bb2yolo(resizebbox, h_step, w_step))
                elif iou == 0:
                    accept.append(0)
                else:
                    accept.append(1)

            # print("accept",accept, sum(accept))
            if sum(accept) == 0:
                if len(mkp2file) == 0:
                    lbl_p = img_back_path.replace("images","labels")
                    img_p = img_back_path
                else:
                    lbl_p = img_path.replace("images","labels")
                    img_p = img_path
                save_name = f'{filename}_{i}_{j}_{variant}'
                with open(f'{lbl_p}{save_name}.txt', "w") as f:
                    for mkp in mkp2file:
                        mkp = [str(x) for x in mkp]
                        f.write("0 " + " ".join(mkp) + "\n")
                        # mkp = "0 " + " ".join(mkp) + "\n"
                        # bbox = yolo2bb(mkp, h_step, w_step)
                        # cv2.rectangle(cimage,(bbox[1],bbox[2]),(bbox[3],bbox[4]),(0,255,0), 3)
                cv2.imwrite(f'{img_p}{save_name}.jpg', cimage)
                
                
def crop_submission(ROWS, COLS, w_step, h_step, variant):
    for i in range(0,ROWS):
        for j in range(0,COLS):
            
            y_0 = int(w_step*i)
            y_1 = int(w_step*i + w_step)
            x_0 = int(h_step*j)
            x_1 = int(h_step*j + h_step)
            
            if variant == "C":
                x_0 = int(h_step*j + 0.5 * h_step)
                x_1 = int(h_step*j + 1.5 * h_step)
            elif variant == "R":
                y_0 = int(w_step*i + 0.5 * w_step)
                y_1 = int(w_step*i + 1.5 * w_step)


            yield y_0,y_1, x_0,x_1
