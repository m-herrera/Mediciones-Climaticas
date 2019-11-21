CREATE KEYSPACE IF NOT EXISTS Clima WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};

CREATE TABLE IF NOT EXISTS Medicion
(
    IdMedicion  UUID PRIMARY KEY,
    Temperatura FLOAT,
    Humedad     FLOAT,
    Instante    TIMESTAMP
);
