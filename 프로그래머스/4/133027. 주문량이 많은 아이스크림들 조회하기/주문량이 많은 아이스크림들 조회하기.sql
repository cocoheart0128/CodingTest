-- 코드를 입력하세요
select FLAVOR from (
SELECT f.FLAVOR,f.TOTAL_ORDER+j.TOTAL_ORDER as total_order from FIRST_HALF f
left join (
    select flavor,sum(total_order) as total_order from JULY
group by flavor) j
on  f.FLAVOR=j.FLAVOR)t
order by total_order desc
limit 3