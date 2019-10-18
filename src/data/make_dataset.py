# -*- coding: utf-8 -*-
"""
The entry point of the data processor
"""
import sys
from util.logger import Logger
from data.data_loader import DataLoader
from configs.configs import Configs
from dotenv import find_dotenv, load_dotenv
import time


def main(configs: Configs = None, data_loader: DataLoader = None):
    """
    main function for data processor from raw files SAP to tables in database
    to be consumed by forecast model

    usage example:
        $ python spike-challenge/src/make_dataset.py

    """
    if configs is None:
        configs = Configs('default_config.yaml')

    if data_loader is None:

        data_loader = DataLoader()

        data_loader.load_data()

    # parser = Parser(
    #     data=data_loader
    # )


if __name__ == '__main__':
    START = time.time()
    # find .env automatically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    configs = None
    if len(sys.argv) > 1:
        configs = Configs(sys.argv[1])

    main(configs)

    END = time.time()
    Logger.info('Script completed in', '%i seconds' % int(END - START), __file__)
