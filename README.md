# 도커 모니터링 대시보드

## 🖼️ 스크린샷
<img width="1498" alt="monitor-screenshot" src="https://github.com/user-attachments/assets/0e8fc1e7-398a-4ba2-bc34-9b0ae72f4067" />

## 📌 프로젝트 개요
Docker Monitoring Dashboard는 도커 컨테이너 및 시스템 리소스를 실시간으로 모니터링할 수 있는 대시보드 애플리케이션입니다. 사용자는 컨테이너 상태, 리소스 사용량(CPU, 메모리, 네트워크, 디스크 I/O) 등을 직관적으로 확인할 수 있습니다.

## 🚀 주요 기능
- **컨테이너 리스트 및 상태 확인**: 실행 중인 컨테이너 목록과 상태를 실시간으로 확인
- **리소스 사용량 시각화**: CPU, 메모리, 네트워크 트래픽 및 디스크 사용량을 그래프로 표시
- **컨테이너 로그 조회**: 특정 컨테이너의 실시간 로그 확인 기능 제공

## 🕑 앞으로의 계획
- **알림 시스템**: 특정 리소스 사용량 초과 시 알림 전송 기능
- **사용자 권한별 관리**: 사용자별 권한에 따라 수동 관리
- **수동 컨테이너 관리**: 컨테이너를 수동으로 시작, 종료, 재시작 하도록 하는 관리 기능


### 1️⃣ 환경 설정
이 프로젝트를 실행하기 위해 다음과 같은 환경이 필요합니다:
- Docker (버전 20.x 이상 권장)
- Python (버전 3.12)

### 2️⃣ 프로젝트 클론
```sh
git clone https://github.com/dev-holim/docker-monitering.git
cd docker-monitering
```

### 3️⃣ 환경 변수 설정
`.env` 파일을 생성하고 필요한 변수를 설정합니다:

```
# 예제 환경 변수 파일
DEBUG=True

DATABASE_NAME=
DATABASE_HOST=
DATABASE_PORT=
DATABASE_USER_NAME=
DATABASE_USER_PASSWORD=
DATABASE_SCHEMA=
```

## 4️⃣ 🔧설치 및 실행 방법
```bash
pip install -r requirements.txt
```

```bash
gunicorn -k eventlet -w 1 run:app
```

### 5️⃣ 대시보드 접속
```
http://127.0.0.1:8000
```
