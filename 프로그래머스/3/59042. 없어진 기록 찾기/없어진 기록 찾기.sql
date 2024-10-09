-- 코드를 입력하세요
select animal_id, ifnull(i.name, o.name) as name
from animal_outs o left outer join animal_ins i
using(animal_id)
where i.datetime is null
order by animal_id;