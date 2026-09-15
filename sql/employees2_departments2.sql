-- =========================================================
-- EMPLOYEES2 and DEPARTMENTS2 Tables
-- Oracle SQL
-- =========================================================

-- Drop tables if they already exist
BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE EMPLOYEES2 CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN RAISE; END IF;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE DEPARTMENTS2 CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN RAISE; END IF;
END;
/

-- =========================================================
-- 1. Create DEPARTMENTS2 table
-- =========================================================

CREATE TABLE DEPARTMENTS2 (
    DEPT_ID   VARCHAR2(10) PRIMARY KEY,
    DEPT_NAME VARCHAR2(50) NOT NULL
);

-- =========================================================
-- 2. Create EMPLOYEES2 table
-- =========================================================

CREATE TABLE EMPLOYEES2 (
    EMP_ID   VARCHAR2(10) PRIMARY KEY,
    NAME     VARCHAR2(50) NOT NULL,
    AGE      NUMBER(3),
    DOJ      DATE NOT NULL,
    SALARY   NUMBER(10,2) CHECK (SALARY >= 0),
    DEPT_ID  VARCHAR2(10) NOT NULL,
    MOB_NO   VARCHAR2(15) UNIQUE,
    MAIL_ID  VARCHAR2(100) UNIQUE,
    CITY     VARCHAR2(50),

    CONSTRAINT FK_EMP_DEPT
        FOREIGN KEY (DEPT_ID)
        REFERENCES DEPARTMENTS2(DEPT_ID),

    CONSTRAINT CHK_AGE
        CHECK (AGE >= 18)
);

-- =========================================================
-- 3. Insert data into DEPARTMENTS2
-- =========================================================

INSERT INTO DEPARTMENTS2 VALUES ('D001', 'HR');
INSERT INTO DEPARTMENTS2 VALUES ('D002', 'Finance');
INSERT INTO DEPARTMENTS2 VALUES ('D003', 'IT');
INSERT INTO DEPARTMENTS2 VALUES ('D004', 'Operations');
INSERT INTO DEPARTMENTS2 VALUES ('D005', 'Marketing');

-- =========================================================
-- 4. Insert data into EMPLOYEES2
-- =========================================================

INSERT INTO EMPLOYEES2
VALUES ('EMP0001', 'Ramesh Sharma', 32,
        TO_DATE('12-JUL-2025','DD-MON-YYYY'),
        50000.00, 'D001', '9876543210',
        'Ramesh@gmail.com', 'Gwalior');

INSERT INTO EMPLOYEES2
VALUES ('EMP0002', 'Mukesh Verma', 40,
        TO_DATE('24-JUL-2025','DD-MON-YYYY'),
        60000.00, 'D002', '9876543211',
        'Mukesh@gmail.com', 'Gwalior');

INSERT INTO EMPLOYEES2
VALUES ('EMP0003', 'Sumit Singh', 45,
        TO_DATE('15-JAN-2025','DD-MON-YYYY'),
        45000.00, 'D002', '9876543212',
        'Sumit@gmail.com', 'Bhopal');

INSERT INTO EMPLOYEES2
VALUES ('EMP0004', 'Kaushik Singh', 25,
        TO_DATE('25-SEP-2025','DD-MON-YYYY'),
        25000.00, 'D003', '9876543213',
        'Kaushik@gmail.com', 'Bhopal');

INSERT INTO EMPLOYEES2
VALUES ('EMP0005', 'Hardik Patel', 29,
        TO_DATE('18-FEB-2025','DD-MON-YYYY'),
        35000.00, 'D004', '9876543214',
        'Hardik@gmail.com', 'Gwalior');

INSERT INTO EMPLOYEES2
VALUES ('EMP0006', 'Komal Malhotra', 38,
        TO_DATE('20-APR-2025','DD-MON-YYYY'),
        75000.00, 'D004', '9876543215',
        'Komal@gmail.com', 'Morena');

INSERT INTO EMPLOYEES2
VALUES ('EMP0007', 'Ayush', NULL,
        TO_DATE('22-JUN-2025','DD-MON-YYYY'),
        65000.00, 'D005', '9876543216',
        'Ayush@gmail.com', 'Bhind');

-- =========================================================
-- 5. Save changes
-- =========================================================

COMMIT;

-- =========================================================
-- 6. Verify tables
-- =========================================================

SELECT * FROM DEPARTMENTS2;
SELECT * FROM EMPLOYEES2;
