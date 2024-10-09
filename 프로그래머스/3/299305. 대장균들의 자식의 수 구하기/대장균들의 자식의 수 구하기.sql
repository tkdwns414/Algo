-- 코드를 작성해주세요
select m.id, count(s.id) as child_count
from ECOLI_DATA m left outer join ECOLI_DATA s
on m.id = s.parent_id
group by m.id