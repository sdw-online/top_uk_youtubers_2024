-- 4. Duplicate records check

SELECT 
	channel_name,
	COUNT(*) as duplicate_count
FROM 
	view_uk_youtubers_2024
GROUP BY 
	channel_name 
HAVING 
	COUNT(*) > 1 