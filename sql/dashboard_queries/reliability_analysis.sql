SELECT
    carrier_reliability_score,
    AVG(lead_time_days) AS avg_lead_time
FROM fact_shipments
GROUP BY carrier_reliability_score
ORDER BY carrier_reliability_score;