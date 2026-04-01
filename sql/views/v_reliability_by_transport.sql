CREATE OR REPLACE VIEW analytics.v_reliability_by_transport AS
SELECT
    t.transport_mode,
    AVG(f.lead_time_days) AS avg_lead_time,
    AVG(f.carrier_reliability_score) AS reliability,
    COUNT(*) AS shipments
FROM public.fact_shipments f
JOIN public.dim_transport_mode t
ON f.transport_mode_id = t.transport_mode_id
GROUP BY t.transport_mode;