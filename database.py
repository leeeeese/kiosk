import pymysql

# MySQL 연결 설정
db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pingpong"
)

cursor = db.cursor()

# 사용자 정보 가져오기


def get_user(qr_code=None, rfid=None):
    if qr_code:
        cursor.execute("SELECT id FROM users WHERE qr_code=%s", (qr_code,))
    elif rfid:
        cursor.execute("SELECT id FROM users WHERE rfid_tag=%s", (rfid,))

    return cursor.fetchone()

# 출입 기록 저장


def log_entry(user_id):
    cursor.execute("INSERT INTO access_logs (user_id) VALUES (%s)", (user_id,))
    db.commit()


db.close()
