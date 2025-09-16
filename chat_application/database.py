import psycopg2
conn = psycopg2.connect(
       database = "postgres",
       user = "postgres",
       password = "trisha123",
       port = 5432,
       host = "localhost"
)
def create_tables():
    with conn.cursor() as cursor:
        cursor.execute("create table if not exists user_table(id serial primary key,username TEXT UNIQUE NOT NULL)")
        cursor.execute("create table if not exists messages(id serial primary key,sender_id INT references user_table(id),receiver_id INT references user_table(id),message TEXT not null,timestamp TIMESTAMP default CURRENT_TIMESTAMP)")
        conn.commit()

def add_user(username):
    with conn.cursor() as cursor:
        cursor.execute("insert into user_table(username) values(%s) ON CONFLICT DO NOTHING;",(username,))
    conn.commit()
def add_message(sender_id,receiver_id,message):
    with conn.cursor() as cursor:
        cursor.execute("insert into messages(sender_id,receiver_id,message) values(%s,%s,%s);",(sender_id,receiver_id,message))
    conn.commit()

def chat_history(user1_id,user2_id):
    with conn.cursor() as cursor:
        cursor.execute(""" 
                     select u1.username,u2.username,m.message,m.timestamp
                     from messages as m 
                     join user_table as u1 on m.sender_id = u1.id
                     join user_table as u2 on m.receiver_id = u2.id
                     where (m.sender_id =  %s and m.receiver_id = %s);
                        """,(user1_id,user2_id))
        rows = cursor.fetchall()
        for row in rows:

            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        
