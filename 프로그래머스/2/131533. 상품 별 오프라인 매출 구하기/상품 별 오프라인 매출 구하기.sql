-- 코드를 입력하세요
SELECT product_code, sum(o.sales_amount * p.price) sales
from product p natural join offline_sale o
group by product_id
order by sales desc, product_code;