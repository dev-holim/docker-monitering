# 도커 모니터링 대시보드

## 📌 프로젝트 개요
Docker Monitoring Dashboard는 도커 컨테이너 및 시스템 리소스를 실시간으로 모니터링할 수 있는 대시보드 애플리케이션입니다. 사용자는 컨테이너 상태, 리소스 사용량(CPU, 메모리, 네트워크, 디스크 I/O) 등을 직관적으로 확인할 수 있습니다.

## 🚀 주요 기능
- **컨테이너 리스트 및 상태 확인**: 실행 중인 컨테이너 목록과 상태를 실시간으로 확인
- **리소스 사용량 시각화**: CPU, 메모리, 네트워크 트래픽 및 디스크 사용량을 그래프로 표시
- **컨테이너 로그 조회**: 특정 컨테이너의 실시간 로그 확인 기능 제공
- **알림 시스템**: 특정 리소스 사용량 초과 시 알림 전송 기능
- **다중 노드 지원**: 여러 개의 Docker 호스트를 모니터링할 수 있는 기능 지원
- **REST API 제공**: 데이터를 JSON 형태로 제공하는 API 지원

## 📂 폴더 구조
```
📂 docker-monitoring
├── 📂 app          # 백엔드 서버 (FastAPI, Flask, Node.js 등)
│   ├── app.py         # API 서버 메인 실행 파일
│   ├── requirements.txt # 필요한 Python 패키지 목록
│   ├── Dockerfile     # 백엔드용 Dockerfile
│   └── ...
├── 📂 frontend         # 프론트엔드 (React, Vue, Angular 등)
│   ├── src
│   ├── package.json   # Node.js 패키지 관리 파일
│   ├── Dockerfile     # 프론트엔드용 Dockerfile
│   └── ...
├── 📂 assets          # 스크린샷, 문서 자료 등
├── 📜 run.py          # 실행
├── 📜 docker-compose.yml # Docker Compose 설정 파일
├── 📜 .env             # 환경 변수 파일
├── 📜 README.md        # 프로젝트 설명 문서
└── 📜 LICENSE          # 라이선스 정보
```

## 🔧 설치 및 실행 방법

### 1️⃣ 환경 설정
이 프로젝트를 실행하기 위해 다음과 같은 환경이 필요합니다:

- Docker (버전 20.x 이상 권장)
- Docker Compose (버전 2.x 이상 권장)
- Node.js (프론트엔드 빌드용, 선택 사항)

### 2️⃣ 프로젝트 클론
```sh
git clone https://github.com/your-repo/docker-monitoring-dashboard.git
cd docker-monitoring-dashboard
```

### 3️⃣ 환경 변수 설정
`.env` 파일을 생성하고 필요한 변수를 설정합니다:

```
# 예제 환경 변수 파일
PORT=5000
DOCKER_API_URL=http://localhost:2375
```

### 4️⃣ Docker Compose 실행
```sh
docker-compose up -d
```

이 명령어를 실행하면 백엔드와 프론트엔드 컨테이너가 자동으로 실행됩니다.

### 5️⃣ 대시보드 접속
브라우저에서 아래 URL을 입력하여 대시보드에 접속할 수 있습니다:

```
http://localhost:3000
```

## 📡 API 사용 방법

### 컨테이너 리스트 조회

```sh
GET /api/containers
```

응답 예시:

```json
[
  {
    "id": "abcd1234",
    "name": "my-container",
    "status": "running",
    "cpu_usage": 15.3,
    "memory_usage": 256
  }
]
```

## 🖼️ 스크린샷
