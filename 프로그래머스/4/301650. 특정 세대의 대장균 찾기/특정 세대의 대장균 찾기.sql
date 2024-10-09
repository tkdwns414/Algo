-- 코드를 작성해주세요
select t.id
from (
        select s.*
        from ECOLI_DATA f join ECOLI_DATA s
        on f.id = s.parent_id and f.parent_id is null
     ) m
     join ECOLI_DATA t
     on m.id = t.parent_id
order by id;
     