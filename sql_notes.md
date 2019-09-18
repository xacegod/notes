# Select all from one table that does not exist in another table
SELECT t1.name
FROM table1 t1
LEFT JOIN table2 t2 ON t2.name = t1.name
WHERE t2.name IS NULL


select num,count(*) from list_dat group by num having count(*)>1


select id,min(time),max(time) from tab1 where id in (select broj from tab2 where something > '') group by id 
having cast(substr(max(time),1,2) as int)-cast(substr(min(time),1,2) as int) > 1
