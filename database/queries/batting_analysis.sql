USE cricketiq_analytics;

-- ==========================================
-- BATTING ANALYSIS
-- ==========================================

-- 1. Top 10 Run Scorers
SELECT
    batter,
    SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;


-- 2. Top 10 Batters by Number of Fours
SELECT
    batter,
    COUNT(*) AS total_fours
FROM deliveries
WHERE batsman_runs = 4
GROUP BY batter
ORDER BY total_fours DESC
LIMIT 10;


-- 3. Top 10 Batters by Number of Sixes
SELECT
    batter,
    COUNT(*) AS total_sixes
FROM deliveries
WHERE batsman_runs = 6
GROUP BY batter
ORDER BY total_sixes DESC
LIMIT 10;


-- 4. Best Strike Rates
-- Minimum 500 runs for fair comparison
SELECT
    batter,
    SUM(batsman_runs) AS total_runs,
    COUNT(*) AS balls_faced,
    ROUND(
        SUM(batsman_runs) * 100.0 / COUNT(*),
        2
    ) AS strike_rate
FROM deliveries
GROUP BY batter
HAVING SUM(batsman_runs) >= 500
ORDER BY strike_rate DESC
LIMIT 10;