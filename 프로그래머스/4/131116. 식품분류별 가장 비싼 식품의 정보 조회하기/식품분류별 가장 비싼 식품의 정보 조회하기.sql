-- 코드를 입력하세요
SELECT category, price as max_price, product_name
from food_product
where category in ("과자", "국", "김치", "식용유")
and price in (
    select max(price) as max_price
    from food_product
    where category in ("과자", "국", "김치", "식용유")
    group by category
)
group by category
order by max_price desc