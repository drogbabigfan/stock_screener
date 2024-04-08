import os
from unittest import TestCase

import pandas as pd

from stock_screening.collector import DataManager
from stock_screening.utils.data_type import DataType


class TestDataManager(TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.data_type = DataType
        self.root_path = os.path.dirname(os.path.abspath(__file__))

    def get_new_data(self):
        new_data = pd.DataFrame({
            "A": [2, 3, 4],
            "B": [5, 6, 5],
            "C": [8, 9, 6],
        })

        # timestamp index
        new_data.index = pd.date_range(start='1/1/2021', periods=3, freq='Y')
        return new_data

    def get_old_data(self):
        old_data = pd.DataFrame({
            "A": [0, 1, 2, 3],
            "B": [0, 4, 5, 6],
            "C": [0, 7, 8, 8]
        })

        # timestamp index
        old_data.index = pd.date_range(start='1/1/2020', periods=4, freq='Y')

        return old_data

    def test_merge_dfs_on_date_index(self):
        new_data = self.get_new_data()
        old_data = self.get_old_data()

        result_df = self.data_manager.merge_dfs_on_date_index(new_data, old_data)

        # result 첫 row와 old_data 첫 row 같은지 검증
        self.assertTrue(result_df.iloc[0].equals(old_data.iloc[0]))

        # result 마지막 row와 new_data 마지막 row 같은지 검증
        self.assertTrue(result_df.iloc[-1].equals(new_data.iloc[-1]))

        # result 마지막 -1 row와 new_data 마지막 row 같은지 검증
        self.assertTrue(result_df.iloc[-2].equals(new_data.iloc[-2]))

        # result 마지막 -2 row와 old_data 마지막 row 다른지 검증
        self.assertFalse(result_df.iloc[-2].equals(old_data.iloc[-1]))


    def test_get_finanacial_annual_folder_path(self):
        # 예상값
        expected = self.data_manager.data_root_path + "/financial_data/annual"
        # 실제값
        actual = self.data_manager.get_financial_annual_folder_path()

        self.assertEqual(expected, actual)

    def test_get_finanal_quarter_folder_path(self):
        # 예상값
        expected = self.data_manager.data_root_path + "/financial_data/quarter"
        # 실제값
        actual = self.data_manager.get_financial_quarter_folder_path()

        self.assertEqual(expected, actual)

    def test_get_ohlcv_folder_path(self):
        # 예상값
        expected = self.data_manager.data_root_path + "/ohlcv"
        # 실제값
        actual = self.data_manager.get_ohlcv_folder_path()

        self.assertEqual(expected, actual)
