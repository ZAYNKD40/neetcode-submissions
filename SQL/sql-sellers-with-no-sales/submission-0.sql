-- Write your query below
--1. name of seller 2. no sales in 2020
select s.seller_name
from seller s
left join orders o on s.seller_id = o.seller_id and o.sale_date >= '2020-01-01' and sale_date <= '2020-12-31' --like work with var char only
where o.sale_date is null


order by s.seller_name;