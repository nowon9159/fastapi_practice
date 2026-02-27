# FastAPI Practice

FastAPI + 코딩테스트 연습용 레포입니다. 주차별 과제를 통해 한 개의 애플리케이션을 단계적으로 확장합니다.

---

## 📁 과정 구조 (디렉터리 안내)

- **`week00/`, `week01/`, …**  
  각 주차별 **README(과제 설명·학습 목표·진행 순서)** 만 있습니다.  
  여기에는 소스 코드를 두지 않습니다.

- **프로젝트 루트의 `app/`**  
  **모든 주차의 웹서비스 과제 코드**를 이 한 디렉터리에 모아서 구현합니다.  
  - Week 0: 환경 세팅 후 `app/main.py` 등 뼈대 생성  
  - Week 1: `app/` 에 메모리 CRUD 추가  
  - Week 2: DI, 에러 처리 추가  
  - … 이후 주차마다 같은 `app/` 을 확장  

- **테스트, 설정, Docker 등**  
  `tests/`, `pyproject.toml`, `docker-compose.yml` 등은 **프로젝트 루트**에 두고, 위 `app/` 과 함께 하나의 프로젝트로 관리합니다.

- **코테 과제 풀이**  
  각 주차 코테(알고리즘) 과제 풀이는 **프로젝트 루트의 `coding-test/weekNN/`** 에 둡니다.  
  예: Week 1 → `coding-test/week01/`, Week 2 → `coding-test/week02/`.  
  풀이 코드(`.py`)와 접근법·복잡도 정리(README 또는 노트)를 같은 폴더에 넣으면 됩니다.  
  자세한 제출 방법은 각 주차 README의 **「📤 코테 과제 제출 방법」** 을 참고하세요.

정리하면, **과제 설명은 각 주차 폴더(week00, week01, …)의 README만 보고, 실제 구현은 루트의 `app/`(와 루트 설정) 하나에서 진행**하면 됩니다.

---

## 🗓 주차별 요약

| 주차 | 폴더 | 내용 |
|------|------|------|
| 0 | [week00/](week00/README.md) | 환경 세팅, uv/pytest/ruff, Hello FastAPI, Docker Compose |
| 1 | [week01/](week01/README.md) | Python 기초 1 + 메모리 CRUD (catalog-service) |
| 2 | [week02/](week02/README.md) | Python 기초 2 + FastAPI DI/에러 처리 |
| 3 | [week03/](week03/README.md) | 알고리즘 복잡도 + SQL 기초 |
| 4 | [week04/](week04/README.md) | Postgres + ORM + Migration |
| 5 | [week05/](week05/README.md) | 미들웨어, 로깅, 페이지네이션, 필터 |
| 6 | [week06/](week06/README.md) | Auth(JWT) + 보호 라우트 |
| 7 | [week07/](week07/README.md) | 서비스 분리 + API 계약 |
| 8 | [week08/](week08/README.md) | Compose 고도화, Makefile |
| 9 | [week09/](week09/README.md) | Unit/Integration 테스트 |
| 10 | [week10/](week10/README.md) | E2E + 문서화, 미니 프로젝트 완성 |

각 주차의 **구체적인 목표, 진행 순서, 제출 체크리스트**는 해당 폴더의 **README**를 읽으면 됩니다.
