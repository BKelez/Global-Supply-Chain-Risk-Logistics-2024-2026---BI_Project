CREATE OR REPLACE VIEW analytics.v_weather_disruptions AS
SELECT
    w.weather_condition,
    COUNT(*) AS disruptions
FROM public.fact_shipments f
JOIN public.dim_weather w
ON f.weather_id = w.weather_id
WHERE f.disruption_occurred = 1
GROUP BY w.weather_condition;