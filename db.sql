-- log table:
--
-- id| start            | end              |
-- 1 | 2017-08-09 09:05 | NULL             |
-- 
-- 
-- id| start            | end              |
-- 1 | 2017-08-09 09:05 | 2017-08-09 11:45 |


-- sqlite> .tables
-- sqlite> .help

-- schema
create table log (id INTEGER PRIMARY KEY, start datetime NOT NULL, end DATETIME);

-- query for getting the most recent entry
select * from log ORDER BY start DESC LIMIT 1;

-- when we start the program, we always run this:
-- (possibly, delete the last row if end is null)
insert into log (start) VALUES (datetime('now'));


-- updating the entry (the id should be replaced by
-- the one returned by the query for getting the most
-- recent entry
UPDATE log set end = datetime('now') WHERE id = 1;
