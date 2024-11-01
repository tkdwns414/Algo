-- 코드를 작성해주세요
SELECT quarter, COUNT(*) as ecoli_count
FROM (
    SELECT
        CASE
            WHEN (month(differentiation_date) between 1 and 3) THEN '1Q'
            WHEN (month(differentiation_date) between 4 and 6) THEN '2Q'
            WHEN (month(differentiation_date) between 7 and 9) THEN '3Q'
            ELSE '4Q'
        END AS QUARTER
    FROM
        ECOLI_DATA
) q
GROUP BY quarter
order by quarter

# 일단 분기별로 묶어야 하는데
# 그냥 날짜 기준으로 묶으면 될듯?