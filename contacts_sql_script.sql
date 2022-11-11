drop database if exists contacts;
create database contacts;

use contacts;

drop table if exists email;
drop table if exists address;
drop table if exists phone;
drop table if exists address_type;
drop table if exists phone_type;
drop table if exists email_type;
drop table if exists student;

create table email_type(
	`id` int auto_increment,
    `description` varchar(50) not null,
    primary key (`id`)
);

create table address_type(
	`id` int auto_increment,
    `description` varchar(50) not null,
    primary key (`id`)
);

create table phone_type(
	`id` int auto_increment,
    `description` varchar(50) not null,
    primary key (`id`)
);

create table student(
	`uni` varchar(10) not null,
    primary key(`uni`)
);

create table email(
	`id` int auto_increment,
    `type_id` int not null,
    `uni` varchar(10) not null,
    `address` varchar(50) not null,
    primary key(`id`),
    foreign key(`type_id`)
		references email_type(`id`),
	foreign key(`uni`)
		references student(`uni`)
);

create table address(
	`id` int auto_increment,
    `type_id` int not null,
    `uni` varchar(10) not null,
    `country` varchar(50) not null,
    `state` varchar(50) not null,
    `city` varchar(50) not null,
    `zip_code` varchar(10) not null,
    `street` varchar(100) not null,
    primary key(`id`),
    foreign key(`type_id`)
		references address_type(`id`),
	foreign key(`uni`)
		references student(`uni`)
);

create table phone(
	`id` int auto_increment,
    `type_id` int not null,
    `uni` varchar(10) not null,
    `country_code` varchar(10) not null,
    `phone_no` varchar(20) not null,
    primary key(`id`),
    foreign key(`type_id`)
		references phone_type(`id`),
	foreign key(`uni`)
		references student(`uni`)
);

insert into email_type (`description`)
values ("personal");
insert into email_type (`description`)
values ("work");
insert into email_type (`description`)
values ("education");

insert into address_type (`description`)
values ("home");
insert into address_type (`description`)
values ("work");
insert into address_type (`description`)
values ("campus");

insert into phone_type (`description`)
values ("home");
insert into phone_type (`description`)
values ("mobile");
insert into phone_type (`description`)
values ("work");