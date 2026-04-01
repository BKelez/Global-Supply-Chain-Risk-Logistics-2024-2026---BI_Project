SELECT
    p.port_name,
    AVG(f.lead_time_days) AS avg_lead_time
FROM fact_shipments f
JOIN dim_port p
ON f.origin_port_id = p.port_id
GROUP BY p.port_name
ORDER BY avg_lead_time DESC;