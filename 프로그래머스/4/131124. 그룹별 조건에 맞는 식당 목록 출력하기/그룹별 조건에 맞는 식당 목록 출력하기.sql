-- 코드를 입력하세요
SELECT member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from rest_review natural join member_profile
where member_id = (select member_id
                  from rest_review
                  group by member_id
                  order by count(*) desc
                  limit 1)
order by review_date, review_text

# 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
# 리뷰를 가장 많이 작성한 회원을 먼저 찾기
