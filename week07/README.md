# Week 7 — 서비스 분리 + API 계약(Contract)

## 🎯 목표

서비스 간 **API 계약**(req/res 모델, 에러 규칙, 상태코드)을 통일하고, OpenAPI 문서 기준으로 정리한다.  
여러 서비스가 같은 “에러 형식·응답 형식”을 쓰도록 해, 클라이언트·서비스 간 호출이 예측 가능해지게 한다.

---

## ✅ 이번 주를 마치면 얻는 것

- **API 계약**: 공통 `ErrorResponse`, `SuccessResponse`로 모든 서비스의 응답 형식을 맞추는 방법.
- **상태 코드 규칙**: 각 엔드포인트별 성공/실패 코드를 문서화하고, README·Swagger에 반영.
- **OpenAPI 정리**: `/docs`의 스키마·설명을 정비해 “문서 = 계약”으로 쓰는 습관.
- **Auth 토큰 검증**: user-service에서 auth-service의 JWT를 검증하는 흐름을 한 가지로 확정.

---

## 📁 코드 위치

- **공통 스키마**: 루트의 `libs/common/`(또는 `app/common/`)에 공통 모델 정의. 각 서비스는 `app/` 내 해당 라우트에서 이 스키마 사용.
- `week07/` 폴더에는 이 README만 둔다. [루트 README](../README.md) 참고.

---

## 📋 진행 순서

1. **공통 스키마**: `libs/common/`에 ErrorResponse, SuccessResponse 정의 후, 모든 서비스에서 동일 사용.
2. **상태 코드 문서화**: 서비스별 엔드포인트·성공/에러 코드를 README 표로 정리.
3. **OpenAPI 정리**: response_model, status_code, description 점검.
4. **JWT 검증 흐름**: user-service에서 auth JWT 검증 방식 확정 및 구현.

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

**📤 제출**: 풀이 코드와 접근법·복잡도 정리는 **`coding-test/week07/`** 에 둡니다. (자세한 규칙은 [week01 README](week01/README.md)의 「📤 코테 과제 제출 방법」 참고.)

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
