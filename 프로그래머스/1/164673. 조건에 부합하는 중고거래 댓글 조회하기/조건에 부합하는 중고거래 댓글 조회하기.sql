-- 코드를 입력하세요
SELECT title, board_id, reply_id, r.writer_id, r.contents, date_format(r.created_date,'%Y-%m-%d') as created_date
from used_goods_board b join used_goods_reply r
using (board_id)
where year(b.created_date) = 2022 and month(b.created_date) = 10
order by created_date, title;