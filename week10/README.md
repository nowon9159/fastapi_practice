# Week 10 — 미니 프로젝트 완성(E2E)

## 🎯 목표
E2E 플로우(가입→로그인→아이템 생성→조회)를 완성하고, 문서화하여 "완주 가능한 로컬 MSA 데모"를 만든다.

---

## 📚 학습 키워드
- E2E (End-to-End) 테스트
- API 플로우 설계
- 문서화 (README, 아키텍처 다이어그램)
- 트러블슈팅 기록
- 전체 복습

---

## 🧑‍💻 코테 과제

### 전체 복습 + 정리
- [ ] Week 1~9 풀이 노트 재검토
- [ ] 유형별 "나만의 템플릿" 정리:
  - 투 포인터 / 슬라이딩 윈도우
  - BFS / DFS
  - 정렬 / 해시
  - 스택 / 큐
  - 그리디 / DP (기초)
- [ ] 약점 유형 마지막 보강 (2~3문제)

---

## 🌐 웹서비스 과제

### 과제 1: E2E 플로우 구현 및 검증
전체 플로우가 끊김 없이 동작하는지 확인:

```
1. POST /auth/signup     → 회원가입 (201)
2. POST /auth/login      → 로그인, JWT 발급 (200)
3. GET  /users/me         → 내 정보 확인 (200, JWT 필수)
4. POST /items            → 아이템 생성 (201, JWT 필수)
5. GET  /items             → 아이템 목록 조회 (200)
6. GET  /items/{id}       → 아이템 상세 조회 (200)
```

- [ ] 위 플로우를 수동(curl/httpie)으로 1회 검증
- [ ] pytest로 E2E 테스트 작성 (signup → login → create item → list items)

### 과제 2: 문서화
- [ ] README.md 최종 정리:
  - 프로젝트 소개
  - 아키텍처 설명 (서비스 구성도)
  - 로컬 실행 방법 (`make up`)
  - API 엔드포인트 요약 표
  - 환경변수 목록
  - 트러블슈팅 FAQ
- [ ] 각 서비스 README에 해당 서비스 설명 추가

### 과제 3: 최종 점검
- [ ] `make up` → 전체 스택 기동
- [ ] `make test` → 모든 테스트 통과
- [ ] `make lint` → ruff 경고 0
- [ ] 모든 healthcheck 통과
- [ ] OpenAPI 문서 최신 상태 확인

---

## ✅ 최종 산출물 체크리스트

### 🏗️ 서비스
- [ ] auth-service: signup, login, JWT 발급
- [ ] user-service: 보호 라우트 (GET /users/me)
- [ ] catalog-service: CRUD + pagination + filter

### 🐳 인프라
- [ ] docker-compose.yml: 전체 서비스 + DB + healthcheck
- [ ] Makefile: up, down, test, lint, logs
- [ ] .env: 환경변수 관리

### 🧪 테스트
- [ ] unit 테스트
- [ ] integration 테스트
- [ ] E2E 테스트 (전체 플로우)

### 📝 문서
- [ ] README.md (실행 방법, 아키텍처, API 요약)
- [ ] API 계약 표
- [ ] 릴리즈 체크리스트

### 📖 코테
- [ ] 유형별 풀이 노트 정리 완료
- [ ] 나만의 템플릿 정리 완료

---

## 🎉 완주 축하!

10주 동안의 학습을 통해 아래 역량을 갖추게 됩니다:
- ✅ Python 기초 문법 + 타입 힌트
- ✅ 코테 기초 유형 (투포인터, BFS/DFS, 해시, 그리디 등)
- ✅ FastAPI CRUD + 인증/인가 (JWT)
- ✅ PostgreSQL + ORM + Migration
- ✅ Docker Compose 기반 로컬 MSA 운영
- ✅ 테스트 + 품질 도구 (pytest, ruff)
- ✅ API 계약 + 문서화 습관

---

## 🔗 참고
- [FastAPI 전체 튜토리얼](https://fastapi.tiangolo.com/tutorial/)
- [Docker Compose 공식 문서](https://docs.docker.com/compose/)
- [Real Python](https://realpython.com/)
