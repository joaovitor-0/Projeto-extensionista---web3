CREATE TABLE voluntarios (

    id SERIAL PRIMARY KEY,

    -- Campos obrigatórios
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,

    -- Campos opcionais
    telefone VARCHAR(20),

    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);