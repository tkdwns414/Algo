-- 코드를 입력하세요

select flavor
from (
    SELECT flavor, sum(total_order) as total
    from(
        select *
        from first_half
        union
        select *
        from july
    ) t
    group by flavor
    order by total desc
) t
limit 3;

