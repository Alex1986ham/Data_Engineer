# NOT NULL
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL,
    store_id int,
    spent numeric
);

# UNIQUE
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL UNIQUE,
    sotre_id int NOT NULL UNIQUE,
    spent numeric
);

CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL,
    store_id int NOT NULL,
    spent numeric,
    UNIQUE (customer_id, sotre_id)
);


# Primary Key / the primary key constraint has the unique and not null constraint built if __name__ == '__main__':
CREATE TABLE IF NOT EXSITS store (
    store_id int PRIMARY KEY,
    sotre_location_city text,
);

CREATE TABLE IF NOT EXISTS store (
    customer_id int,
    sotre_id int,
    spent numeric,
    PRIMARY KEY (customer_id, store_id)
)
