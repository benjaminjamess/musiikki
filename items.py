import db

def add_item(title, artist, rating, comment, user_id):
    sql = "INSERT INTO items (title, artist, rating, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, artist, rating, user_id])
    item_id = db.last_insert_id()
    
    sql = "INSERT INTO comments (item_id, user_id, content) VALUES (?, ?, ?)"
    db.execute(sql, [item_id, user_id, comment])