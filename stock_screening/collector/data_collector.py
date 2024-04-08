import FinanceDataReader as fdr
import pandas as pd


class DataCollector:
    def __init__(self):
        pass

    def get_year_finstate_from_naver(self, code: str):
        return fdr.SnapDataReader(f"NAVER/FINSTATE/{code}")

    def get_quarter_finstate_from_naver(self, code: str):
        return fdr.SnapDataReader(f"NAVER/FINSTATE-Q/{code}")

    def get_ohlcv(self, code: str, start: str, end: str):
        return fdr.DataReader(code, start, end)

    def get_listed_stock_dataframe(self) -> pd.DataFrame:
        kospi = fdr.StockListing("KOSPI")
        kosdaq = fdr.StockListing("KOSDAQ")

        all_stock = pd.concat([kospi, kosdaq])

        # 종목코드 마지막자리 0으로 끝나는 보통주만 사용
        filtered_all_stock = all_stock[all_stock["Code"].str.endswith('0')]

        return filtered_all_stock
