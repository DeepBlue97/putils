from .labelme_parser import (Category, SuperCategory)


class ELLabelParser:
    """
    解析[[]]格式的label
    """
    def __init__(self, label_names):
        self.raw_label_names = label_names
        self.supercategories = [SuperCategory(i[0]) for i in label_names]
        self.categories = []
        for s_i, names in enumerate(label_names):
            for c_i, name in enumerate(names):
                category = Category(supercategory=self.supercategories[s_i], id_=len(self.categories)+1, name=name)
                self.categories.append(category)

    # def get_categories(self):
    #     return self.categories
    #
    # def get_supercategories(self):
    #     return self.supercategories

    def get_supercategory_by_category(self, name):
        """ 查询是否存在父类，不存在则直接返回name作为父类 """
        for names in self.raw_label_names:
            if name in names:
                return names[0]
        return name
