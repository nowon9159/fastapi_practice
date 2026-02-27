# Week 8 — Compose 운영 고도화(로컬 운영)

## 🎯 목표

Docker Compose를 **운영 수준**으로 고도화하고, Makefile로 명령을 단순화해 **전체 스택 로컬 기동**을 달성한다.  
기동 순서(healthcheck·depends_on), 데이터 영속화(volume), 일상 명령(make up / make test)을 정리한다.

---

## ✅ 이번 주를 마치면 얻는 것

- **Compose 고도화**: 모든 서비스 healthcheck, `depends_on` + service_healthy, named volume으로 DB 데이터 유지.
- **네트워크**: 커스텀 네트워크로 서비스 간 통신 구간 명확히 하기.
- **Makefile**: `make up`, `make down`, `make test`, `make logs` 등으로 로컬 운영을 한 줄 명령으로 정리.
- **(선택) 서비스별 DB 분리**: auth/catalog 등 서비스가 자기 DB만 쓰도록 구성하는 방법.

---

## 📁 코드 위치

- **Compose·Makefile**: 프로젝트 루트의 `docker-compose.yml`, `Makefile`.  
- **앱 코드**: 기존 `app/` 유지. 이번 주는 인프라·명령 정리에 집중.  
- `week08/` 폴더에는 이 README만 둔다. [루트 README](../README.md) 참고.

---

## 📋 진행 순서

1. **Compose**: 각 서비스에 healthcheck, depends_on(condition: service_healthy), named volume, 커스텀 네트워크 추가.
2. **Makefile**: up / down / test / logs / build 타깃 작성 후 동작 확인.
3. **검증**: `make up` → 전체 기동·헬스체크 통과, 재시작 후 DB 데이터 유지 확인.
4. **(선택) 서비스별 DB 분리** 구현.

---

## 📚 학습 키워드
- Docker Compose: healthcheck, depends_on, volumes, networks
- Makefile 기초
- 서비스별 DB 분리 (선택)
- DP (Dynamic Programming) 기초
- 약점 복습

---

## 🧑‍💻 코테 과제

### 유형: DP 기초 + 약점 복습
- [ ] 계단 오르기 (피보나치 변형)
- [ ] 0-1 배낭 문제 (기초)
- [ ] 최장 증가 부분 수열 (LIS) — 얕게

> 💡 DP = "큰 문제를 작은 문제로" + 메모이제이션
> 이번 주는 DP 깊게 파지 않고, 이전 주차 약점 복습에 더 집중!

### 약점 복습
- [ ] Week 3~7 중 틀렸던 문제 다시 풀기
- [ ] 복잡도 분석 재확인

**📤 제출**: 풀이 코드와 접근법·복잡도 정리는 **`coding-test/week08/`** 에 둡니다. (자세한 규칙은 [week01 README](week01/README.md)의 「📤 코테 과제 제출 방법」 참고.)

---

## 🌐 웹서비스 과제

### 과제 1: Compose 고도화
- [ ] 모든 서비스에 healthcheck 추가
- [ ] `depends_on` + condition: service_healthy 설정
- [ ] named volume으로 DB 데이터 영속화
- [ ] 커스텀 네트워크 구성:
  ```yaml
  networks:
    backend:
      driver: bridge
  ```

### 과제 2: (선택) 서비스별 DB 분리
- [ ] auth-service → auth_db
- [ ] catalog-service → catalog_db
- [ ] 각 서비스가 자기 DB만 접근하도록 분리

### 과제 3: Makefile 작성
- [ ] `make up` — 전체 스택 기동
- [ ] `make down` — 전체 스택 중지
- [ ] `make test` — 전체 테스트 실행
- [ ] `make logs` — 로그 확인
- [ ] `make build` — 빌드만
  ```makefile
  .PHONY: up down test logs build

  up:
  	docker compose up -d --build

  down:
  	docker compose down

  test:
  	docker compose exec app pytest -q

  logs:
  	docker compose logs -f

  build:
  	docker compose build
  ```

### Definition of Done
- 전체 스택(auth + user + catalog + postgres) 로컬 기동 성공
- healthcheck 모두 통과
- `make up` / `make test` 동작
- 서비스 재시작 후 DB 데이터 유지 (volume)

---

## ✅ 산출물 체크리스트
- [ ] Compose: healthcheck + depends_on + volume + network
- [ ] `make up`, `make test` 등 명령 동작
- [ ] 전체 스택 로컬 기동 성공
- [ ] (선택) 서비스별 DB 분리
- [ ] 코테: DP 기초 + 약점 복습

---

## 🔗 참고
- [Compose Healthcheck](https://docs.docker.com/compose/compose-file/05-services/#healthcheck)
- [Compose depends_on](https://docs.docker.com/compose/compose-file/05-services/#depends_on)
- [Makefile Tutorial](https://makefiletutorial.com/)
