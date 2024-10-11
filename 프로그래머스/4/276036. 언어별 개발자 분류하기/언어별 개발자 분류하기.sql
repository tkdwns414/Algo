-- 코드를 작성해주세요
select grade, id, email
from (   
     select case
        when (
                skill_code & (select code from skillcodes where name="Python")
                and
                (   
                    select count(*)
                    from skillcodes
                    where category = "Front End" and code & skill_code
                )
             ) then 'A'
        when skill_code & (select code from skillcodes where name="C#")
            then 'B'
        when (   
                select count(*)
                from skillcodes
                where category = "Front End" and code & skill_code
            ) then 'C'
        else 'D'
        end as grade,
        id, email
    from developers
) w
where grade != "D"
order by grade, id;

# 이걸 어떻게 group by로 풀지?