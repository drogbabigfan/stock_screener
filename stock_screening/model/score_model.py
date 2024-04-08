import pandas as pd


class score_model:
    def __init__(self):
        pass

    def calculate_f_score(self, annual_finstate: pd.DataFrame):
        '''
        1. 순이익 > 0
        2. 영업현금흐름 > 0
        3. ROA/전년 ROA > 1
        4. 영업현금흐름>순이익
        5. 부채비율/전년부채비율 < 1
        6. 유동비율/전년유동비율 > 1 (!) 적합한데이터가 없음 -> 이자발생부채/자본총계의 비율 변화
        7. 발행주식수 - 전년발행주식수 < 0
        8. 매출총이익률 > 전년매출총이익률 -> (!)매출성장률로 대체(OPM 증가울도 사용가능)
        9. 자산회전율 > 전년자산회전율

        1,2,3,4: 수익성 지표
        5,6,7: 안정성(재무건전성) 지표
        8,9: 효율성 OR 성장성 지표
        '''

        # data cleaning - 영업이익(발표기준)이 NaN인 row 제거
        annual_finstate = annual_finstate.dropna(subset=['영업이익(발표기준)'])

        # 1. 순이익 > 0
        condition1 = annual_finstate['당기순이익(지배)'] > 0

        # 2. 영업현금흐름 > 0
        condition2 = annual_finstate['영업활동현금흐름'] > 0

        # 3. ROA/전년 ROA > 1
        condition3 = annual_finstate['ROA(%)'] / annual_finstate['ROA(%)'].shift(1) > 1

        # 4. 영업현금흐름>순이익
        condition4 = annual_finstate['영업활동현금흐름'] > annual_finstate['당기순이익(지배)']

        # 5. 부채비율/전년부채비율 < 1
        condition5 = annual_finstate['부채비율'] / annual_finstate['부채비율'].shift(1) < 1

        # 6. 유동비율/전년유동비율 > 1 -> 대체지표 사용
        annual_finstate['이자발생부채/자본총계'] = annual_finstate['이자발생부채'] / annual_finstate['자본총계(지배)']
        condition6 = annual_finstate['이자발생부채/자본총계'] / annual_finstate['이자발생부채/자본총계'].shift(1) > 1

        # 7. 발행주식수 - 전년발행주식수 < 0
        condition7 = annual_finstate['발행주식수'] - annual_finstate['발행주식수'].shift(1) <= 0

        # 8. 매출총이익률 > 전년매출총이익률 -> (!)매출성장률로 대체(OPM 증가울도 사용가능)
        annual_finstate['매출성장률'] = annual_finstate['매출액'] / annual_finstate['매출액'].shift(1)
        condition8 = annual_finstate['매출성장률'] > 1

        # 9. 자산회전율 > 전년자산회전율
        annual_finstate['자산회전율'] = annual_finstate['매출액'] / annual_finstate['자산총계']
        condition9 = annual_finstate['자산회전율'] > annual_finstate['자산회전율'].shift(1)

        # F-Score 계산
        f_score = condition1.astype(int) + condition2.astype(int) + condition3.astype(int) + condition4.astype(int) + condition5.astype(int) + condition6.astype(int) + condition7.astype(int) + condition8.astype(int) + condition9.astype(int)

        return f_score

