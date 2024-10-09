-- 코드를 입력하세요=
select 
    year(sales_date) as year, 
    month(sales_date) as month,
    count(distinct user_id) as purchased_users,
    round(
        count(distinct user_id) / (
            select count(*) 
            from user_info
            where joined between '2021-01-01' and '2021-12-31')
        ,1) as purchased_ratio
from (
    select user_id, sales_date 
    from online_sale
    where user_id in (
        select user_id
        from user_info
        where joined between '2021-01-01' and '2021-12-31'
    )
) purchased
group by year, month
order by year, month;


# 2021년에 가입한 전체 회원들 중
# 상품을 구매한 회원 수와 상품을 구매한 회원의 비율
# 년, 월, 별 출력
# 상품 구매 비율은 소수점 두번째 자리에서 반올림

# 우선 2021년에 가입한 전체 회원들을 구함
# 이때 상품을 구매한 회원 수와 가입한 회원 수를 구함

# 그냥 join하고 like로 해버릴 수도 있네... 