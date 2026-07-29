-- Write your query below
Select employee_id,
    Case --the if else of sql, and in the end you have to store the data as something
        When employee_id %2 = 1 And name Not LIke 'M%' Then salary
        else 0
    end as bonus
From employees
Order by employee_id;
