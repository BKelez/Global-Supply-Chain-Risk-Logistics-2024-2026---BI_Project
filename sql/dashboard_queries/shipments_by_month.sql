SELECT
    d.year,
    d.month,
    COUNT(*) AS shipments
FROM fact_shipments f
JOIN dim_date d
ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;