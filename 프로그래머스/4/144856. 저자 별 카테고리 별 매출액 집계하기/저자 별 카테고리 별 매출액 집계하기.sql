-- 코드를 입력하세요
SELECT author_id, author_name, category, sum(sales * price) as total_sales
from book join author using(author_id) join book_sales using(book_id)
where sales_date between '2022-01-01' and '2022-01-31'
group by author_id, category
order by author_id, category desc;

# 1월에 판매된 도서 중 저자별, 카테고리별 매출액 구하기
# 