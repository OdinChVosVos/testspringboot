Create table public.history(
    id Serial primary key not null,
    event text
);

create unique index history_id_uni on public.history(id);