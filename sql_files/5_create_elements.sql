CREATE TABLE elements (
    id_element SERIAL PRIMARY KEY,
    domain_code varchar (10) NOT NULL,
    domain varchar (200) NOT NULL,
    element_code integer NOT NULL,
    element varchar (100) NOT NULL,
    unit varchar (50)
);