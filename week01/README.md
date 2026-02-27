# Week 1 — Python 기초 1 + FastAPI CRUD(메모리)

## 🎯 목표

Python 기본 문법(문자열, 리스트, dict)을 익히고, FastAPI로 **메모리 기반** 아이템 CRUD API를 만든다.  
DB 없이 리스트/딕셔너리만으로 “만들기·목록·조회·수정·삭제”가 동작하는 상태까지 가져간다.

---

## ✅ 이번 주를 마치면 얻는 것

- **Python**: 문자열/리스트/dict로 데이터를 다루고, 반복문·조건문으로 CRUD 로직을 직접 짤 수 있다.
- **FastAPI**: 경로(path), 쿼리(query), 요청 body를 구분하고, GET/POST/PUT/DELETE로 REST 스타일 API를 하나 만든 경험.
- **Pydantic**: “들어오는 값 검증”과 “나가는 값 형태 고정”을 모델로 정의하는 방법.
- **실제 산출물**: `POST/GET/PUT/DELETE /items` 로 동작하는 catalog-service 형태의 API 한 개.

---

## 📁 코드 위치

- **구현은 프로젝트 루트의 `app/` 에서 진행**한다.  
- `week01/` 폴더에는 이 README만 두고, 소스는 루트의 `app/` 에만 둔다.  
- 자세한 구조는 [루트 README](../README.md)의 “과정 구조”를 참고한다.

---

## 📋 진행 순서 (이 순서대로 하면 수월함)

1. **Python 복습**  
   문자열, 리스트, dict, `for`/`if` 를 한 번씩 터치.  
   “아이템을 리스트에 추가하고, id로 찾고, 수정/삭제하는 함수”를 순수 Python으로 먼저 짜 보면 FastAPI와 연결하기 쉽다.

2. **Pydantic 모델 정하기**  
   `ItemCreate`(이름, 가격, 설명), `ItemResponse`(id 포함) 를 정의.  
   “클라이언트가 보내는 형식”과 “API가 돌려주는 형식”을 먼저 고정한다.

3. **메모리 저장소 만들기**  
   전역 리스트 또는 dict로 “아이템 목록”을 두고,  
   “다음 id 부여 → 추가 / id로 조회 / id로 수정 / id로 삭제” 함수를 만든다.  
   (이 단계는 아직 FastAPI 없이도 가능.)

4. **엔드포인트 5개 연결**  
   위 저장소를 사용해서 FastAPI 라우트 구현:  
   `POST /items` → 201 + 생성된 아이템,  
   `GET /items` → 200 + 전체 목록,  
   `GET /items/{item_id}` → 200 또는 404,  
   `PUT /items/{item_id}` → 200 또는 404,  
   `DELETE /items/{item_id}` → 204 또는 404.  
   요청 body는 `ItemCreate`, 응답은 `ItemResponse`(또는 목록)로 통일.

5. **테스트 작성**  
   “create 한 뒤 list 로 2개 이상 보인다” 수준의 테스트를 최소 2개 작성하고,  
   `uv run pytest`(또는 `pytest`)로 통과시키기.

---

## 📚 학습 키워드

- Python: 문자열, 리스트, 딕셔너리, 반복문, 조건문
- 투 포인터 기초
- FastAPI: 라우팅, Path/Query 파라미터
- Pydantic: Request/Response 모델
- HTTP 메서드: GET, POST, PUT, DELETE

---

## 🧑‍💻 코테 과제

### 유형: 문자열 / 리스트 / dict 빈도수

- [ ] 문자열 뒤집기 (투 포인터)
- [ ] 리스트에서 중복 제거
- [ ] 문자열 내 문자 빈도수 세기 (dict 활용)
- [ ] 투 포인터로 정렬된 배열에서 두 수의 합 찾기

> 💡 각 문제마다 **접근법 → 복잡도 → 엣지케이스** 정리 필수!

### 📤 코테 과제 제출 방법

- **제출 위치**: 프로젝트 루트에 `coding-test/week01/` 폴더를 만들고, 그 안에 다음을 둡니다.
  - **풀이 코드**: 문제별로 `.py` 파일 (예: `01_reverse_string.py`, `02_two_sum.py`)  
  - **풀이 노트**: 접근법·시간/공간 복잡도·엣지케이스를 정리한 `README.md` 또는 `notes.md`
- **파일/폴더명**: 자유. 문제 번호·이름으로 구분만 되면 됩니다.
- **제출 시점**: 해당 주차 산출물 체크리스트에 “코테 문제 풀이 기록”이 있으므로, 주차 마무리 전에 `coding-test/week01/` 에 올려두면 됩니다.

---

## 🌐 웹서비스 과제

### 과제: catalog-service 메모리 CRUD

**무엇을 하나요?**  
아이템을 “메모리(리스트/딕셔너리)”에만 저장하는 CRUD API 5개를 만든다.  
DB나 파일은 사용하지 않는다.

**왜 하나요?**  
FastAPI 라우팅, Pydantic 검증, HTTP 상태 코드를 익히기 위함이다.  
다음 주차부터 DI·DB를 붙일 때 “저장소만 바꾸면 된다”는 걸 체감할 수 있다.

| 메서드 | 경로 | 설명 | 상태 코드 |
|--------|------|------|-----------|
| POST   | `/items`        | 아이템 생성 | 201 |
| GET    | `/items`        | 전체 목록 조회 | 200 |
| GET    | `/items/{item_id}` | 단건 조회 | 200 / 404 |
| PUT    | `/items/{item_id}` | 수정 | 200 / 404 |
| DELETE | `/items/{item_id}` | 삭제 | 204 / 404 |

### Pydantic 모델 예시

```python
class ItemCreate(BaseModel):
    name: str
    price: float
    description: str | None = None

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None
```

- **어떻게 하나요?**  
  - `app/main.py`(또는 `app/routers/items.py`)에 위 5개 라우트를 추가.  
  - 내부에서는 “다음 id”를 관리하는 변수와 “아이템 목록” 리스트/딕셔너리를 두고,  
    생성 시 id 부여 후 목록에 추가, 조회/수정/삭제는 id로 찾아서 처리.

### Definition of Done

- [ ] 엔드포인트 5개 모두 동작 (curl 또는 Swagger로 확인)
- [ ] Pydantic으로 입력 검증 (잘못된 타입 시 422 등)
- [ ] 메모리(dict/list) 기반 저장
- [ ] 테스트: create + list 최소 2개 통과

---

## ✅ 산출물 체크리스트

- [ ] `app/` 에 catalog-service 메모리 CRUD 완성
- [ ] Pydantic req/res 모델 정의
- [ ] 테스트 2개 이상 통과
- [ ] 코테 문제 풀이 기록 (접근/복잡도)

---

## 🔗 참고

- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Pydantic Models](https://fastapi.tiangolo.com/tutorial/body/)
