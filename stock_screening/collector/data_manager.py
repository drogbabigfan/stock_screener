import os

import pandas as pd

from stock_screening.utils.data_type import DataType
from stock_screening.utils.file_utils import FileUtils


class DataManager:
    def __init__(self):
        self.data_root_path = os.path.dirname(os.path.abspath(__file__))+"/../data"
        self.file_utils = FileUtils()

    def update_or_save_data(self, new_df: pd.DataFrame, code: str, format_type: DataType, folder_path: str):
        save_path = f"{folder_path}/{format_type.value}/{code}.{format_type.value}"

        if self.file_utils.is_exists(save_path):
            old_df = self.file_utils.read_date_index_file(save_path, format_type)
            result_df = self.merge_dfs_on_date_index(new_df, old_df)
            self.file_utils.save_file(result_df, save_path, format_type)
        else:
            self.file_utils.save_file(new_df, save_path, format_type)

    def merge_dfs_on_date_index(self, new_df: pd.DataFrame, old_df: pd.DataFrame):
        missing_rows = old_df.loc[~old_df.index.isin(new_df.index)]
        result_df = pd.concat([new_df, missing_rows], axis=0)

        # 오름차순 정렬
        result_df.sort_index(inplace=True, ascending=True)

        return result_df

    def is_folder_exists(self, folder_path: str) -> bool:
        return os.path.exists(folder_path)

    def get_financial_annual_folder_path(self) -> str:
        return f"{self.data_root_path}/financial_data/annual"

    def get_financial_quarter_folder_path(self) -> str:
        return f"{self.data_root_path}/financial_data/quarter"

    def get_ohlcv_folder_path(self) -> str:
        return f"{self.data_root_path}/ohlcv"
