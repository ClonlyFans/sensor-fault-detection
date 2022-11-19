from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
import sys
from sensor.exception import SensorException
from sensor.logger import logging

class TrainPipeline:
    
    def __init__(self):
        
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        self.training_pipeline_config=training_pipeline_config  

    def data_ingestion_config(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)