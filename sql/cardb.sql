create database cardb;

use cardb;

CREATE TABLE IF NOT EXISTS tbl_car (
    car_id    INT PRIMARY KEY AUTO_INCREMENT,
    
    origin    INT NOT NULL,
    company   VARCHAR(100) NOT NULL,
    model     VARCHAR(100) NOT NULL,
    fuel      VARCHAR(50) NOT NULL,
    age       INT NOT NULL,
    pur_count INT NOT NULL
    
    -- INDEX idx_analysis (origin, age, model)
);