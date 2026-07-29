-- Write your query below
Select c.customer_id, c.customer_name --c. to mention the table we are using, and we are using this table because we also want customer name
From customers c --notatn to shorten customers to c to use in dot notation to acess table quicker
WHere c.customer_id in (Select customer_id From orders where product_name = 'A') --the condition, and query it within query
and c.customer_id in (Select customer_id From orders where product_name = 'B')
and c.customer_id not in (Select customer_id From orders where product_name = 'C')
Order by customer_name; --using order by and a semi colon
