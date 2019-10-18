import os
import util.input_output as io
from util.paths import PATH_CONFIG
from util.logger import Logger


class Configs:

    def __init__(self, config_file_name: str = None, configs: dict = None):
        """
        Create configs element from file or from a dictionary of values

        Args:
             config_file_name (str): name of the configs file
             configs (dict): settings as a dictionary
        """

        if config_file_name is not None:
            configs = io.read_yaml(PATH_CONFIG, config_file_name)

            Logger.info('Loaded configs from file', os.path.join(PATH_CONFIG, config_file_name),
                        self.__class__.__name__)

        for name, value in configs.items():
            self.__setattr__(name, value)


