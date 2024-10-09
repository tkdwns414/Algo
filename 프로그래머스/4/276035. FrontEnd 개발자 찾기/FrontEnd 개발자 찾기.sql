-- 코드를 작성해주세요
select distinct id, email, first_name, last_name
from developers d join skillcodes s
on s.category = "Front End" and d.skill_code & s.code
order by id;

# 프론트엔드 코드 중 적어도 하나와 비트연산 후 참인 애들을 남기기
# where skill_code & any(select code from skillcodes where category = "Front End") >> 비트연산자 비교연산자라서 사용 불가