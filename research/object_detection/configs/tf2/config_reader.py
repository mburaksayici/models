import os 
from tfmodels.research.object_detection.utils.config_util import get_configs_from_pipeline_file


class ConfigReader:
    def __init__(self):
        pass


    def read_configs(self):
        return [i for i in os.listdir() if "config" in i]



    def return_config(self,config_name):
        return get_configs_from_pipeline_file(config_name)

