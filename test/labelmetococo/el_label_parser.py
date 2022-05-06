from putil.labelmetococo.el_label_parser import ELLabelParser
from putil.labelmetococo.el_label_name_config import label_names

elLabelParser = ELLabelParser(label_names=label_names)
# print([i.name for i in elLabelParser.get_categories()])
# print([i.name for i in elLabelParser.get_supercategories()])
