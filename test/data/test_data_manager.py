from unittest import TestCase

from stock_screening.data import DataManager


class TestDataManager(TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_update_or_save_data(self):
        self.fail()

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
