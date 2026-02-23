# Week 0 — 환경 세팅 + 레포 표준화

## 🎯 목표
개발 환경을 세팅하고, 프로젝트의 뼈대(모노레포 + 품질 도구 + Compose)를 완성한다.

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
    - pre-commit 은 실제 커밋하기 전에 자동으로 hook 실행해서 깨진 코드가 있는지 확인하는 툴이라고 함.
        - 여기서 이야기하는 깨진 코드가 뭔지 모르겠음.
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
