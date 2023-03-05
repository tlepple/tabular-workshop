CREATE TABLE IF NOT EXISTS `<your warehouse>`.`<your database>`.customer (
    first_name STRING,
    last_name STRING,
    street_address STRING,
    city STRING,
    state STRING,
    zip_code STRING,
    home_phone STRING,
    mobile STRING,
    email STRING,
    ssn STRING,
    job_title STRING,
    create_date STRING,
    cust_id BIGINT)
USING iceberg;
