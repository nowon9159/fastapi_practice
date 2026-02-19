# FastAPI Practice

FastAPI와 SQLAlchemy를 사용한 연습용 REST API 프로젝트입니다. SQLite를 DB로 사용하며, 기본적인 CRUD API를 제공합니다.

## 기술 스택

- **Python** 3.12+
- **FastAPI** - 웹 프레임워크
- **SQLAlchemy** 2.0 - ORM
- **Uvicorn** - ASGI 서버
- **SQLite** - 데이터베이스 (`app.db`)

## 설치 및 실행

### uv 사용 (권장)

```bash
# 의존성 설치
uv sync

# 서버 실행
uv run uvicorn main:app --reload
```

### pip 사용

```bash
# 가상환경 생성 및 활성화 후
pip install -r requirements.txt

# 서버 실행
uvicorn main:app --reload
```

서버 실행 후 다음 주소에서 확인할 수 있습니다.

- **API 문서 (Swagger):** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/` | 기본 인사 메시지 |
| GET | `/db/info` | DB 테이블 목록, `items` 컬럼 정보, 개수 조회 |
| POST | `/articles` | 글 생성 |
| GET | `/articles/{article_id}` | 글 단건 조회 |
| PUT | `/articles/{article_id}` | 글 수정 |
| DELETE | `/articles/{article_id}` | 글 삭제 |

## 프로젝트 구조

```
fastapi_practice/
├── main.py        # FastAPI 앱 및 라우트
├── database.py    # SQLAlchemy 엔진, 세션, Base, Item 모델
├── pyproject.toml # 프로젝트 설정 및 의존성 (uv)
├── requirements.txt
└── README.md
```

## DB 정보

- **위치:** 프로젝트 루트의 `app.db` (SQLite 파일)
- **테이블:** 앱 시작 시 `Base.metadata.create_all()`로 자동 생성
- **모델:** `database.py`에 `Item` 모델 정의 (`items` 테이블)

### 데이터베이스 테이블 내용 확인하는 법

**1. API로 확인 (서버 실행 중일 때)**

```bash
curl http://127.0.0.1:8000/db/info
```

응답에 테이블 목록(`tables`), `items` 테이블 컬럼 정보(`items_columns`), `items` 개수(`items_count`)가 포함됩니다.

**2. sqlite3 CLI로 확인**

macOS·Linux에는 보통 `sqlite3`가 포함되어 있습니다. 프로젝트 루트에서 실행하세요.

```bash
# DB 접속
sqlite3 app.db

# 접속 후 사용할 수 있는 명령어:
.tables                    # 테이블 목록 보기
.schema items              # items 테이블 스키마 보기
SELECT * FROM items;       # items 테이블 전체 데이터 조회
.quit                      # 종료
```

한 줄로 데이터만 보고 싶을 때:

```bash
sqlite3 app.db "SELECT * FROM items;"
```

## 라이선스

MIT
