create database faqdb;

use faqdb;

create table FAQ (
	FAQ_ID int auto_increment primary key,
    QUESTION varchar(3000) not null,
    ANSWER text not null
    -- COMPANY_ID int,
    -- foreign key (COMPANY_ID) references COMPANY(COMPAY_ID)-- 
);