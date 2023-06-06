CREATE TABLE IF NOT EXISTS audio_users(
	id serial primary key, 
	name VARCHAR(100), 
	token UUID
	);
CREATE TABLE IF NOT EXISTS audio_records(
	id UUID,
	filename VARCHAR(150),
	record BYTEA,
	user_id INTEGER REFERENCES audio_users(id) ON DELETE SET NULL (user_id)  
	);
