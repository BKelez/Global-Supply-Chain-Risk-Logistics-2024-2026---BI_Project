CREATE OR REPLACE VIEW analytics.v_reliability_analysis AS
SELECT
    carrier_reliability_score,
    AVG(lead_time_days) AS avg_lead_time,
    COUNT(*) AS shipments
FROM public.fact_shipments
GROUP BY carrier_reliability_score
ORDER BY carrier_reliability_score;