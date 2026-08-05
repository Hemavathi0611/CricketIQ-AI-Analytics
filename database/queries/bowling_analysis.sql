USE cricketiq_analytics;

-- ==========================================
-- BOWLING ANALYSIS
-- ==========================================

-- 1. Top 10 Wicket Takers
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


-- 2. Most Economical Bowlers
-- Minimum 500 balls bowled for fair comparison
SELECT
    bowler,
    COUNT(*) AS balls_bowled,
    SUM(total_runs) AS runs_conceded,
    ROUND(
        SUM(total_runs) * 6.0 / COUNT(*),
        2
    ) AS economy_rate
FROM deliveries
GROUP BY bowler
HAVING COUNT(*) >= 500
ORDER BY economy_rate ASC
LIMIT 10;


-- 3. Bowlers with the Most Dot Balls
SELECT
    bowler,
    COUNT(*) AS dot_balls
FROM deliveries
WHERE total_runs = 0
GROUP BY bowler
ORDER BY dot_balls DESC
LIMIT 10;


-- 4. Best Bowling Strike Rate
-- Minimum 50 wickets for fair comparison
SELECT
    bowler,
    COUNT(*) AS balls_bowled,
    SUM(
        CASE
            WHEN is_wicket = 1
            AND dismissal_kind NOT IN (
                'run out',
                'retired hurt',
                'obstructing the field'
            )
            THEN 1
            ELSE 0
        END
    ) AS total_wickets,
    ROUND(
        COUNT(*) * 1.0 /
        SUM(
            CASE
                WHEN is_wicket = 1
                AND dismissal_kind NOT IN (
                    'run out',
                    'retired hurt',
                    'obstructing the field'
                )
                THEN 1
                ELSE 0
            END
        ),
        2
    ) AS bowling_strike_rate
FROM deliveries
GROUP BY bowler
HAVING total_wickets >= 50
ORDER BY bowling_strike_rate ASC
LIMIT 10;