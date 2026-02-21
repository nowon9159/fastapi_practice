# Week 9 — 테스트/품질(실무 수준)

## 🎯 목표
unit/integration 테스트를 구분하고, ruff + pytest를 "CI 흉내"로 고정하여 실무 수준의 품질 기반을 만든다.

---

## 📚 학습 키워드
- Unit Test vs Integration Test
- pytest: fixture, parametrize, conftest
- 테스트 DB (테스트용 격리 환경)
- ruff (린터/포매터) CI 적용
- mypy (선택: 정적 타입 검사)
- 릴리즈 체크리스트

---

## 🧑‍💻 코테 과제

### 약점 유형 집중 (개인화)
- [ ] 지금까지 가장 어려웠던 유형 3개 선택
- [ ] 각 유형별 문제 2~3개씩 추가 풀이
- [ ] 풀이 노트에 "왜 틀렸는지" 패턴 분석

> 💡 이 시점에서는 새로운 유형보다 **약점 보강**이 더 효과적!

---

## 🌐 웹서비스 과제

### 과제 1: Unit Test 정비
- [ ] service 레이어 단위 테스트 (DB 없이, mock 사용)
- [ ] Pydantic 모델 검증 테스트
- [ ] 순수 함수(유틸) 테스트

### 과제 2: Integration Test 정비
- [ ] API 엔드포인트 통합 테스트 (TestClient)
- [ ] DB 포함 테스트 (테스트용 DB or fixture로 격리)
- [ ] 인증 흐름 통합 테스트 (signup → login → 보호 라우트)

### 과제 3: 테스트 구조화
- [ ] `tests/unit/` — 단위 테스트
- [ ] `tests/integration/` — 통합 테스트
- [ ] `conftest.py`에 공통 fixture 정리
- [ ] `pytest.ini` or `pyproject.toml`에 마커 설정:
  ```toml
  [tool.pytest.ini_options]
  markers = [
      "unit: Unit tests",
      "integration: Integration tests",
  ]
  ```

### 과제 4: 품질 도구 CI 흉내
- [ ] ruff check + ruff format 자동 실행
- [ ] pytest 자동 실행
- [ ] (선택) mypy로 타입 검사
- [ ] `make lint`, `make test`, `make check` 명령 추가:
  ```makefile
  lint:
  	ruff check . --fix
  	ruff format .

  check: lint test
  ```

### 과제 5: 릴리즈 체크리스트 작성
- [ ] 배포 전 확인 사항 문서화:
  - 모든 테스트 통과
  - ruff 경고 0
  - 환경변수 확인
  - compose 기동 + healthcheck 통과
  - API 문서(OpenAPI) 최신 상태

---

## ✅ 산출물 체크리스트
- [ ] unit/integration 테스트 구분 완료
- [ ] ruff + pytest "CI 흉내" 고정
- [ ] 릴리즈 체크리스트 문서 작성
- [ ] 테스트/품질 규칙 고정
- [ ] 코테: 약점 유형 집중 풀이

---

## 🔗 참고
- [pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [ruff 공식 문서](https://docs.astral.sh/ruff/)
