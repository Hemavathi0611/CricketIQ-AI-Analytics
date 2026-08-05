CREATE DATABASE IF NOT EXISTS cricketiq_analytics;

USE cricketiq_analytics;

CREATE TABLE matches (
    match_id INT PRIMARY KEY,
    season VARCHAR(20),
    city VARCHAR(100),
    match_date DATE,
    match_type VARCHAR(50),
    player_of_match VARCHAR(100),
    venue VARCHAR(200),
    team1 VARCHAR(100),
    team2 VARCHAR(100),
    toss_winner VARCHAR(100),
    toss_decision VARCHAR(20),
    winner VARCHAR(100),
    result VARCHAR(50),
    result_margin FLOAT,
    target_runs FLOAT,
    target_overs FLOAT,
    super_over VARCHAR(10),
    method VARCHAR(50),
    umpire1 VARCHAR(100),
    umpire2 VARCHAR(100)
);


CREATE TABLE deliveries (
    delivery_id BIGINT AUTO_INCREMENT PRIMARY KEY,

    match_id INT NOT NULL,
    inning INT,

    batting_team VARCHAR(100),
    bowling_team VARCHAR(100),

    over_number INT,
    ball_number INT,

    batter VARCHAR(100),
    bowler VARCHAR(100),
    non_striker VARCHAR(100),

    batsman_runs INT,
    extra_runs INT,
    total_runs INT,

    extras_type VARCHAR(50),

    is_wicket TINYINT,

    player_dismissed VARCHAR(100),
    dismissal_kind VARCHAR(50),
    fielder VARCHAR(100),

    FOREIGN KEY (match_id)
        REFERENCES matches(match_id)
);