CREATE DATABASE IF NOT EXISTS `agenciadeviajes`;
USE `agenciadeviajes`;

CREATE TABLE IF NOT EXISTS `rol` (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO rol VALUES (1, 'Administrador'), (2, 'Cliente');

CREATE TABLE IF NOT EXISTS `usuario` (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) DEFAULT NULL,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rolId INT DEFAULT 2,
    FOREIGN KEY (rolId) REFERENCES Rol(id),
	fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion DATETIME ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO usuario (nombre, apellido, email, password_hash, rolId) VALUES 
("John", "Doe", "email@example.com", "", 1);
