CREATE ROLE datagen LOGIN PASSWORD 'supersecret1';
CREATE DATABASE datagen OWNER datagen ENCODING 'UTF-8';
ALTER ROLE "datagen" WITH LOGIN;
ALTER ROLE "datagen" WITH REPLICATION;