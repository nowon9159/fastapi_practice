# Week 2 — Python 기초 2(예외/모듈/타이핑) + FastAPI DI/에러

## 🎯 목표
Python 예외 처리·모듈화·타입 힌트를 배우고, FastAPI의 의존성 주입(DI)과 공통 에러 처리를 익힌다.

---

## 📚 학습 키워드
- Python: try/except, 커스텀 예외, 모듈/패키지, 타입 힌트
- FastAPI: `Depends()`, 예외 핸들러, `HTTPException`
- 환경변수: `.env`, `pydantic-settings`
- 로깅: `logging` 모듈 기초

---

## 🧑‍💻 코테 과제

### 유형: 스택 / 큐
- [ ] 괄호 검사 (유효한 괄호 문자열 판별)
- [ ] 스택으로 문자열 뒤집기
- [ ] 큐를 이용한 프린터 우선순위 문제

> 💡 스택 = LIFO, 큐 = FIFO — 각각 언제 쓰는지 정리하기

---

## 🌐 웹서비스 과제

### 과제 1: 의존성 주입(DI) 기초
- [ ] `dependencies.py`에 공통 의존성 함수 작성
- [ ] 라우터에서 `Depends()`로 주입하여 사용
- [ ] 예시: 설정값 주입, 간단한 인증 시뮬레이션

### 과제 2: 공통 에러 처리
- [ ] 공통 에러 응답 스키마 정의
  ```python
  class ErrorResponse(BaseModel):
      detail: str
      error_code: str
  ```
- [ ] `@app.exception_handler`로 HTTPException 커스터마이징
- [ ] 404, 422 등 에러를 통일된 포맷으로 반환

### 과제 3: .env + 로깅
- [ ] `pydantic-settings`로 환경변수 관리
- [ ] `.env` 파일 생성 (APP_NAME, DEBUG 등)
- [ ] `logging` 모듈로 요청 로깅 추가

### Definition of Done
- DI로 설정/의존성 주입 동작
- 에러 응답 포맷 통일 완료
- .env 기반 설정 로딩
- 테스트: validation 에러 + 404 에러 케이스 추가

---

## ✅ 산출물 체크리스트
- [ ] `catalog-service` 에러 포맷 통일
- [ ] `Depends()` 활용 코드 작성
- [ ] .env + pydantic-settings 설정
- [ ] 테스트: validation/404 케이스 추가
- [ ] 코테 문제 풀이 기록

---

## 🔗 참고
- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
