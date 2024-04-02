import os

import pandas as pd

from stock_screening.data.collector.data_type import DataType
from stock_screening.data.utils.file_utils import FileUtils


class DataManager:
    def __init__(self):
        self.data_root_path = os.path.dirname(os.path.abspath(__file__))
        self.file_utils = FileUtils()

    def update_or_save_data(self, df: pd.DataFrame, code: str, format_type: DataType, folder_path: str):
        pass

    def save_data(self, df: pd.DataFrame, format_type: DataType, file_path: str):
        self.file_utils.save_file(df, file_path, format_type)

    def update_data(self, df: pd.DataFrame, code: str, format_type: DataType, folder_path: str):
        pass

    def is_folder_exists(self, folder_path: str) -> bool:
        return os.path.exists(folder_path)

    def get_financial_annual_folder_path(self) -> str:
        return f"{self.data_root_path}/financial_data/annual"

    def get_financial_quarter_folder_path(self) -> str:
        return f"{self.data_root_path}/financial_data/quarter"

    def get_ohlcv_folder_path(self) -> str:
        return f"{self.data_root_path}/ohlcv"
