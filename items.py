import db

def add_item(title, artist, rating, comment, user_id):
    sql = "INSERT INTO items (title, artist, rating, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, artist, rating, user_id])
    item_id = db.last_insert_id()
    
    sql = "INSERT INTO comments (item_id, user_id, content) VALUES (?, ?, ?)"
    db.execute(sql, [item_id, user_id, comment])
def get_items():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):   
    sql = """SELECT items.id, items.title, items.artist, items.rating,
        comments.content AS comment, users.username, users.id user_id
        FROM items
        LEFT JOIN users ON items.user_id = users.id
        LEFT JOIN comments ON comments.item_id = items.id
        WHERE items.id = ?"""
    results = db.query(sql, [item_id])
    return results[0] if results else None

def update_item(item_id, title, artist, rating, comment):
    sql = """UPDATE items SET title = ?, artist = ?, rating = ?
            WHERE id = ?"""
    db.execute(sql, [title, artist, rating, item_id])

    sql = """UPDATE comments SET content = ?
            WHERE item_id = ? AND user_id = (SELECT user_id FROM items WHERE id = ?)"""
    db.execute(sql, [comment, item_id, item_id])
            
                

