# Week 4 — Postgres + ORM + Migration

## 🎯 목표
PostgreSQL을 Compose에 추가하고, ORM(SQLAlchemy)과 Alembic으로 DB 기반 CRUD를 완성한다.

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
