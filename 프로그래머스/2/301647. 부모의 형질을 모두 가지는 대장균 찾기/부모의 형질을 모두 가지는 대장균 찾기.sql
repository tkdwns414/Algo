-- 코드를 작성해주세요
select m.id, m.genotype, s.genotype as parent_genotype
from ecoli_data m join ecoli_data s
on m.parent_id = s.id
where m.genotype & s.genotype = s.genotype
order by id;

# 일부 보유 말고 모두 보유로 풀면 풀리는듯