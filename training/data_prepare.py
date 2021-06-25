import re 
import os
import xml.etree.ElementTree as ET

from tqdm import tqdm 



def prepare_annotations(data_path="traniing/fire-dataset"):
    for data_type in ['train', 'validation']:
        base_path = os.getcwd()
        template_path = os.path.join(base_path, "training", "fire-dataset", data_type, "images")
        annots_dir_path = os.path.join(base_path, "training", "fire-dataset", data_type, "annotations")
        for annot in tqdm(os.listdir(annots_dir_path)):
            annot_path = os.path.join(base_path, "training", "fire-dataset", data_type, "annotations", annot)
  
            tree = ET.parse(annot_path) 
            root = tree.getroot() 

            # changing a field text 
            for elem in root.iter('path'): 
                elem.text = re.sub(r'C:.*images', template_path, elem.text)
            tree.write(annot_path) 
            

if __name__=='__main__':
    prepare_annotations('traniing/fire-dataset')