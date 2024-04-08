import os
import pandas as pd
from stock_screening.utils.data_type import DataType


class FileUtils:
    def __init__(self):
        self.data_root_path = os.path.dirname(os.path.abspath(__file__))+"/../data"

    @staticmethod
    def is_exists(path: str) -> bool:
        return os.path.exists(path)

    def read_file(self, path: str, format_type: DataType):
        if format_type == DataType.CSV:
            return pd.read_csv(path, index_col=0)

        if format_type == DataType.PARQUET:
            return pd.read_parquet(path)

        if format_type == DataType.EXCEL:
            return pd.read_excel(path)

        raise ValueError(f"Unsupported file format: {format_type}")

    @staticmethod
    def save_file(df: pd.DataFrame, file_path: str, format_type: DataType):
        # 폴더 존재 여부 확인
        folder_path = os.path.dirname(file_path)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if format_type == DataType.CSV:
            return df.to_csv(file_path, index=True, encoding='utf-8-sig')

        if format_type == DataType.PARQUET:
            return df.to_parquet(file_path, index=True)

        if format_type == DataType.EXCEL:
            return df.to_excel(file_path, index=True)

        raise ValueError(f"Unsupported file format: {format_type}")

    def read_date_index_file(self, path: str, format_type: DataType):
        df = self.read_file(path, format_type)
        df.index = pd.to_datetime(df.index)
        return df

    def read_real_finance_data_only(self, path: str, format_type: DataType):
        df = self.read_date_index_file(path, format_type)
        # 영업이익(발표기준) Nan값인 row 삭제 후 DataFrame 반환
        return df.dropna(subset=['영업이익(발표기준)'])

    @staticmethod
    def read_file_name_list(folder_path: str):
        file_names = os.listdir(folder_path)
        return file_names

    def get_financial_annual_folder_path(self) -> str:
        return f"{self.data_root_path}/financial_data/annual"

    def get_financial_quarter_folder_path(self) -> str:
        return f"{self.data_root_path}/financial_data/quarter"

    def get_ohlcv_folder_path(self) -> str:
        return f"{self.data_root_path}/ohlcv"

