# bigbig
/search2.html 에 접속해서 병명을 적은 후 폼 위에 선택사항 선택한 후 검색 ->
메뉴 클릭시 레시피 화면으로 넘어감 (일부는 오류 발생 - > 데이터 정제를 더 해서 db를 바꿔야함(정제는 해놓음 db만 바꾸면 되는데 미루고 있음 금방 함))
(이미지랑 조리순서 아직 안보여줌, db엔 있는데 다른거 먼저 하느라 아직 안함 -> 금방함)
권장/추천지수 (내림차순 정렬) 위험지수 (오름차순 정렬) 정렬 기능 추가
특정 음식이나, 특정 재료가 들어간 음식을 검색하는 기능을 추가
히트맵 이미지 그리고 표시하는 코드는 완성햇지만 아직 웹 연동 안함. (분업 결과를 아직 합치지 않음)
전체적으로 웹페이지를 다듬어야함. (일단 결과 확인만 하느라 예쁘지 않음)


해야할 일 (숫자는 우선 순위 아님)
1. 페이지네이션 설정 (완료)
2. 연관분석 지수로 추천메뉴 표시 (보여주는 것만 웹에 추가하면 끝)
3. 정제된 db로 교체 (교체만 하면 끝)
4. 히트맵 추가 (보여주는 것만 웹에 추가하면 끝)
5. 전체적으로 다듬기 

mongoDB에 데이터 import 해야함
recipeDB
disease.json -> disease
food.json -> food
recipe.json -> recipe
(프로젝트루트 폴더에 있음)
