재무데이터/시장데이터를 활용해 주식 스크리닝

1. Collector: 하단의 데이터를 수집하여 종목별 CSV, PARQUET으로 저장
   - 재무데이터: 네이버 Finance 데이터를 활용하여 연도별/분기별 데이터를 종목별로 보관
   - 가격데이터: OHLCV 5년치 수집
   - 기타데이터: 일자별 시가총액, 거래대금, 거래회전율

2. 스크리닝 방식:
   - Quality 지표: ROE, OPM, GPM, OP Growth, Revenue Growth
   - Value 지표: PER, PBR, PEG(OP Growth), PEG(NI Growth)
   - Scoring 지표: F-Score
   - Quantile/Rank 지표: FCF, 영업현금흐름, OPM, GPM, 시가총액, 거래회전율
