import os
import pandas as pd
from stock_screening.data.collector.data_type import DataType


class FileUtils:
    @staticmethod
    def file_exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def read_file(path: str, format_type: DataType):
        if format_type == DataType.CSV:
            return pd.read_csv(path, index_col=0)

        if format_type == DataType.PARQUET:
            return pd.read_parquet(path)

        if format_type == DataType.EXCEL:
            return pd.read_excel(path)

        raise ValueError(f"Unsupported file format: {format_type}")

    @staticmethod
    def save_file(df: pd.DataFrame, path: str, format_type: DataType):
        if format_type == DataType.CSV:
            df.to_csv(path, index=True)

        if format_type == DataType.PARQUET:
            df.to_parquet(path, index=True)

        if format_type == DataType.EXCEL:
            df.to_excel(path, index=True)

        raise ValueError(f"Unsupported file format: {format_type}")

