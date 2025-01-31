-- 코드를 입력하세요
SELECT
    b.title,
    b.board_id,
    r.reply_id,
    r.writer_id,
    r.contents,
    TO_CHAR(r.created_date, 'yyyy-mm-dd') as created_date
FROM
    USED_GOODS_BOARD b JOIN USED_GOODS_REPLY r ON b.board_id = r.board_id
WHERE
    EXTRACT(YEAR FROM b.CREATED_DATE) = 2022
    AND
    EXTRACT(MONTH FROM b.CREATED_DATE) = 10
ORDER BY
    r.CREATED_DATE, b.title