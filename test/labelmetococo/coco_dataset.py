from putil.labelmetococo.coco import CocoDataset

# CocoDataset()


root_dir = r'D:\workspace\data\总数据集'

import glob

from putil.labelmetococo.labelme_parser import LabelmeParser
from putil.labelmetococo.coco import CocoDataset

json_files = glob.glob(r'D:\workspace\data\总数据集\*\*.json', )

cocoDataset = CocoDataset()

shuiyin_error_count = 0

label_set = set()
for json_file in json_files:
    lp = LabelmeParser(json_file=json_file)
    # for shape in lp.json_dict['shapes']:
    #     label_set.add(shape['label'])
    #     if shape['label'] == 'ˮӡ':
    #         shuiyin_error_count += 1
    #         # raise Exception
    # # cocoDataset.load_labelme_format(lp.json_dict)

    print(lp.mix_coding_error)
print(label_set)
print(len(label_set))
print(shuiyin_error_count)
