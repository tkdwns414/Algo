-- 코드를 작성해주세요
select dept_id, dept_name_en, round(avg(sal),0) as avg_sal
from HR_DEPARTMENT natural join HR_EMPLOYEES
group by dept_id
order by avg_sal desc;