from unittest import TestCase
from stock_screening.collector.data_collector import DataCollector

class TestDataReader(TestCase):
    def setUp(self):
        self.data_reader = DataCollector()

    def test_get_year_finstate_from_naver(self):
        ## 삼성전자 2023년 매출: 3031256
        code = "005930"
        revenue = 2589355

        finstate = self.data_reader.get_year_finstate_from_naver(code)

        actual_revenue = finstate.loc['2023-12-01', '매출액']

        self.assertEqual(revenue, actual_revenue)

    def test_get_quarter_finstate_from_naver(self):
        ## 삼성전자 2023년 1분기 매출: 677,797
        code = "005930"
        revenue = 677799

        finstate = self.data_reader.get_quarter_finstate_from_naver(code)

        actual_revenue = finstate.loc['2023-12-01', '매출액']

        self.assertEqual(revenue, actual_revenue)

    def test_get_ohlcv(self):
        code = "005930"
        start_date = "2024-01-01"
        end_date = "2024-03-31"

        ohlcv = self.data_reader.get_ohlcv(code, start_date, end_date)
        close = 82400

        actual_close = ohlcv.loc['2024-03-29', 'Close']

        self.assertEqual(close, actual_close)

    def test_get_listed_stock_dataframe(self):
        all_stock = self.data_reader.get_listed_stock_dataframe()

        code = "005930"
        name = "삼성전자"

        samsung = all_stock[all_stock["Code"] == code]

        self.assertEqual(name, samsung["Name"].values[0])