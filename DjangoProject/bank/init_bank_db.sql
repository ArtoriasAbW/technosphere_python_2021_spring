CREATE SEQUENCE department_id_seq;
CREATE SEQUENCE client_id_seq;

CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER DEFAULT nextval('client_id_seq') PRIMARY KEY,
    client_name VARCHAR(80) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(50),
    client_address VARCHAR(200),
    registration_date DATE NOT NULL,
);


CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER DEFAULT nextval('department_id_seq') PRIMARY KEY,
    department_name VARCHAR(80) NOT NULL,
    department_address VARCHAR(200) NOT NULL,
    department_phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS accounts (
    account_number VARCHAR(12) PRIMARY KEY,
    account_status VARCHAR(15) NOT NULL,
    client INTEGER REFERENCES clients ON DELETE CASCADE NOT NULL,
    account_balance FLOAT NOT NULL,
    department INTEGER REFERENCES departments ON DELETE CASCADE NOT NULL,
    opening_date DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(15) PRIMARY KEY,
    transaction_date timestamp NOT NULL,
    sender VARCHAR(12) REFERENCES accounts ON DELETE CASCADE NOT NULL,
    receiver VARCHAR(12) REFERENCES accounts ON DELETE CASCADE NOT NULL,
    amount FLOAT NOT NULL    
);
 
