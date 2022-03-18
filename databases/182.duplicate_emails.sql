# Write your MySQL query statement below
# First approach:
select email 
from Person
group by email
having count(*) > 1