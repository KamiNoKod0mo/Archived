-- Criar o banco de dados
CREATE DATABASE videoroom;

-- Usar o banco de dados criado
USE videoroom;

-- Tabela para usuários
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY, -- ID único do usuário
    nome VARCHAR(100) NOT NULL,        -- Nome do usuário
    senha VARCHAR(255) NOT NULL,       -- Senha do usuário (recomenda-se armazenar como hash)
    email VARCHAR(150) UNIQUE NOT NULL -- Email do usuário (único)
);

-- Tabela para salas
CREATE TABLE sala (
    criador VARCHAR(255) NOT NULL,        -- ID do usuário que criou a sala
    npart INT,
    hash VARCHAR(255) PRIMARY KEY   -- URL única da sala (usada como identificador)
);
