-- 코드를 입력하세요
SELECT p.product_id, p.product_name, sum(o.amount*p.price) as total_sales
from food_product p join food_order o
    on o.produce_date between '2022-05-01' and '2022-05-31'
        and p.product_id = o.product_id
group by p.product_id
order by total_sales desc, product_id

# 5월에 생산된 식품들만 남기고
# 식품 기준으로 묶어서 SUM