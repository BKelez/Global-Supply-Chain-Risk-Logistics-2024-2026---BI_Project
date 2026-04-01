CREATE OR REPLACE VIEW analytics.v_risk_score_analysis AS
SELECT
    geopolitical_risk_score,
    AVG(lead_time_days) AS avg_lead_time,
    COUNT(*) AS shipments
FROM public.fact_shipments
GROUP BY geopolitical_risk_score
ORDER BY geopolitical_risk_score;