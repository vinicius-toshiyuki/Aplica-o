CREATE TABLE IF NOT EXISTS PROFESSOR (
		COD SERIAL PRIMARY KEY,
		NOME VARCHAR(500) NOT NULL,
		SENHA VARCHAR(50) NOT NULL,
		FOTO OID,
		DATA_NASC DATE,
		DATA_CADR TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC+3') NOT NULL
);

CREATE TABLE IF NOT EXISTS DISCIPLINA (
		COD SERIAL PRIMARY KEY,
		NOME VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS TURMA (
		COD INTEGER,
		SEMESTRE CHAR(5), -- ex.: 20171
		PROF_COD INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,
		PRIMARY KEY (COD, SEMESTRE),
		FOREIGN KEY (PROF_COD) REFERENCES PROFESSOR(COD),
		FOREIGN KEY (DISC_COD) REFERENCES DISCIPLINA(COD)
);

CREATE TABLE IF NOT EXISTS ALUNO (
		MATRICULA DECIMAL(9) PRIMARY KEY,
		NOME VARCHAR(500),
		SENHA VARCHAR(500),
		FOTO OID,
		DATA_NASC DATE,
		DATA_CADR TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC+3') NOT NULL,

		TURMA_COD INTEGER,
		TURMA_SEMESTRE CHAR,
		FOREIGN KEY (TURMA_COD, TURMA_SEMESTRE) REFERENCES TURMA(COD, SEMESTRE)
);

CREATE TABLE IF NOT EXISTS MONITOR_TURMA (
		ALUNO_MATR DECIMAL(9),
		TURMA_COD INTEGER,
		TURMA_SEMESTRE CHAR(5),
		PRIMARY KEY (ALUNO_MATR, TURMA_COD, TURMA_SEMESTRE),
		FOREIGN KEY (ALUNO_MATR) REFERENCES ALUNO(MATRICULA),
		FOREIGN KEY (TURMA_COD, TURMA_SEMESTRE) REFERENCES TURMA(COD, SEMESTRE)
);

CREATE TABLE IF NOT EXISTS LING_PROGR (
		COD INTEGER PRIMARY KEY,
		NOME VARCHAR(500) NOT NULL,
		COMAND_COMPILA VARCHAR(1000) NOT NULL
);

CREATE TABLE IF NOT EXISTS LING_PROGR_DISCI (
		LING_PROGR_COD INTEGER,
		DISC_COD INTEGER,
		PRIMARY KEY (LING_PROGR_COD, DISC_COD),
		FOREIGN KEY (LING_PROGR_COD) REFERENCES LING_PROGR(COD),
		FOREIGN KEY (DISC_COD) REFERENCES DISCIPLINA(COD)
);

CREATE TABLE IF NOT EXISTS MODULO (
		NUMERO INTEGER,
		DISC_COD INTEGER,
		PRIMARY KEY (NUMERO, DISC_COD),
		FOREIGN KEY (DISC_COD) REFERENCES DISCIPLINA(COD)
);

CREATE TABLE IF NOT EXISTS LISTA (
		COD INTEGER PRIMARY KEY,
		DESCR VARCHAR(4000) NOT NULL, -- mudar para binario, pois pode armazenar um pdf
		DATA_HR_INICIO TIMESTAMP,
		DATA_HR_FIM TIMESTAMP,
		VISIBILIDADE CHAR(1) NOT NULL,
		PROVA CHAR(1) NOT NULL,
		MODULO_COD INTEGER,
		DISC_COD INTEGER,
		FOREIGN KEY (MODULO_COD, DISC_COD) REFERENCES MODULO(NUMERO, DISC_COD)
);

CREATE TABLE IF NOT EXISTS PROBLEMA (
		COD INTEGER,
		LISTA_COD INTEGER,
		TITULO VARCHAR(300),
		DESCR VARCHAR(4000),
		DIFICUL VARCHAR(50),
		LIMITE_MEM VARCHAR(500),
		LIMITE_TEMP VARCHAR(500),
		PRIMARY KEY (COD, LISTA_COD),
		FOREIGN KEY (LISTA_COD) REFERENCES LISTA(COD)
);

CREATE TABLE IF NOT EXISTS ENTRADA (
		COD INTEGER,
		PROBLEMA_COD INTEGER NOT NULL,
		LISTA_COD INTEGER NOT NULL,
		ENTRADA VARCHAR(4000) NOT NULL,
		PRIMARY KEY (COD, PROBLEMA_COD),
		FOREIGN KEY (PROBLEMA_COD, LISTA_COD) REFERENCES PROBLEMA(COD, LISTA_COD)
);

CREATE TABLE IF NOT EXISTS SAIDA (
		COD INTEGER,
		PROBLEMA_COD INTEGER NOT NULL,
		LISTA_COD INTEGER NOT NULL,
		SAIDA VARCHAR(4000) NOT NULL,
		PRIMARY KEY (COD, PROBLEMA_COD),
		FOREIGN KEY (PROBLEMA_COD, LISTA_COD) REFERENCES PROBLEMA(COD, LISTA_COD)
);

CREATE TABLE IF NOT EXISTS SUBMISSAO (
		COD INTEGER PRIMARY KEY,
		DATA_HORA TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC+3') NOT NULL,
		CODI_FONTE TEXT NOT NULL,
		MEM_UTILI VARCHAR(4000),
		TEMPO_EXEC VARCHAR(4000),
		VEREDITO VARCHAR(500) NOT NULL,
		ALUNO_MATR DECIMAL(9),
		PROBLEMA_COD INTEGER,
		LISTA_COD INTEGER,
		LING_PROGR_COD INTEGER,
		FOREIGN KEY (ALUNO_MATR) REFERENCES ALUNO(MATRICULA),
		FOREIGN KEY (PROBLEMA_COD, LISTA_COD) REFERENCES PROBLEMA(COD, LISTA_COD),
		FOREIGN KEY (LING_PROGR_COD) REFERENCES LING_PROGR(COD)
);











