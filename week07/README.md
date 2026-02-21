# Week 7 — 서비스 분리 + API 계약(Contract)

## 🎯 목표
서비스 간 API 계약(req/res 모델, 에러 규칙, 상태코드)을 통일하고, OpenAPI 문서 기준으로 정리한다.

---

## 📚 학습 키워드
- API 계약 (Contract)
- OpenAPI / Swagger 문서
- 서비스 간 통신 패턴 (HTTP 동기 호출)
- 공통 에러/응답 스키마
- 그리디 알고리즘
- 힙 (heapq)

---

## 🧑‍💻 코테 과제

### 유형: 그리디 / 힙
- [ ] 회의실 배정 (그리디 - 종료 시간 정렬)
- [ ] 거스름돈 최소 동전 수 (그리디)
- [ ] 최솟값/최댓값 빠르게 구하기 (heapq)
- [ ] 상위 K개 빈도수 원소 (힙)

> 💡 그리디 = "지금 최선이 전체 최선" — 증명/반례 습관 기르기

---

## 🌐 웹서비스 과제

### 과제 1: 공통 스키마 통일
- [ ] `libs/common/`에 공통 모델 정의:
  ```python
  class ErrorResponse(BaseModel):
      detail: str
      error_code: str
      timestamp: datetime

  class SuccessResponse(BaseModel, Generic[T]):
      data: T
      message: str = "success"
  ```
- [ ] 모든 서비스에서 동일한 에러 포맷 사용

### 과제 2: 상태 코드 규칙 문서화
- [ ] 서비스별 엔드포인트 목록 정리
- [ ] 각 엔드포인트의 성공/실패 상태 코드 명시
- [ ] README에 API 계약 표 작성:
  | Service | Endpoint | Method | Success | Error Codes |
  |---------|----------|--------|---------|-------------|
  | auth | /auth/signup | POST | 201 | 409, 422 |
  | auth | /auth/login | POST | 200 | 401, 422 |
  | user | /users/me | GET | 200 | 401 |
  | catalog | /items | GET | 200 | 422 |

### 과제 3: OpenAPI 문서 정리
- [ ] FastAPI 자동 생성 `/docs` 확인
- [ ] response_model, status_code, description 정리
- [ ] 서비스별 Swagger 문서 스크린샷/확인

### 과제 4: Auth 토큰 검증 흐름 고정
- [ ] user-service에서 auth-service의 JWT를 검증하는 흐름 확정
- [ ] 공유 비밀키 방식 또는 내부 API 호출 방식 결정 및 구현

---

## ✅ 산출물 체크리스트
- [ ] 공통 에러/응답 스키마 통일
- [ ] README에 API 계약 표 작성
- [ ] OpenAPI 문서 정리
- [ ] auth 토큰 검증 흐름 고정
- [ ] 코테 문제 풀이 기록

---

## 🔗 참고
- [OpenAPI Specification](https://swagger.io/specification/)
- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Python heapq](https://docs.python.org/3/library/heapq.html)
