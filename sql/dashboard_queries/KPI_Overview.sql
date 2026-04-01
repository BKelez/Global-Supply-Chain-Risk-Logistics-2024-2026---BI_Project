SELECT
    COUNT(*) AS total_shipments,
    AVG(lead_time_days) AS avg_lead_time,
    SUM(CASE WHEN disruption_occurred = TRUE THEN 1 ELSE 0 END) AS disruptions,
    AVG(carrier_reliability_score) AS avg_reliability
FROM fact_shipments;