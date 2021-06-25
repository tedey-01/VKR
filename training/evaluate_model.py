import os 
from imageai.Detection.Custom import DetectionModelTrainer


def evaluate_model(model_path, data_path, config_path):
    base_path = os.getcwd()
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory=os.path.join(base_path, data_path))
    metrics = trainer.evaluateModel(model_path=os.path.join(base_path, model_path), 
                                    json_path=os.path.join(base_path, config_path), 
                                    iou_threshold=0.75, 
                                    object_threshold=0.3, 
                                    nms_threshold=0.5)
    print(metrics)


if __name__=="__main__":
    model_path = "models/detection_model-ex-33--loss-4.97.h5"
    data_path = "training/fire-dataset"
    config_path = "detection_config.json"