from fastapi import FastAPI
import database
import door_control

app = FastAPI()


@app.post("/check_access")
def check_access(data: dict):
    qr_code = data.get("qr_code")
    rfid = data.get("rfid")

    user = database.get_user(qr_code=qr_code, rfid=rfid)

    if user:
        database.log_entry(user[0])  # DB에 출입 기록 저장
        door_control.open_door()  # 문 열기
        return {"status": "approved"}
    else:
        return {"status": "denied"}
