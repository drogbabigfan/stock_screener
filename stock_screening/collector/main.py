import time
from tqdm import tqdm
from stock_screening.collector.data_collector import DataCollector
from stock_screening.collector.data_manager import DataManager
from stock_screening.utils.data_type import DataType


class Main:
    def __init__(self):
        self.data_collector = DataCollector()
        self.data_manager = DataManager()
        self.data_type = DataType
        self.listed_stock_code_list = self.get_listed_stock_code_list()

    def get_listed_stock_code_list(self):
        df = self.data_collector.get_listed_stock_dataframe()
        return df["Code"].tolist()

    def collect_annual_financial_data(self):
        print("Collecting Annual Financial Data")
        for code in tqdm(self.listed_stock_code_list):
            time.sleep(1)
            finstate = self.data_collector.get_year_finstate_from_naver(code)

            # save to csv
            self.data_manager.update_or_save_data(finstate, code, self.data_type.CSV,
                                                  self.data_manager.get_financial_annual_folder_path())

            # save to parquet
            self.data_manager.update_or_save_data(finstate, code, self.data_type.PARQUET,
                                                  self.data_manager.get_financial_annual_folder_path())

    def collect_quarter_financial_data(self):
        print("Collecting Quarter Financial Data")
        for code in tqdm(self.listed_stock_code_list):
            time.sleep(1)
            finstate = self.data_collector.get_quarter_finstate_from_naver(code)

            # save to csv
            self.data_manager.update_or_save_data(finstate, code, self.data_type.CSV,
                                                  self.data_manager.get_financial_quarter_folder_path())

            # save to parquet
            self.data_manager.update_or_save_data(finstate, code, self.data_type.PARQUET,
                                                  self.data_manager.get_financial_quarter_folder_path())

    def collect_ohlcv_data(self, start_date: str, end_date: str):
        print("Collecting OHLCV Data")
        for code in tqdm(self.listed_stock_code_list):
            time.sleep(1)
            ohlcv = self.data_collector.get_ohlcv(code, start_date, end_date)

            # save to csv
            self.data_manager.update_or_save_data(ohlcv, code, self.data_type.CSV,
                                                  self.data_manager.get_ohlcv_folder_path())

            # save to parquet
            self.data_manager.update_or_save_data(ohlcv, code, self.data_type.PARQUET,
                                                  self.data_manager.get_ohlcv_folder_path())

    def run(self):
        start_time = time.time()
        print("Data Collection Start, time : ", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))
        self.collect_annual_financial_data()
        print("Annual Financial Data Collection End")
        self.collect_quarter_financial_data()
        print("Quarter Financial Data Collection End")
        self.collect_ohlcv_data("2018-01-01", "2024-03-31")
        print("OHLCV Data Collection End")
        end_time = time.time()
        print("Data Collection End, time : ", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)))


if __name__ == "__main__":
    main = Main()
    main.run()
