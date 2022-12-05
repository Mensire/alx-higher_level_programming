-- Lists all records of second_table where name is present
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
OR name <> ''
ORDER BY score DESC;
