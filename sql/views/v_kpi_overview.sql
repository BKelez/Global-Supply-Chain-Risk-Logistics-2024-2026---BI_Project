CREATE OR REPLACE VIEW analytics.v_kpi_overview AS
SELECT
    COUNT(*) AS total_shipments,
    AVG(lead_time_days) AS avg_lead_time,
    SUM(CASE WHEN disruption_occurred = 1 THEN 1 ELSE 0 END) AS disruptions,
    AVG(carrier_reliability_score) AS avg_reliability
FROM public.fact_shipments;