-- MySQL схема для задания "Flask + MySQL: авторизация"
-- Выполните этот скрипт один раз в MySQL-клиенте

CREATE DATABASE IF NOT EXISTS flask_auth;
USE flask_auth;

CREATE TABLE IF NOT EXISTS users (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    user_name     VARCHAR(64)  NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL
);

-- Тестовый пользователь из задания
INSERT INTO users (user_name, user_password)
VALUES ('Vladimir Putin', '123456789')
ON DUPLICATE KEY UPDATE user_password = VALUES(user_password);
