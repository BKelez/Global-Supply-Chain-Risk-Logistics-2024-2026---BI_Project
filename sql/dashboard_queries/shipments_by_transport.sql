SELECT
    t.transport_mode,
    COUNT(*) AS shipments
FROM fact_shipments f
JOIN dim_transport_mode t
ON f.transport_mode_id = t.transport_mode_id
GROUP BY t.transport_mode
ORDER BY shipments DESC;