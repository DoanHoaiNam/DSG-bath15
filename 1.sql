CREATE TABLE Benhnhan (
  Benh text,
  NhomBenh text
);
COPY Benhnhan(Benh, NhomBenh)
FROM 'D:\benhVaNhomBenh_cleaned.csv'
DELIMITER ','
CSV HEADER;
