CREATE OR REPLACE VIEW analytics.v_risk_by_product AS
SELECT
    p.product_category,
    AVG(f.lead_time_days) AS avg_lead_time,
    AVG(f.geopolitical_risk_score) AS avg_risk,
    COUNT(*) AS shipments
FROM public.fact_shipments f
JOIN public.dim_product_category p
ON f.product_category_id = p.product_category_id
GROUP BY p.product_category;