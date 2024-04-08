from unittest import TestCase

import pandas as pd

from stock_screening.data_processor.financial_processor import FinancialProcessor


class TestFinancialProcessor(TestCase):
    def setUp(self):
        self.financial_processor = FinancialProcessor()

    def test_generate_single_factor_dataframe(self):
        self.fail()

    def test_korea_value_up_dataframe(self):
        self.fail()

    def test_get_annual_financial_file_list(self):
        file_list = self.financial_processor.get_annual_parquet_file_list()
        self.assertIsNotNone(file_list)
        code = "005930.parquet"
        self.assertIn(code, file_list)

    def test_add_name_and_market_cap(self):
        index = ['005930', '001440']
        columns = ['기업명','시가총액','ROE(%)', '현금배당성향(%)', '자본유보율', 'FCF', 'PBR(배)', 'PER(배)']
        temp_df = pd.DataFrame(index=index, columns=columns)

        result_df = self.financial_processor.add_name_and_market_cap(temp_df)

        self.assertIsNotNone(result_df)

        expected_name = '삼성전자'
        actual_name = result_df.loc['005930', '기업명']

        self.assertEqual(expected_name, actual_name)
