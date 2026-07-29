-- Write your query below
Select c.customer_id, c.customer_name
From customers c
WHere c.customer_id in (Select customer_id From orders where product_name = 'A')
and c.customer_id in (Select customer_id From orders where product_name = 'B')
and c.customer_id not in (Select customer_id From orders where product_name = 'C')
Order by customer_name;
