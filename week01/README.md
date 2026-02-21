# Week 1 — Python 기초 1 + FastAPI CRUD(메모리)

## 🎯 목표
Python 기본 문법(문자열, 리스트, dict)을 익히고, FastAPI로 메모리 기반 CRUD API를 만든다.

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

---

## 🌐 웹서비스 과제

### 과제: catalog-service 메모리 CRUD
- [ ] `POST /items` → 아이템 생성 (201)
- [ ] `GET /items` → 전체 목록 조회 (200)
- [ ] `GET /items/{item_id}` → 단건 조회 (200 / 404)
- [ ] `PUT /items/{item_id}` → 수정 (200 / 404)
- [ ] `DELETE /items/{item_id}` → 삭제 (204 / 404)

### Pydantic 모델
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

### Definition of Done
- 엔드포인트 5개 모두 동작
- Pydantic으로 입력 검증
- 메모리(dict/list) 기반 저장
- 테스트: create + list 최소 2개

---

## ✅ 산출물 체크리스트
- [ ] `catalog-service` 메모리 CRUD 완성
- [ ] Pydantic req/res 모델 정의
- [ ] 테스트 2개 이상 통과
- [ ] 코테 문제 풀이 기록 (접근/복잡도)

---

## 🔗 참고
- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Pydantic Models](https://fastapi.tiangolo.com/tutorial/body/)
