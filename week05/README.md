# Week 5 — FastAPI 실전(운영 감각)

## 🎯 목표
미들웨어, 공통 로깅, 페이지네이션, 필터를 구현하여 운영 수준의 API를 만든다.

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
