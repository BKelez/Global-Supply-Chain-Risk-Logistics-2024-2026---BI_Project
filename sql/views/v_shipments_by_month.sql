CREATE OR REPLACE VIEW analytics.v_shipments_by_month AS
SELECT
    d.year,
    d.month,
    COUNT(*) AS shipments
FROM public.fact_shipments f
JOIN public.dim_date d
ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;