ALTER TABLE told RENAME to tnew

ALTER TABLE told RENAME cold TO cnew

ALTER TABLE IF EXISTS told RENAME cold TO cnew

ALTER TABLE IF EXISTS cold RENAME TO told

ALTER FUNCTION oldfunc(int) RENAME TO newfunc

ALTER SCHEMA s1 RENAME TO s2

ALTER DATABASE db1 RENAME TO db2
