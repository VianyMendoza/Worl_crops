CREATE TABLE items (
    id_item SERIAL PRIMARY KEY,
    domain_code varchar (10) NOT NULL,
    domain varchar (200) NOT NULL,
    item_code integer NOT NULL,
    item varchar (200) NOT NULL,
    description varchar (5000),
    hs_code varchar (10),
    hs07_code varchar (500),
    hs12_code varchar (500),
    cpc_code varchar (10)
);
    