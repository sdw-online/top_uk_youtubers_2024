/*
# 3. Data type check

Check the data types of each column from the view by checking the INFORMATION SCHEMA view

*/


SELECT
    COLUMN_NAME,
    DATA_TYPE
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'view_uk_youtubers_2024';