USE cricketiq_analytics;

-- ==========================================
-- MATCH ANALYSIS
-- ==========================================

-- 1. Team-wise Total Wins
SELECT
    winner AS team,
    COUNT(*) AS total_wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY total_wins DESC;


-- 2. Team-wise Total Matches Played
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


-- 3. Player of the Match Awards
SELECT
    player_of_match,
    COUNT(*) AS total_awards
FROM matches
WHERE player_of_match IS NOT NULL
GROUP BY player_of_match
ORDER BY total_awards DESC
LIMIT 10;


-- 4. Season-wise Number of Matches
SELECT
    season,
    COUNT(*) AS total_matches
FROM matches
GROUP BY season
ORDER BY season;


-- 5. Most Successful Teams by Win Percentage
SELECT
    team,
    matches_played,
    matches_won,
    ROUND(
        matches_won * 100.0 / matches_played,
        2
    ) AS win_percentage
FROM (
    SELECT
        team,
        COUNT(*) AS matches_played,
        SUM(
            CASE
                WHEN winner = team THEN 1
                ELSE 0
            END
        ) AS matches_won
    FROM (
        SELECT
            team1 AS team,
            winner
        FROM matches

        UNION ALL

        SELECT
            team2 AS team,
            winner
        FROM matches
    ) AS team_matches
    GROUP BY team
) AS team_statistics
ORDER BY win_percentage DESC;