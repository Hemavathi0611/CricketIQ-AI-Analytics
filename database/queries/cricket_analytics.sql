-- ==================================================
-- CRICKETIQ AI ANALYTICS - SQL ANALYSIS QUERIES
-- ==================================================

USE cricketiq_analytics;


-- ==================================================
-- 1. TOP 10 RUN SCORERS
-- ==================================================

SELECT
    batter,
    SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;


-- ==================================================
-- 2. TOP 10 WICKET TAKERS
-- ==================================================

SELECT
    bowler,
    COUNT(*) AS total_wickets
FROM deliveries
WHERE is_wicket = 1
AND dismissal_kind NOT IN (
    'run out',
    'retired hurt',
    'obstructing the field'
)
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10;


-- ==================================================
-- 3. TOP 10 BATTERS BY NUMBER OF SIXES
-- ==================================================

SELECT
    batter,
    COUNT(*) AS total_sixes
FROM deliveries
WHERE batsman_runs = 6
GROUP BY batter
ORDER BY total_sixes DESC
LIMIT 10;


-- ==================================================
-- 4. TOP 10 BATTERS BY NUMBER OF FOURS
-- ==================================================

SELECT
    batter,
    COUNT(*) AS total_fours
FROM deliveries
WHERE batsman_runs = 4
GROUP BY batter
ORDER BY total_fours DESC
LIMIT 10;


-- ==================================================
-- 5. TEAM-WISE MATCH WINS
-- ==================================================

SELECT
    winner AS team,
    COUNT(*) AS total_wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY total_wins DESC;


-- ==================================================
-- 6. MOST SUCCESSFUL TEAM
-- ==================================================

SELECT
    winner AS team,
    COUNT(*) AS total_wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY total_wins DESC
LIMIT 1;


-- ==================================================
-- 7. TOTAL MATCHES PLAYED BY EACH TEAM
-- ==================================================

SELECT
    team,
    COUNT(*) AS matches_played
FROM (
    SELECT team1 AS team
    FROM matches

    UNION ALL

    SELECT team2 AS team
    FROM matches
) AS all_teams
GROUP BY team
ORDER BY matches_played DESC;


-- ==================================================
-- 8. TOP 10 BATTERS BY STRIKE RATE
-- Minimum 500 runs included for fair comparison
-- ==================================================

SELECT
    batter,
    SUM(batsman_runs) AS total_runs,
    COUNT(*) AS balls_faced,
    ROUND(
        SUM(batsman_runs) * 100.0 /
        COUNT(*),
        2
    ) AS strike_rate
FROM deliveries
GROUP BY batter
HAVING SUM(batsman_runs) >= 500
ORDER BY strike_rate DESC
LIMIT 10;