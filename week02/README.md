# Week 2 — Python 기초 2(예외/모듈/타이핑) + FastAPI DI/에러

## 🎯 목표

Python 예외 처리·모듈화·타입 힌트를 배우고, FastAPI의 **의존성 주입(DI)** 과 **공통 에러 처리**를 익힌다.  
API 전체에서 “설정값 주입”, “에러 응답 형식 통일”, “환경변수·로깅”을 한 번에 적용하는 방법을 경험한다.

---

## ✅ 이번 주를 마치면 얻는 것

- **Python**: try/except, 커스텀 예외, 모듈/패키지, 타입 힌트로 코드를 더 안전하고 읽기 쉽게 만드는 방법.
- **FastAPI DI**: `Depends()`로 “설정”, “DB 세션”, “인증 정보” 등을 라우트에 주입하는 패턴.
- **에러 처리**: 404·422 등을 `ErrorResponse` 같은 공통 스키마로 통일하고, `@app.exception_handler`로 한 곳에서 처리하는 방식.
- **환경·로깅**: `.env` + pydantic-settings로 설정 분리, `logging`으로 요청 추적 기초.

---

## 📁 코드 위치

- **구현은 프로젝트 루트의 `app/`** 에서 진행. Week 1에서 만든 catalog-service에 DI·에러·설정·로깅을 **추가**한다.  
- `week02/` 폴더에는 이 README만 둔다. [루트 README](../README.md) 참고.

---

## 📋 진행 순서

1. **의존성 주입**: `dependencies.py`에 “설정 주입”, “간단한 인증 시뮬레이션” 등 공통 함수를 만들고, 라우터에서 `Depends()`로 사용.
2. **공통 에러 스키마**: `ErrorResponse(detail, error_code)` 정의 후, `@app.exception_handler(HTTPException)`에서 이 형식으로 반환하도록 처리. 404·422가 같은 형태로 나오는지 확인.
3. **환경변수**: pydantic-settings로 `.env` 로드, `APP_NAME`, `DEBUG` 등 사용. `.env` 파일 생성.
4. **로깅**: `logging` 모듈로 요청(경로, 메서드 등) 로깅 추가.
5. **테스트**: validation 에러·404 에러 케이스를 추가하고, 응답 형식이 통일되었는지 검증.

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

**📤 제출**: 풀이 코드와 접근법·복잡도 정리는 **`coding-test/week02/`** 에 둡니다. (자세한 규칙은 [week01 README](week01/README.md)의 「📤 코테 과제 제출 방법」 참고.)

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
