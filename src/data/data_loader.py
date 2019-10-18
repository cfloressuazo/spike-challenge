from util.logger import Logger
import util.input_output as io
from util.paths import PATH_DATA_RAW


class DataLoader:

    df_caudal_extra = None

    FILE_NAME_CAUDAL_EXTRA = 'caudal_extra.csv.zip'

    def __init__(self, use_gbq: bool = False):

        self.use_gbq = use_gbq

        Logger.info('Files loaded from data directory', PATH_DATA_RAW, self.__class__.__name__)

    def load_data(self):

        if self.use_gbq:
            self.load_caudal_extra_gbq_data()
        else:
            self.load_caudal_extra_zip_data()

    def load_caudal_extra_zip_data(self):

        self.df_caudal_extra = io.read_csv(
            PATH_DATA_RAW, DataLoader.FILE_NAME_CAUDAL_EXTRA
        )
        Logger.info(
            'Loaded caudal extra data from file',
            DataLoader.FILE_NAME_CAUDAL_EXTRA,
            self.__class__.__name__
        )

    def load_caudal_extra_gbq_data(self):
        query = ""
        self.df_caudal_extra = io.read_gbq(query='')