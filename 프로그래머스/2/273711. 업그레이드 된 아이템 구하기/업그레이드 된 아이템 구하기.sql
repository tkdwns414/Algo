-- 코드를 작성해주세요
select item_id, item_name, rarity
from item_info
where item_id in (
    select t.item_id
    from item_tree t join item_info i
    on t.parent_item_id = i.item_id
    where i.rarity="RARE" and t.parent_item_id is not null
)
order by item_id desc;

## join을 했어. 
## 내가 rare야? 
## 그럼 나를 parent_item_id로 가지는 애들의 item_id를 뱉어