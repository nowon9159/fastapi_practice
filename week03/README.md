# Week 3 — 알고리즘 체력(복잡도) + SQL 기초 준비

## 🎯 목표
정렬/해시/슬라이딩 윈도우/이진 탐색을 연습하며 복잡도 분석 습관을 기르고, SQL 기초를 맛본다.

---

## 📚 학습 키워드
- 시간 복잡도: O(1), O(n), O(n log n), O(n²)
- 공간 복잡도
- 정렬 알고리즘 (built-in sort, key 활용)
- 해시맵 활용 패턴
- 슬라이딩 윈도우
- 이진 탐색 (bisect)
- SQL: SELECT, WHERE, JOIN, GROUP BY

---

## 🧑‍💻 코테 과제 (이번 주 집중!)

### 유형별 문제 (총 10문제 목표)

#### 정렬 (2~3문제)
- [ ] K번째 큰 수 찾기
- [ ] 문자열 정렬 (사전순, 길이순)
- [ ] 좌표 정렬 (다중 키)

#### 해시 (2~3문제)
- [ ] 두 수의 합 (해시맵)
- [ ] 아나그램 그룹핑
- [ ] 완주하지 못한 선수

#### 슬라이딩 윈도우 (2문제)
- [ ] 길이 K인 부분 배열의 최대 합
- [ ] 중복 없는 가장 긴 부분 문자열

#### 이진 탐색 (2문제)
- [ ] 정렬된 배열에서 target 찾기
- [ ] 상한/하한 (bisect_left, bisect_right)

> ⚠️ 각 문제마다 반드시 기록:
> 1. 접근법 (핵심 아이디어 1~2줄)
> 2. 시간/공간 복잡도
> 3. 실수했던 점 / 엣지케이스

---

## 🌐 웹서비스 과제

### 과제: SQL 기초 맛보기
- [ ] PostgreSQL 로컬 or Docker로 띄우기
- [ ] 테이블 생성 (items 테이블)
- [ ] 기본 쿼리 연습:
  - `SELECT * FROM items`
  - `WHERE price > 100`
  - `ORDER BY name`
  - `JOIN` 맛보기 (categories 테이블)
- [ ] 다음 주(Week 4) ORM 도입을 위한 준비

---

## ✅ 산출물 체크리스트
- [ ] 코테 문제 풀이 노트 10개 (접근/복잡도/실수 기록)
- [ ] SQL 기본 쿼리 연습 완료
- [ ] 복잡도 분석이 자연스럽게 되는 수준 도달

---

## 🔗 참고
- [Python Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
- [bisect 모듈](https://docs.python.org/3/library/bisect.html)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
