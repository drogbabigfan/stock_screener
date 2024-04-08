import os
from unittest import TestCase
import pandas as pd
from stock_screening.utils.file_utils import FileUtils
from stock_screening.utils.data_type import DataType


class TestFileUtils(TestCase):
    def setUp(self):
        self.file_utils = FileUtils()
        self.test_data = self.generate_test_data()
        self.test_save_path = os.path.dirname(os.path.abspath(__file__)) + "/../data/test_save_path"

    def generate_test_data(self):
        data = {
            "A": [1, 2, 3],
            "B": [4, 5, 6],
            "C": [7, 8, 9]
        }

        return pd.DataFrame(data)

    def test_save_file(self):
        csv_format = DataType.CSV
        parquet_format = DataType.PARQUET

        csv_file_path = self.test_save_path + "/csv_save_test.csv"
        parquet_file_path = self.test_save_path + "/parquet_save_test.parquet"

        self.file_utils.save_file(df=self.test_data, file_path=csv_file_path, format_type=csv_format)
        self.assertTrue(self.file_utils.is_exists(csv_file_path))

        self.file_utils.save_file(df=self.test_data, file_path=parquet_file_path, format_type=parquet_format)
        self.assertTrue(self.file_utils.is_exists(parquet_file_path))


    def test_read_file(self):
        csv_format = DataType.CSV
        parquet_format = DataType.PARQUET

        csv_file_path = self.test_save_path + "/csv_save_test.csv"
        parquet_file_path = self.test_save_path + "/parquet_save_test.parquet"

        csv_data = self.file_utils.read_file(path=csv_file_path, format_type=csv_format)
        parquet_data = self.file_utils.read_file(path=parquet_file_path, format_type=parquet_format)

        self.assertTrue(csv_data.equals(self.test_data))
        self.assertTrue(parquet_data.equals(self.test_data))
