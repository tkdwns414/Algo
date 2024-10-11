-- 코드를 입력하세요
SELECT category, sum(sales) as total_sales
from book b join book_sales s using (book_id)
where year(sales_date) = 2022 and month(sales_date) = 1
group by category
order by category;