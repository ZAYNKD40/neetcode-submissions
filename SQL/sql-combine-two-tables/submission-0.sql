-- Write your query below
--first part is select, choose what you want to select, then from first table since we want to left join favor that first table then left join this is same part with from and give table name and the shortenened char then do on and the rows that are matched = each other
select p.first_name, p.last_name, a.city, a.state
from person p
left join address a on p.person_id = a.person_id