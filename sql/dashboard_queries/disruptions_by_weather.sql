SELECT
    w.weather_condition,
    COUNT(*) AS disruptions
FROM fact_shipments f
JOIN dim_weather w
ON f.weather_id = w.weather_id
WHERE disruption_occurred = TRUE
GROUP BY w.weather_condition
ORDER BY disruptions DESC;