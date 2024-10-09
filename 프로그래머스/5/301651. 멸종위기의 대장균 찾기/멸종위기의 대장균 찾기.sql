-- 코드를 작성해주세요
with recursive r as(
    select *, 1 as GENERATION
    from ECOLI_DATA
    where parent_id is null
    
    union all
    
    select a.*, r.generation + 1 as GENERATION
    from ECOLI_DATA a join r
    where r.id = a.parent_id
)
select count(*) as COUNT, GENERATION
from r 
where r.id not in (select parent_id from ecoli_data where parent_id is not null)
group by generation
order by generation;