import pandas as pd
from tqdm import tqdm

from stock_screening.collector.data_collector import DataCollector
from stock_screening.utils.data_type import DataType
from stock_screening.utils.file_utils import FileUtils


class FinancialProcessor:
    def __init__(self):
        self.file_utils = FileUtils()
        self.annual_file_list = self.get_annual_parquet_file_list()
        self.data_type = DataType
        self.data_collector = DataCollector()

    # use_cols를 이용해 필요한 컬럼만을 읽은 뒤 병렬처리로 하나의 데이터프레임으로 합친다
    def generate_single_factor_dataframe(self, column_name: str):
        pass

    def korea_value_up_dataframe(self, roe_hurdle: float, div_hurdle: float, cap_reserves_hurdle: float,
                                 fcf_hurdle: float, pbr_hurdle: float, per_hurdle: float):
        '''
        12월 말 기준 data
        1. ROE(%)
        2. 현금배당성향(%)
        3. 자본유보율: 100% 이상
        4. FCF: 0 이상
        5. PBR: 0 이상
        6. PER: 0 이상
        '''

        result_df = pd.DataFrame(columns=['기업명','시가총액(억)','ROE(%)', '현금배당성향(%)', '자본유보율', 'FCF', 'PBR(배)', 'PER(배)'])

        for file_name in tqdm(self.annual_file_list):
            annual_folder_path = self.file_utils.get_financial_annual_folder_path() + "/parquet"
            file_path = f"{annual_folder_path}/{file_name}"
            code = file_name.split(".")[0]
            df = self.file_utils.read_real_finance_data_only(file_path, format_type=self.data_type.PARQUET)

            if len(df) < 2:
                continue

            # 1. ROE(%)
            roe = df['ROE(%)'].iloc[-1]
            roe_filter = roe <= roe_hurdle

            # 2. 현금배당성향(%)
            div = df['현금배당성향(%)'].iloc[-1]
            div_filter = div <= div_hurdle

            # 3. 자본유보율
            cap_reserves = df['자본유보율'].iloc[-1]
            cap_reserves_filter = cap_reserves >= cap_reserves_hurdle

            # 4. FCF
            fcf = df['FCF'].iloc[-1]
            fcf_filter = fcf >= fcf_hurdle

            # 5. PBR
            pbr = df['PBR(배)'].iloc[-1]
            pbr_filter = pbr <= pbr_hurdle

            # 6. PER
            per = df['PER(배)'].iloc[-1]
            per_filter = per <= per_hurdle

            if roe_filter and div_filter and cap_reserves_filter and fcf_filter and pbr_filter and per_filter:
                print(f"{code} is k-value up stock")
                result_df.loc[code, 'ROE(%)'] = roe
                result_df.loc[code, '현금배당성향(%)'] = div
                result_df.loc[code, '자본유보율'] = cap_reserves
                result_df.loc[code, 'FCF'] = fcf
                result_df.loc[code, 'PBR(배)'] = pbr
                result_df.loc[code, 'PER(배)'] = per

        result_df = self.add_name_and_market_cap(result_df)

        return result_df

    def get_annual_parquet_file_list(self) -> list[str]:
        annual_folder_path = self.file_utils.get_financial_annual_folder_path() + "/parquet"
        file_list = self.file_utils.read_file_name_list(folder_path=annual_folder_path)
        return file_list

    def add_name_and_market_cap(self, filtered_df: pd.DataFrame) -> pd.DataFrame:
        all_stock_list = self.data_collector.get_listed_stock_dataframe()
        all_stock_list.set_index('Code', inplace=True)

        name = all_stock_list.loc[filtered_df.index, 'Name']
        market_cap = all_stock_list.loc[filtered_df.index, 'Marcap']//100_000_000

        filtered_df['기업명'] = name
        filtered_df['시가총액(억)'] = market_cap

        return filtered_df


if __name__ == "__main__":
    processor = FinancialProcessor()
    df = processor.korea_value_up_dataframe(roe_hurdle=100, div_hurdle=10, cap_reserves_hurdle=0, fcf_hurdle=0,
                                            pbr_hurdle=2, per_hurdle=100)
    now = pd.Timestamp.now().strftime("%Y%m%d")
    df.to_excel(f"k_value_up_{now}.xlsx", index=True)