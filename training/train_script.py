import re 
import os
import xml.etree.ElementTree as ET

from tqdm import tqdm 
from imageai.Detection.Custom import DetectionModelTrainer



# Предобработка аннотаций (изменение пути к изображению)
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


# Класс, отвечающий за файн-тюнинг модели типа YOLO v3
class Trainer():
    # download 'pretrained-yolov3.h5' from the link below
    # https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5
    
    def __init__(self, model_path, data_path):
        self.base_path = os.getcwd()
        self.model_path = model_path        
        self.data_path = data_path


    def train_detection_model(self):
        trainer = DetectionModelTrainer()
        trainer.setModelTypeAsYOLOv3()
        trainer.setDataDirectory(data_directory=os.path.join(self.base_path, self.data_path))
        trainer.setTrainConfig(object_names_array=["fire"], batch_size=10, num_experiments=10,
                            train_from_pretrained_model=os.path.join(self.base_path, self.model_path))

        trainer.trainModel()


if __name__=='__main__':
    model_path = 'models/pretrained-yolov3.h5'
    data_path = 'training/fire-dataset'

    prepare_annotations(data_path)
    fire_yolo = Trainer(model_path, data_path)
    fire_yolo.train_detection_model()