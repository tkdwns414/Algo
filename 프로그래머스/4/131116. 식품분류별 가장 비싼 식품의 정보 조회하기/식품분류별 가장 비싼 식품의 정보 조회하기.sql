-- 코드를 입력하세요
SELECT f.category, price as max_price, product_name
from food_product f join (
    select category, max(price) as max_price
    from food_product
    where category in ("과자", "국", "김치", "식용유")
    group by category
) m 
where f.category = m.category and f.price = m.max_price 
group by f.category
order by max_price desc