-- SHow all the cities of California that
-- can be found in the database hbtn_0d_usa.
SELECT id, name From cities Where state_id = (
SELECT id FROM states WHERE = name = "California");
