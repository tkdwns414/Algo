-- 코드를 입력하세요
SELECT c.car_id, c.car_type, round(c.daily_fee * 30 * (100 - p.discount_rate) / 100, 0) as fee
from (
    select * 
    from car_rental_company_car
    where car_id not in (
        select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where 
            start_date <= '2022-11-30' and end_date >= '2022-11-01'
        )
    ) c left outer join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
on c.car_type = p.car_type and c.car_type in ("SUV", "세단") and p.duration_type = "30일 이상"
where c.daily_fee * 30 * (100 - ifnull(p.discount_rate, 0)) / 100 between 500000 and 2000000
order by fee desc, car_type, car_id desc


# 자동차 종류가 세단 또는 suv인 자동차
# 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
# 30일간의 대여 금액이 50만원 이상 200만원 미만인
# 자동차

# 일단 대여 자동차 종류가 세단 또는 suv이며 주어진 기간에 대여 가능한 애들을 먼저 다 찾는다
# 그 다음 찾아온 애들 중에서 할인 정책을 적용했을 때 50-200 미만이 되는지 확인한다
# 출력한다

# car에서 history에 있는 애들을 빼는게 맞음
# car에서 plan이 있으면 쓰고 없으면 안 쓰고로 가야함