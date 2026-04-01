CREATE OR REPLACE VIEW analytics.v_lead_time_by_port AS
SELECT
    p.port_name,
    AVG(f.lead_time_days) AS avg_lead_time
FROM public.fact_shipments f
JOIN public.dim_port p
ON f.origin_port_id = p.port_id
GROUP BY p.port_name;