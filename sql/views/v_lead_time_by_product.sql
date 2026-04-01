CREATE OR REPLACE VIEW analytics.v_lead_time_by_product AS
SELECT
    c.product_category,
    AVG(f.lead_time_days) AS avg_lead_time
FROM public.fact_shipments f
JOIN public.dim_product_category c
ON f.product_category_id = c.product_category_id
GROUP BY c.product_category;