SELECT
    t.transport_mode,
    AVG(f.lead_time_days) AS avg_lead_time
FROM fact_shipments f
JOIN dim_transport_mode t
ON f.transport_mode_id = t.transport_mode_id
GROUP BY t.transport_mode
ORDER BY avg_lead_time DESC;