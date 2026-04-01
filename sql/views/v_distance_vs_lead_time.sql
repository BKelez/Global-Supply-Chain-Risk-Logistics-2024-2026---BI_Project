CREATE OR REPLACE VIEW analytics.v_distance_vs_lead_time AS
SELECT
    distance_km,
    lead_time_days
FROM public.fact_shipments;

SELECT * FROM analytics.v_distance_vs_lead_time;