DROP TABLE IF EXISTS jpm_diplomas;
CREATE TABLE jpm_diplomas (
  school_name varchar(50),
  link varchar(100) not null,
  begin_date date,
  end_date date,
  language varchar(6) not null,
  cursus_content varchar(300),
  CONSTRAINT PK_Diplom PRIMARY KEY (link,language)
);
insert into jpm_diplomas (school_name, link, begin_date, end_date, language, cursus_content) values ('Ecole Centrale de Lille', 'https://centralelille.fr/', STR_TO_DATE('01/09/1988', '%d/%m/%Y'), STR_TO_DATE('01/01/1991', '%d/%m/%Y'), 'fr_FR', 'Ecole d''ingénieurs Généraliste du Concours Centrale anciennement IDN');
insert into jpm_diplomas (school_name, link, begin_date, end_date, language, cursus_content) values ('Ecole Centrale de Lille', 'https://centralelille.fr/en/', STR_TO_DATE('01/09/1988', '%d/%m/%Y'), STR_TO_DATE('01/01/1991', '%d/%m/%Y'), 'en_EN', 'General Enginnering School training top level engineers accessible though competitive exam after two years highscool');
insert into jpm_diplomas (school_name, link, begin_date, end_date, language, cursus_content) values ('Ecole Centrale de Lille', 'https://centralelille.fr/en/', STR_TO_DATE('01/09/1988', '%d/%m/%Y'), STR_TO_DATE('01/01/1991', '%d/%m/%Y'), 'de_DE', 'Ingenieur Hochschule sogennante <i>Grande Ecole</i> fûr allgemeine Ingenieur Asubildiung');