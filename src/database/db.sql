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


CREATE TABLE IF NOT EXISTS `destino` (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(55) NOT NULL,
    descripcion VARCHAR(255) DEFAULT NULL,
    costo DECIMAL(65, 2)
);

CREATE TABLE IF NOT EXISTS `actividad` (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(55) NOT NULL,
    descripcion VARCHAR(255) DEFAULT NULL,
    destinoId INT,
	FOREIGN KEY (destinoId) REFERENCES Destino(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS `PaqueteTuristico` (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS `PaqueteXDestino` (
paqueteId INT NOT NULL,
destinoId INT NOT NULL,
PRIMARY KEY (paqueteId, destinoId),
FOREIGN KEY (paqueteId) REFERENCES PaqueteTuristico(id) ON DELETE CASCADE,
FOREIGN KEY (destinoId) REFERENCES Destino(id)
);

CREATE TABLE Reserva (
userId INT NOT NULL,
paqueteId INT NOT NULL,
PRIMARY KEY (userId, paqueteId),
FOREIGN KEY (userId) REFERENCES Usuario(id),
FOREIGN KEY (paqueteId) REFERENCES PaqueteTuristico(id) ON DELETE CASCADE,
fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);