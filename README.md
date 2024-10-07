# fastapi-spark-oracle

SQL> connect sys as sysdba;
Enter password: 

To create pdb database, first In SQL*Plus, ensure that the current container is the CDB root or an application root. after connect
CREATE PLUGGABLE DATABASE pdbfastapi ADMIN USER pdbfastapiadmin IDENTIFIED BY oracle FILE_NAME_CONVERT = ('/opt/oracle/oradata/ORCLCDB/pdbseed/', '/opt/oracle/oradata/ORCLCDB/pdbfastapi/');


SQL> show pdbs;

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 ORCLPDB1                       READ WRITE NO
         4 PDBFASTAPI                     MOUNTED


SQL> alter pluggable database pdbfastapi OPEN;

SQL> show pdbs;

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 ORCLPDB1                       READ WRITE NO
         4 PDBFASTAPI                     READ WRITE NO


SQL> ALTER SESSION SET CONTAINER = pdbfastapi;


CREATE USER grillazz IDENTIFIED BY oracle;

GRANT CONNECT, RESOURCE, DBA TO grillazz;

Oracle Database 21c Enterprise Edition Release 21.0.0.0.0 - Production
Version 21.3.0.0.0

SQL> connect grillazz@pdbfastapi;
Enter password: 
Connected.
SQL> 
