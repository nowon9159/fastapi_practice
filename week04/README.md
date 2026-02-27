# Week 4 — Postgres + ORM + Migration

## 🎯 목표

PostgreSQL을 Compose에 추가하고, ORM(SQLAlchemy)과 Alembic으로 **DB 기반 CRUD**를 완성한다.  
지금까지의 “메모리 저장”을 “실제 DB 테이블”로 바꾸는 주차다.

---

## ✅ 이번 주를 마치면 얻는 것

- **Compose + Postgres**: `docker-compose.yml`에 DB 서비스를 넣고, 환경변수로 접속 정보를 관리하는 방법.
- **SQLAlchemy**: `models.py`에 모델 정의, 세션 팩토리, `Depends(get_db)`로 라우트에 세션 주입.
- **Alembic**: 스키마 변경을 “마이그레이션 파일”로 관리하고, `upgrade head`로 DB에 반영하는 흐름.
- **실제 산출물**: 메모리 대신 Postgres를 쓰는 catalog-service. 기존 엔드포인트 동작은 유지.

---

## 📁 코드 위치

- **구현은 프로젝트 루트의 `app/`** 에서 진행. `models.py`, `dependencies.py`(get_db), 서비스/라우트에서 DB 쿼리로 전환.
- `docker-compose.yml`, `.env`는 루트에 둔다. `week04/` 폴더에는 이 README만 둔다. [루트 README](../README.md) 참고.

---

## 📋 진행 순서

1. **Compose에 Postgres 추가**: `docker-compose.yml`에 postgres 서비스, 환경변수, 헬스체크.
2. **SQLAlchemy 모델·세션**: `models.py`에 Item 등 모델 정의, `dependencies.py`에 `get_db`, 라우트에서 `Depends(get_db)` 사용.
3. **Alembic**: `alembic init` → 초기 마이그레이션 생성 → `alembic upgrade head` 적용.
4. **CRUD를 DB로 교체**: 기존 메모리 저장 로직을 DB 쿼리로 바꾸고, 엔드포인트 동작·테스트 확인.
5. **통합 테스트**: DB를 사용하는 테스트 최소 1개 추가.

---

## 📚 학습 키워드
- PostgreSQL + Docker Compose
- SQLAlchemy (ORM 기초)
- Alembic (DB 마이그레이션)
- FastAPI + DB 세션 관리 (`Depends`)
- DB 통합 테스트

---

## 🧑‍💻 코테 과제

### 유형: 연결 리스트 / 재귀 (얕게)
- [ ] 연결 리스트 뒤집기
- [ ] 재귀로 팩토리얼 / 피보나치
- [ ] 재귀 → 반복문 변환 연습

> 💡 재귀의 기저 조건(base case)을 반드시 먼저 정의하기

**📤 제출**: 풀이 코드와 접근법·복잡도 정리는 **`coding-test/week04/`** 에 둡니다. (자세한 규칙은 [week01 README](week01/README.md)의 「📤 코테 과제 제출 방법」 참고.)

---

## 🌐 웹서비스 과제

### 과제 1: Compose에 PostgreSQL 추가
- [ ] `docker-compose.yml`에 postgres 서비스 추가
- [ ] 환경변수로 DB 접속 정보 관리 (`.env`)
- [ ] 헬스체크 설정
  ```yaml
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U $POSTGRES_USER"]
    interval: 5s
    retries: 5
  ```

### 과제 2: SQLAlchemy ORM 모델
- [ ] `models.py`에 Item 모델 정의
- [ ] DB 세션 팩토리 (`dependencies.py`)
- [ ] `Depends(get_db)`로 세션 주입

### 과제 3: Alembic 마이그레이션
- [ ] `alembic init` 실행
- [ ] 초기 마이그레이션 생성 (`alembic revision --autogenerate`)
- [ ] 마이그레이션 적용 (`alembic upgrade head`)

### 과제 4: CRUD를 DB 기반으로 교체
- [ ] `service.py`에서 메모리 저장 → DB 쿼리로 변경
- [ ] 기존 엔드포인트 동작 유지 확인

### Definition of Done
- compose에 postgres 포함, 헬스체크 통과
- ORM 모델로 CRUD 동작
- Alembic 마이그레이션 적용 완료
- DB 통합 테스트 1개 이상

---

## ✅ 산출물 체크리스트
- [ ] `docker-compose.yml`에 postgres 서비스 추가
- [ ] SQLAlchemy 모델 + 세션 관리
- [ ] Alembic 마이그레이션 동작
- [ ] DB 기반 CRUD 테스트 1개 이상
- [ ] 코테 문제 풀이 기록

---

## 🔗 참고
- [SQLAlchemy 공식 문서](https://docs.sqlalchemy.org/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
