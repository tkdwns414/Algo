-- 코드를 작성해주세요
select id, 
    case 
        when ntile(4) over (order by SIZE_OF_COLONY) = 1 then "LOW"
        when ntile(4) over (order by SIZE_OF_COLONY) = 2 then "MEDIUM"
        when ntile(4) over (order by SIZE_OF_COLONY) = 3 then "HIGH"
        else "CRITICAL"
    end as colony_name
from ecoli_data
order by id;