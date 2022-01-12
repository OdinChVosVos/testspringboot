CREATE TABLE public.bd(
	id Serial Primary key NOT NULL,
	login text NOT NULL unique,
	password text NULL,
	achieves int NOT NULL,
	points int NOT NULL,
	status int NOT NULL
);

create unique index bd_id_uin on public.bd(id);
CREATE SEQUENCE bd_seq START with 1 OWNED BY bd.id;
INSERT INTO bd VALUES (0, 'admin', 'admin', 4, 0, 1);

CREATE TABLE public.journal(
	id serial Primary key NOT NULL,
	kol_vis int NULL,
	popad int NULL,
	user_id int NOT NULL,
	CONSTRAINT journal_bd_id_fk FOREIGN KEY (user_id) REFERENCES bd(id) on update cascade
);

create unique index journal_id_uin on public.journal(id);
CREATE SEQUENCE journal_seq START with 1 OWNED BY journal.id;