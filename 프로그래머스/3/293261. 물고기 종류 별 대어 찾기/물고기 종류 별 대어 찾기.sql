-- 코드를 작성해주세요
WITH max_fishes as (
    select fish_type, max(length) as length
    from fish_info natural join fish_name_info
    group by fish_type
)
SELECT id, fish_name, length
from fish_info join fish_name_info using(fish_type)
    join max_fishes using(fish_type, length)
order by id

# 종류별로 가장 큰 물고기 id, 물고기 이름, 길이
# 종류별 가장 큰 길이 구해서 그거랑 같은 애 남기기
# 종류별로 가장 큰 물고기 구하기