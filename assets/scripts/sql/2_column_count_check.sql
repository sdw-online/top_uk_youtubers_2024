-- 2. Column count check 

SELECT 
	COUNT(*) as column_count 
FROM 
	INFORMATION_SCHEMA.COLUMNS
WHERE 
	TABLE_NAME = 'view_uk_youtubers_2024'