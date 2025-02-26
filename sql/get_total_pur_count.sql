USE cardb;
SELECT 
    age, 
    SUM(pur_count) AS total_purchases
FROM tbl_car
WHERE age IS NOT NULL
GROUP BY age
ORDER BY age;