-- Write your query below
--need names of all sales people, no orders with crimson
--sale id in both sale person andorder, and connected to com id in orders and company
--want order id to be null with com_id 1
select s.name
from sales_person s
left join orders o on s.sales_id = o.sales_id
left join company c on o.com_id = c.com_id and c.name = 'CRIMSON'
gROUP BY s.sales_id, s.name
HAVING SUM(CASE WHEN c.name = 'CRIMSON' THEN 1 ELSE 0 END) = 0;
