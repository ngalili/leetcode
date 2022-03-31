# Write your MySQL query statement below
select totals.customer_number
from Orders,
(
select customer_number, count(customer_number) as occurence_number
from Orders
group by customer_number
order by occurence_number desc
) As totals
limit 1;

# or
select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1;
