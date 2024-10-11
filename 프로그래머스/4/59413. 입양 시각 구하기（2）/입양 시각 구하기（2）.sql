-- 코드를 입력하세요
with recursive time as (
    select 0 as hour
    
    union all
    
    select hour + 1
    from time 
    where hour < 23
)

SELECT hour, count(animal_id) as count
from time left join animal_outs
on hour(datetime) = hour
group by hour
order by hour;