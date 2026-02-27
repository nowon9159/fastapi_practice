# Week 5 — FastAPI 실전(운영 감각)

## 🎯 목표

미들웨어, 공통 로깅, 페이지네이션, 필터를 구현해 **운영에 가까운 API**를 만든다.  
요청 추적(request_id), 구조화된 로그, 목록 API의 limit/offset·필터를 경험한다.

---

## ✅ 이번 주를 마치면 얻는 것

- **미들웨어**: 요청마다 `X-Request-ID`(UUID) 부여, 응답 헤더·로그에 포함시켜 “한 요청”을 추적하는 방법.
- **로깅**: 요청/응답(메서드, 경로, 상태코드, 소요 시간)을 로그로 남기는 패턴.
- **페이지네이션**: `GET /items?limit=10&offset=0` 형태로 목록을 나누어 반환.
- **필터**: `min_price` 등 쿼리 파라미터로 조건을 걸어 조회. 응답에 `total`, `limit`, `offset` 포함.

---

## 📁 코드 위치

- **구현은 프로젝트 루트의 `app/`** 에서 진행. Week 4 DB CRUD에 미들웨어·로깅·pagination·필터를 추가한다.
- `week05/` 폴더에는 이 README만 둔다. [루트 README](../README.md) 참고.

---

## 📋 진행 순서

1. **미들웨어**: 요청 진입 시 `X-Request-ID` 생성, 응답 헤더에 붙이기. 로그에도 request_id 포함.
2. **요청/응답 로깅**: 메서드, 경로, 상태코드, duration_ms 등을 로그에 남기기. 에러 시 traceback 포함.
3. **Pagination**: `limit`, `offset` 쿼리 파라미터 처리, `PaginatedResponse(items, total, limit, offset)` 형태로 반환.
4. **필터**: `min_price` 등 최소 1개 쿼리 필터 구현.
5. **테스트**: pagination·필터 동작 테스트 추가.

---

## 📚 학습 키워드
- FastAPI 미들웨어 (Middleware)
- 요청 ID (X-Request-ID)
- 구조화된 로깅 (structured logging)
- 페이지네이션 (limit/offset)
- 쿼리 파라미터 필터링
- BFS / DFS 기초

---

## 🧑‍💻 코테 과제

### 유형: BFS / DFS 기초
- [ ] 2D 격자에서 섬 개수 세기 (DFS)
- [ ] 미로 탈출 최단 거리 (BFS)
- [ ] 그래프 탐색: 인접 리스트 순회

> 💡 BFS = 최단거리, DFS = 탐색/백트래킹 — 사용 기준 정리하기

**📤 제출**: 풀이 코드와 접근법·복잡도 정리는 **`coding-test/week05/`** 에 둡니다. (자세한 규칙은 [week01 README](week01/README.md)의 「📤 코테 과제 제출 방법」 참고.)

---

## 🌐 웹서비스 과제

### 과제 1: 미들웨어 + 요청 ID
- [ ] 미들웨어에서 `X-Request-ID` 생성 (UUID)
- [ ] 모든 응답 헤더에 `X-Request-ID` 포함
- [ ] 로그에 request_id 포함시키기

### 과제 2: 공통 로깅
- [ ] 요청/응답 로깅 미들웨어
- [ ] 로그 포맷: `[request_id] METHOD /path → status_code (duration_ms)`
- [ ] 에러 발생 시 traceback 로깅

### 과제 3: Pagination + Filter
- [ ] `GET /items?limit=10&offset=0` 페이지네이션
- [ ] `GET /items?min_price=100` 필터 1개 이상
- [ ] 응답에 총 개수 포함:
  ```python
  class PaginatedResponse(BaseModel):
      items: list[ItemResponse]
      total: int
      limit: int
      offset: int
  ```

### Definition of Done
- 미들웨어: 모든 요청에 X-Request-ID 부여
- 로깅: 요청/응답 로그 출력
- 페이지네이션: limit/offset 동작
- 필터: 최소 1개 쿼리 파라미터 필터
- 테스트: pagination 동작 테스트

---

## ✅ 산출물 체크리스트
- [ ] 미들웨어 + X-Request-ID 구현
- [ ] 요청/응답 로깅 동작
- [ ] pagination/필터 적용 + 테스트
- [ ] 코테 문제 풀이 기록

---

## 🔗 참고
- [FastAPI Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)
- [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
