create database granja

go

CREATE TABLE Cultivos (
    idCultivos INT PRIMARY KEY IDENTITY(1,1),
    NombreCultivo NVARCHAR(100),
    TipoCultivo NVARCHAR(50),
    AreaCultivo DECIMAL(10,2),
    Rendimiento DECIMAL(10,2)
);
GO

INSERT INTO Cultivos (NombreCultivo, TipoCultivo, AreaCultivo, Rendimiento) 
VALUES 
('Maíz', 'Cereal', 100.50, 250.75),
('patata', 'tuberculo', 75.25, 180.30),
('Arroz', 'Cereal', 120.75, 300.90),
('Fresa', 'Fruta', 50.80, 150.25),
('Zanahoria', 'tuberculo', 200.00, 500.00);
GO

CREATE TABLE Ganado (
    idGanado INT PRIMARY KEY IDENTITY(1,1),
    Especie NVARCHAR(100),
    Edad INT,
    Raza NVARCHAR(50),
    Peso DECIMAL(10,2)
);
GO

INSERT INTO Ganado (Especie, Edad, Raza, Peso) 
VALUES 
('Vaca', 5, 'Holstein', 500.00),
('Cabra', 3, 'Saanen', 80.25),
('Oveja', 2, 'Merina', 70.50),
('Cerdo', 1, 'Choctaw', 120.75),
('Gallina', 1, 'Orpington', 2.00);
GO

