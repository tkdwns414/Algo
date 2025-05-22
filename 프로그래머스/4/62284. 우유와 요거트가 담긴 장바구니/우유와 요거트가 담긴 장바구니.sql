-- 코드를 입력하세요
with milks as (
    select cart_id
    from cart_products
    where name = "Milk"
)
SELECT cart_id
from cart_products
where cart_id in (select cart_id from milks) and name = "Yogurt"
order by id;