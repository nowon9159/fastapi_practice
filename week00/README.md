# Week 0 — 환경 세팅 + 레포 표준화

## 🎯 목표

개발 환경을 세팅하고, 프로젝트의 뼈대(패키지 관리 + 품질 도구 + Compose)를 완성한다.  
이번 주가 끝나면 “어디에 코드를 두고, 어떻게 실행·테스트·컨테이너로 띄우는지”가 한 번에 정리된 상태가 된다.

---

## ✅ 이번 주를 마치면 얻는 것

- **uv**: 의존성 설치·가상환경·Python 버전을 한 곳(`pyproject.toml` + `uv.lock`)에서 관리할 수 있다.
- **FastAPI**: `app/main.py` 하나로 서버를 띄우고, `GET /`, `GET /health` 같은 엔드포인트를 만든 경험.
- **pytest**: 엔드포인트를 “코드로” 호출해서 기대값과 비교하는 테스트를 한 번 작성해 본다.
- **ruff**: 포맷/린트로 코드 스타일을 통일하고, 실수 가능성을 줄이는 기초.
- **pre-commit**: 커밋 전에 자동으로 ruff·테스트 등을 돌려서, **린트/포맷/테스트에 실패하는 코드**(“깨진 코드”)가 저장소에 들어가는 것을 막는 흐름을 경험한다.
- **Docker Compose**: 앱을 컨테이너로 빌드하고, 한 번에 기동할 수 있는 골격.

---

## 📁 코드 위치

- **프로젝트 루트**에 `pyproject.toml`, `docker-compose.yml`, `Dockerfile`, `tests/` 를 둔다.
- **앱 코드**는 루트의 `app/` (예: `app/main.py`)에 둔다.  
- `week00/` 폴더에는 이 README만 두고, 실제 소스는 루트에만 둔다.  
- 전체 구조는 [루트 README](../README.md)의 “과정 구조”를 참고한다.

---

## 📋 진행 순서

1. **uv 설치 및 프로젝트 초기화**  
   uv 설치 → 프로젝트 루트에서 `uv init` → Python 3.12 고정 → FastAPI·uvicorn 추가.  
   개발 의존성(pytest, ruff, pre-commit, httpx)까지 추가하고, `pyproject.toml`에 ruff/pytest 설정을 넣는다.

2. **FastAPI 앱 뼈대**  
   `app/main.py`를 만들고 `GET /`, `GET /health` 를 구현.  
   로컬에서 `uv run uvicorn app.main:app --reload` 로 동작 확인.

3. **테스트 작성**  
   `tests/test_core.py`에서 `/`와 `/health`를 호출해 응답 내용·상태 코드를 검증.  
   `uv run pytest -v` 로 통과 확인.

4. **Docker 골격**  
   `Dockerfile`(앱 이미지 빌드), `docker-compose.yml`(단일 서비스) 작성 후  
   `docker compose up -d --build` 로 기동까지 확인.

5. **(선택) pre-commit 설치**  
   `pre-commit install` 후 커밋 시 자동으로 ruff·테스트가 돌아가는지 확인.

---

## 📚 학습 키워드
- uv (패키지 매니저 + 가상환경 + Python 버전 관리)
- pytest 기초
- ruff (린터/포매터)
- pre-commit
- FastAPI 기본 구조
- Docker / Docker Compose 기초

---

## 🧑‍💻 코테
> 이번 주는 환경 세팅이 우선이므로 코테 과제 없음

---

## 🌐 웹서비스 과제

### 과제 1: uv 프로젝트 세팅 + 품질 도구
- [ ] uv 설치 (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- [ ] 프로젝트 초기화 (`uv init`)
- [ ] Python 버전 고정 (`uv python pin 3.12`)
- [ ] 의존성 추가 (`uv add fastapi uvicorn`)
- [ ] 개발 의존성 추가 (`uv add --dev pytest ruff pre-commit httpx`)
    - pytest 는 httpx 등 기타 애플리케이션 테스트 가능하도록 해주는거, 테스트 케이스 만들 때 유용해보임. (실제 운영환경에서 사용하는지는 의문임. 아마 CI/CD 내부적으로 테스트 케이스 만들어서 approval 하게 사용할수도 있을 것 같음)
    - ruff 는 lint 나 포맷 맞는지 확인하는 툴
    - pre-commit: 커밋 직전에 hook을 실행해, **린트/포맷/테스트가 실패하는 코드**(“깨진 코드”)가 커밋되지 않도록 막는 도구다.  
      즉, ruff 위반·테스트 실패 등이 있으면 커밋이 거부된다.
- [ ] `pyproject.toml` 에 ruff/pytest 설정 추가

### 과제 2: Hello FastAPI + /health
- [ ] FastAPI 앱 생성 (`app/main.py`)
- [ ] `GET /` → `{"message": "Hello, FastAPI!"}`
- [ ] `GET /health` → `{"status": "ok"}`
- [ ] pytest로 위 두 엔드포인트 테스트 작성
```
☁  week00 [master] ⚡  uv run pytest -v
========================================== test session starts ===========================================
platform darwin -- Python 3.12.12, pytest-9.0.2, pluggy-1.6.0 -- /Users/nowon9159/Repository/github/fastapi_practice/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/nowon9159/Repository/github/fastapi_practice
configfile: pyproject.toml
plugins: anyio-4.12.1
collected 2 items                                                                                        

tests/test_core.py::test_health PASSED                                                             [ 50%]
tests/test_core.py::test_root PASSED                                                               [100%]

=========================================== 2 passed in 0.07s ============================================
```


### 과제 3: Docker Compose 기본 골격
- [ ] `Dockerfile` 작성 (단일 서비스)
- [ ] `docker-compose.yml` 작성
- [ ] `docker compose up -d --build` 로 기동 확인

---

## ✅ 산출물 체크리스트
- [ ] uv 프로젝트 초기화 완료 (`pyproject.toml` + `uv.lock`)
- [ ] 모노레포 구조 생성 (`services/`, `libs/`, `infra/`)
- [ ] 품질 도구 세팅 완료 (ruff, pytest, pre-commit)
- [ ] `GET /health` 동작 확인
- [ ] Compose로 단일 서비스 기동 성공
- [ ] 테스트 1개 이상 통과 (`uv run pytest -q`)

---

## 🔗 참고
- [uv 공식 문서](https://docs.astral.sh/uv/)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [pytest 공식 문서](https://docs.pytest.org/)
- [ruff 공식 문서](https://docs.astral.sh/ruff/)
