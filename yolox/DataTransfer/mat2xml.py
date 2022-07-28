
import os
import cv2
from scipy import io
from lxml import etree, objectify

mat_path = "../mydata/test/labels/"
images_path = "../mydata/test/images/"
save_path = "../mydata/test/xmls/"
images_nums = 0
category_nums = 0
bbox_nums = 0
category_nums = 1
category_name = "flower"

mat_files = os.listdir(mat_path)


# print(len(mat_files))
# print(mat_files[0])


def save_anno_to_xml(filename, size, objs, save_path):
    E = objectify.ElementMaker(annotate=False)
    anno_tree = E.annotation(
        E.folder("DATA"),
        E.filename(filename+".jpg"),
        E.source(
            E.database("The VOC Database"),
            E.annotation("PASCAL VOC"),
            E.image("flickr")
        ),
        E.size(
            E.width(size[1]),
            E.height(size[0]),
            E.depth(size[2])
        ),
        E.segmented(0)
    )
    for obj in objs:
        E2 = objectify.ElementMaker(annotate=False)
        anno_tree2 = E2.object(
            E.name(obj[0]),
            E.pose("Unspecified"),
            E.truncated(0),
            E.difficult(0),
            E.bndbox(
                E.xmin(obj[1][0]),
                E.ymin(obj[1][1]),
                E.xmax(obj[1][2]),
                E.ymax(obj[1][3])
            )
        )
        anno_tree.append(anno_tree2)
    anno_path = os.path.join(save_path, filename + ".xml")
    etree.ElementTree(anno_tree).write(anno_path, pretty_print=True)


# 由(x,y,w,h)--->(x,y,x,y)
# def xywh2xyxy(bbox):
#     bbox = list(map(float, bbox))
#     # size = list(map(float, size))
#     xmin = (bbox[0] - bbox[2] / 2.)
#     ymin = (bbox[1] - bbox[3] / 2.)
#     xmax = (bbox[0] + bbox[2] / 2.)
#     ymax = (bbox[1] + bbox[3] / 2.)
#     box = [xmin, ymin, xmax, ymax]
#     return list(map(float, box))

def xywh2xyxy(bbox):
    bbox = list(map(int, bbox))
    # size = list(map(float, size))
    xmin = bbox[0]
    ymax = bbox[1] + bbox[3]
    xmax = bbox[0] + bbox[2]
    ymin = bbox[1]
    box = [xmin, ymin, xmax, ymax]
    return list(map(int, box))


def parseXmlFilse():
    global images_nums, category_nums, bbox_nums
    images = []
    for i in range(len(mat_files)):
        data = io.loadmat('../mydata/test/labels/' + mat_files[i])
        info = data['annotation']
        filename = info[0][0][0][0]
        filename_path = images_path + filename + '.jpg'
        img = cv2.imread(filename_path)
        shape = img.shape
        images.append(filename_path)

        position = info[0][0][1]
        objects = []
        for j in range(len(position)):
            item = position[[j]]
            bbox = xywh2xyxy(item[0])
            obj = [category_name, bbox]
            objects.append(obj)
        # filename = filename+".jpg"
        bbox_nums += len(objects)
        save_anno_to_xml(filename, shape, objects, save_path)
    images_index = dict((v.split(os.sep)[-1][:-4], k) for k, v in enumerate(images))
    images_nums = len(images)

# print("filename:", filename)
# print("info", info)
# print("position", position)
# print("item", item, item.shape, item[0])

# print("features",  info[0][0][0][1])

# filename:XAM01_YM_20150805100255_01
# position :[[4.00510e+02 7.96510e+02 1.09980e+02 1.33980e+02]   numpy
#  [3.23510e+02 1.24751e+03 1.69980e+02 2.51980e+02]
#  [1.57510e+02 1.97651e+03 1.86980e+02 1.65980e+02]]


if __name__ == '__main__':
    """
    脚本说明：
        本脚本用于将yolo格式的标注文件.txt转换为voc格式的标注文件.xml
    参数说明：
        anno_path:标注文件txt存储路径
        save_path:json文件输出的文件夹
        image_path:图片路径
    """
    parseXmlFilse()
    print("image nums: {}".format(images_nums))
    print("category nums: {}".format(category_nums))
    print("bbox nums: {}".format(bbox_nums))
