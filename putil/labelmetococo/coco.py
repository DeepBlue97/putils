from .el_label_parser import ELLabelParser
from .el_label_name_config import label_names


class CocoAnnotation:
    def __init__(self, id_, image_id, segmentation, bbox, category_id, area, iscrowd):
        self.id_ = id_
        self.image_id = image_id
        self.segmentation = segmentation
        self.bbox = bbox
        self.category_id = category_id
        self.area = area
        self.iscrowd = iscrowd


class CocoImage:
    def __init__(self, file_name, height, width, id_):
        self.file_name = file_name
        self.height = height
        self.width = width
        self.id_ = id_


class CocoSuperCategory:
    def __init__(self, name):
        self.name = name


class CocoCategory:
    def __init__(self, name: str, supercategory: CocoSuperCategory, id_):
        self.name = name
        self.supercategory = supercategory
        self.id_ = id_


class CocoDataset:
    def __init__(self):
        self.images = []
        self.annotations = []
        self.categories = []
        self.elLabelParser = ELLabelParser(label_names)

    def get_category_id(self, name: str, supercategory_name: str):
        for category in self.categories:
            if name == category.name:
                return category.id_
        supercategory = CocoSuperCategory(name=supercategory_name)
        category = CocoCategory(name=name, supercategory=supercategory, id_=len(self.categories) + 1)
        return category.id_

    def load_labelme_format(self, data: dict):
        image = CocoImage(
            file_name=data['imagePath'],
            height=data['imageHeight'],
            width=data['imageWidth'],
            id_=len(self.images) + 1
        )

        for shape in data['shapes']:
            category_name = shape['label']
            supercategory_name = self.elLabelParser.get_supercategory_by_category(category_name)
            shape_type = shape['shape_type']

            segmentation = []
            x1 = min([i[0] for i in shape['points']])
            x2 = max([i[0] for i in shape['points']])
            y1 = min([i[1] for i in shape['points']])
            y2 = max([i[1] for i in shape['points']])
            if shape_type == 'polygon':

                for point in shape['points']:
                    segmentation += point

            elif shape_type == 'rectangle':
                segmentation = []
                x1 = min([i[0] for i in shape['points']])
                x2 = max([i[0] for i in shape['points']])
                y1 = min([i[1] for i in shape['points']])
                y2 = max([i[1] for i in shape['points']])
                segmentation = [
                    x1, y1,
                    x2, y1,
                    x2, y2,
                    x1, y2
                ]
            else:
                raise Exception

            annotation = CocoAnnotation(
                id_=len(self.annotations) + 1,
                image_id=image.id_,
                segmentation=segmentation,
                bbox=[(x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1],
                category_id=self.get_category_id(category_name, supercategory_name),
                area=0,
                iscrowd=0,
            )
            self.annotations.append(annotation)
