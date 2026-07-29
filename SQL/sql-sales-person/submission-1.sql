-- Write your query below
--need names of all sales people, no orders with crimson
--sale id in both sale person andorder, and connected to com id in orders and company
--want order id to be null with com_id 1
select s.name
from sales_person s
where s.sales_id not in (select o.sales_id from orders o inner join company c on
        o.com_id = c.com_id where c.name = 'CRIMSON' )