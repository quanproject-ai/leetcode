-- Create the table
CREATE TABLE user_logins (
    user_id INT,
    login_date DATE
);

-- Insert 40 entries with user_id values from 1 to 10
INSERT INTO user_logins (user_id, login_date) VALUES
(1, '2024-01-01'),
(1, '2024-01-02'),
(1, '2024-01-03'),
(2, '2024-01-01'),
(2, '2024-01-02'),
(2, '2024-01-03'),
(3, '2024-01-01'),
(3, '2024-01-04'),
(3, '2024-01-05'),
(4, '2024-01-01'),
(4, '2024-01-06'),
(4, '2024-01-07'),
(5, '2024-01-02'),
(5, '2024-01-08'),
(1, '2024-01-04'),
(2, '2024-01-05'),
(3, '2024-01-06'),
(4, '2024-01-02'),
(5, '2024-01-09'),
(1, '2024-01-05'),
(2, '2024-01-07'),
(3, '2024-01-08'),
(4, '2024-01-09'),
(5, '2024-01-10'),
(1, '2024-01-06'),
(2, '2024-01-11'),
(3, '2024-01-12'),
(4, '2024-01-10'),
(5, '2024-01-13'),
(1, '2024-01-07'),
(2, '2024-01-14'),
(3, '2024-01-15'),
(4, '2024-01-11'),
(5, '2024-01-14'),
(1, '2024-01-08'),
(2, '2024-01-15'),
(3, '2024-01-16'),
(4, '2024-01-12'),
(5, '2024-01-16'),
(1, '2024-01-09'),
(2, '2024-01-17'),
(3, '2024-01-18'),
(4, '2024-01-13'),
(5, '2024-01-19');
-- fetching data

/*WITH chicken as (select 
login_date, 
count(user_id)  as total_login 
from  user_logins
group by login_date  
order by login_date
)

SELECT 
  login_date,
  total_login,
  (lead(total_login,1,total_login) over() / total_login)as user_retention
FROM chicken*/
with dup as (select 
user_id,
login_date, 
row_number() over(partition by user_id order by login_date) as rn
from  user_logins),

count_date as (
select 
login_date, 
count(user_id)  as total_login 
from  user_logins
group by login_date  
order by login_date
),
verify_dup as (
select 
d2.user_id, d2.login_date
from dup d1
left join dup d2 on d1.user_id = d2.user_id and
datediff(d2.login_date,d1.login_date) = 1 and
d2.rn - d1.rn = 1
where d2.user_id is not null
)

select
(count(vd.user_id)/cd.total_login) as retention ,
vd.login_date
from verify_dup vd 
left join count_date cd on cd.login_date = vd.login_date
group by vd.login_date, cd.total_login

