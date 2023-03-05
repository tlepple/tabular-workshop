CREATE TABLE IF NOT EXISTS `<your warehouse>`.`<your database>`.transactions (
    transact_id STRING,
    transaction_date STRING,
    item_desc STRING,
    barcode STRING,
    category STRING,
    amount STRING,
    cust_id BIGINT)
USING iceberg;
