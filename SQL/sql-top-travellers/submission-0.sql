-- Write your query below
-- need totatl distance, in desc order, sort by name in ascending order
select u.name, Coalesce(sum(r.distance),0) as travelled_distance --end output needed
from users u
left join rides r on u.id = r.user_id --users favored and can appear with null
group by u.name
order by travelled_distance desc, name --name as tie breaker