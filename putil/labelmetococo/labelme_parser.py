import json


class SuperCategory:
    def __init__(self, name: str):
        self.name = name


class Category:
    def __init__(self, supercategory: SuperCategory, id_: int, name: str):
        self.supercategory = supercategory
        self.id_ = id_
        self.name = name


class Annotation:
    def __init__(self, image_id: int, bbox: list, segmentation: list, iscrowd: int):
        self.image_id = image_id
        self.bbox = bbox
        self.segmentation = segmentation
        self.iscrowd = iscrowd


class Image:
    def __init__(self, file_name: str, id_: int, height: int, width: int):
        self.file_name = file_name
        self.id_ = id_
        self.height = height
        self.width = width


class LabelmeParser:
    def __init__(self, json_file):

        self.mix_coding_error = 0
        json_dict = None

        f = open(json_file, 'r', encoding='utf-8')
        try:
            json_dict = json.loads(f.read())

            for shape in json_dict['shapes']:
                if shape['label'] == 'ˮӡ':
                    f = open(json_file, 'r', encoding='gbk')
                    json_dict = json.loads(f.read())
                    break

        except UnicodeDecodeError:
            try:

                f = open(json_file, 'r', encoding='gbk')
                json_dict = json.loads(f.read())
            except UnicodeDecodeError:
                self.mix_coding_error += 1

        # f = open(json_file, 'r', encoding='gbk')
        # try:
        #     json_dict = json.loads(f.read())
        # except UnicodeDecodeError:
        #     f = open(json_file, 'r', encoding='utf-8')
        #     json_dict = json.loads(f.read())

        self.json_dict = json_dict
        self.imagePath = json_dict['imagePath']
        self.imageHeight = json_dict['imageHeight']
        self.imageWidth = json_dict['imageWidth']
        self.shapes = json_dict['shapes']
