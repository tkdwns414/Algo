-- 코드를 작성해주세요
WITH MAX_COLONY as (
    SELECT 
        year(differentiation_date) as year,
        max(size_of_colony) as max_colony
    FROM
        ECOLI_DATA
    GROUP BY year
)
SELECT 
    year(differentiation_date) as year,
    max_colony - size_of_colony as year_dev,
    id
from 
    ECOLI_DATA e join MAX_COLONY m
    ON year(e.DIFFERENTIATION_DATE) = m.year
ORDER BY
    year, year_dev



# 각 년도별 최대 크기 구하고
# 맞는 년도와 join해서 빼기