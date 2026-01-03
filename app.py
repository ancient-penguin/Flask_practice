from flask import Flask

# Flask 앱(객체)을 생성합니다.
app = Flask(__name__)

# @app.route는 주소창에 '/' (메인 페이지)를 입력하면
# 아래 함수를 실행하라는 뜻입니다.
@app.route('/')
def home():
    return "Hello, My Memo!"

# 이 파일이 직접 실행될 때만 서버를 켭니다.
if __name__ == '__main__':
    # debug=True는 코드를 고치면 서버가 알아서 재시작되게 해줍니다. (개발할 때 아주 편함!)
    app.run(debug=True)