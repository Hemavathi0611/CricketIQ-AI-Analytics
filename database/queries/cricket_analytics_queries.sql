USE cricketiq_analytics;

-- 1. Top 10 run scorers
SELECT
    batter,
    SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;


-- 2. Top 10 wicket-taking bowlers
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


-- 3. Top 10 players with the most sixes
SELECT
    batter,
    COUNT(*) AS total_sixes
FROM deliveries
WHERE batsman_runs = 6
GROUP BY batter
ORDER BY total_sixes DESC
LIMIT 10;


-- 4. Top 10 players with the most fours
SELECT
    batter,
    COUNT(*) AS total_fours
FROM deliveries
WHERE batsman_runs = 4
GROUP BY batter
ORDER BY total_fours DESC
LIMIT 10;


-- 5. Team-wise total runs
SELECT
    batting_team,
    SUM(total_runs) AS total_runs
FROM deliveries
GROUP BY batting_team
ORDER BY total_runs DESC;


-- 6. Team-wise total wins
SELECT
    winner,
    COUNT(*) AS total_wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY total_wins DESC;


-- 7. Player of the Match awards
SELECT
    player_of_match,
    COUNT(*) AS awards
FROM matches
WHERE player_of_match IS NOT NULL
GROUP BY player_of_match
ORDER BY awards DESC
LIMIT 10;


-- 8. Season-wise total matches
SELECT
    season,
    COUNT(*) AS total_matches
FROM matches
GROUP BY season
ORDER BY season;