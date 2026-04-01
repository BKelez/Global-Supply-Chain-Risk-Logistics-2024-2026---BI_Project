CREATE OR REPLACE VIEW analytics.v_lead_time_by_transport AS
SELECT
    t.transport_mode,
    AVG(f.lead_time_days) AS avg_lead_time
FROM public.fact_shipments f
JOIN public.dim_transport_mode t
ON f.transport_mode_id = t.transport_mode_id
GROUP BY t.transport_mode;