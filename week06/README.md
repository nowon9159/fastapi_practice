# Week 6 — Auth 서비스(JWT) + 보호 라우트

## 🎯 목표

auth-service(회원가입/로그인/JWT)와 user-service(보호 라우트)를 만들어 **2개 서비스 + Compose** 기동을 달성한다.  
인증(누구인지)과 인가(무엇을 허용할지)를 JWT로 다루는 흐름을 경험한다.

---

## ✅ 이번 주를 마치면 얻는 것

- **인증 vs 인가**: 로그인(인증)과 “이 리소스 접근 허용 여부”(인가) 구분.
- **비밀번호**: 평문 저장 금지, bcrypt/passlib으로 해싱.
- **JWT**: access token 발급·검증, OAuth2PasswordBearer, 만료 시간 설정.
- **보호 라우트**: `Depends(get_current_user)`로 “로그인한 사용자만” 접근 가능한 엔드포인트 구현.
- **Compose**: auth + user + postgres 를 한 번에 띄우고, 서비스 간 통신·헬스체크 확인.

---

## 📁 코드 위치

- **구현은 프로젝트 루트의 `app/`** (또는 서비스별로 `app/auth/`, `app/user/` 등 분리해도 됨).  
  auth(회원가입·로그인·JWT), user(보호 라우트)를 같은 레포의 `app/` 안에서 구현.
- `docker-compose.yml`에 auth, user, postgres 서비스를 추가. `week06/` 폴더에는 이 README만 둔다. [루트 README](../README.md) 참고.

---

## 📋 진행 순서

1. **auth-service**: `POST /auth/signup`(비밀번호 해싱, 이메일 중복 409), `POST /auth/login`(비밀번호 검증, JWT 발급). SECRET_KEY·ALGORITHM·EXPIRE는 환경변수.
2. **user-service**: `GET /users/me`(JWT 필수). JWT 검증 실패 시 401. `Depends(get_current_user)` 패턴 적용.
3. **Compose**: auth + user + postgres, 네트워크·depends_on·헬스체크 설정.
4. **테스트**: 로그인 성공/실패, 보호 라우트 401 케이스.

---

## 📚 학습 키워드
- 인증(Authentication) vs 인가(Authorization)
- 비밀번호 해싱 (bcrypt / passlib)
- JWT (JSON Web Token): 구조, 발급, 검증
- FastAPI Security (`OAuth2PasswordBearer`)
- 보호 라우트 (Protected Route)
- 트리 자료구조

---

## 🧑‍💻 코테 과제

### 유형: 트리 기초
- [ ] 이진 트리 순회 (전위/중위/후위)
- [ ] 트리 최대 깊이 구하기
- [ ] 이진 탐색 트리(BST) 검증

> 💡 트리 = 재귀가 자연스러운 구조. 기저 조건을 항상 먼저!

**📤 제출**: 풀이 코드와 접근법·복잡도 정리는 **`coding-test/week06/`** 에 둡니다. (자세한 규칙은 [week01 README](week01/README.md)의 「📤 코테 과제 제출 방법」 참고.)

---

## 🌐 웹서비스 과제

### 과제 1: auth-service 구현
- [ ] `POST /auth/signup` — 회원가입
  - 비밀번호 해싱 (bcrypt)
  - 이메일 중복 체크 (409)
- [ ] `POST /auth/login` — 로그인
  - 비밀번호 검증
  - JWT 발급 (access token)
- [ ] JWT 설정은 환경변수 (SECRET_KEY, ALGORITHM, EXPIRE_MINUTES)

### 과제 2: user-service 보호 라우트
- [ ] `GET /users/me` — 현재 사용자 정보 (JWT 필수)
- [ ] JWT 검증 실패 시 401 반환
- [ ] `Depends(get_current_user)` 패턴 적용

### 과제 3: Compose 2개 서비스 기동
- [ ] `docker-compose.yml`에 auth + user + postgres
- [ ] 서비스 간 네트워크 통신 확인
- [ ] 헬스체크 + depends_on 설정

### Definition of Done
- auth: signup/login 동작, 비번 해싱, JWT 발급
- user: 보호 라우트 동작, 401 처리
- compose: 2개 서비스 + DB 기동 성공
- 테스트: 로그인 성공/실패, 보호 라우트 401

---

## ✅ 산출물 체크리스트
- [ ] auth-service: signup + login + JWT
- [ ] user-service: 보호 라우트 (GET /users/me)
- [ ] 비밀번호 해싱 (plaintext 절대 금지)
- [ ] JWT secret은 환경변수
- [ ] compose: auth + user + postgres 기동
- [ ] 테스트: 로그인 성공/실패, 401 케이스
- [ ] 코테 문제 풀이 기록

---

## ⚠️ 보안 주의사항
- 비밀번호는 **반드시 해싱** (bcrypt/argon2)
- JWT SECRET은 `.env`에만 저장
- 토큰 만료 시간 설정 필수
- 로그에 비밀번호/토큰 원문 출력 금지

---

## 🔗 참고
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [python-jose (JWT)](https://github.com/mpdavis/python-jose)
- [passlib (bcrypt)](https://passlib.readthedocs.io/)
