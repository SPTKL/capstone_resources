SELECT
  category,
  DATE_TRUNC(DATE(created_date), MONTH) AS year_month,
  COUNT(*) AS count
FROM (
  SELECT
    *
  FROM
    `nodal-component-204421.311_complaints.complaints`
  WHERE
    created_date BETWEEN '2010-05-02 04:00:00'
    AND '2018-05-02 04:00:00' )
GROUP BY
  year_month,
  category
ORDER BY
  1,
  2;
