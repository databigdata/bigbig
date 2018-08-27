import pymongo
import pickle
connection = pymongo.MongoClient("localhost", 27017)

index_dic={'후천성면역결핍증식': 0,
 '후두암식': 1,
 '화상식': 2,
 '협심증식': 3,
 '허혈성심장질환식': 4,
 '프라더 윌리 증후군식': 5,
 '폐렴식': 6,
 '폐경기 및 여성의 갱년기': 7,
 '페닐케톤뇨증, PKU': 8,
 '패혈증식': 9,
 '크론병식': 10,
 '콜레라식': 11,
 '췌장암식': 12,
 '지방간식': 13,
 '제대혈조혈모세포식': 14,
 '전이성간암식': 15,
 '전립암식': 16,
 '저혈압식': 17,
 '저혈당증식': 18,
 '저칼륨식': 19,
 '저마그네슘혈증식': 20,
 '저나트륨혈증식': 21,
 '장폐색식, 또는 장유착식': 22,
 '자궁내 성장지연식': 23,
 '자궁경부암식': 24,
 '임신성고혈압식': 25,
 '임신성 당뇨식': 26,
 '유방암식': 27,
 '윌슨병식': 28,
 '위암식': 29,
 '위식도역류질환식': 30,
 '위궤양식': 31,
 '열량조절식': 32,
 '알콜성간질환식': 33,
 '십이지장궤양식': 34,
 '심근경색식': 35,
 '신증후군식': 36,
 '식중독식': 37,
 '식도정맥류식': 38,
 '식도염식': 39,
 '식도암식': 40,
 '셀리악병식': 41,
 '섭식장애식': 42,
 '사구체신염식': 43,
 '빈혈식': 44,
 '복막염식': 45,
 '변비식': 46,
 '바이러스성 간염식': 47,
 '말기신질환식': 54,
 '만성신부전식': 53,
 '만성담낭염식': 50,
 '만성 췌장염식': 51,
 '덤핑증후군식': 52,
 '대장암식': 55,
 '대사증후군식': 56,
 '당원병식/당원축적병식': 57,
 '당뇨병식': 58,
 '담낭암식': 59,
 '단장증후군식': 60,
 '급성췌장염식': 61,
 '급성신부전식': 62,
 '구루병식': 63,
 '골다공증식': 64,
 '고혈압식 / 폐성 고혈압식': 65,
 '고지혈증식': 66,
 '갑상선암식': 67,
 '갑상선기능항진증': 68,
 '갑상선기능저하증': 69,
 '간이식후식': 70,
 '간성혼수식': 71,
 '간경화식': 72,
 '각기병식': 73}
print('query in')
def query(dname1):  # 질병 하나 계싼
    # print('q', dname1)
    # db = connection.recipeDB2
    # recipe = db.recipe
    # food = db.food
    # disease = db.disease
    #
    # foodDict = dict()
    # for i in food.find():
    #     foodDict[i['food']] = i['element']
    #
    # dic = dict()
    #
    # cur = recipe.find()  # 레시피만 가져오기
    # curdis1 = disease.find({'disease_name': {"$eq": dname1}})
    # recommend1 = []
    # bul1 = []
    #
    # # recommend1 = curdis1.next()['권장식품']
    # # recommend2 = curdis2.next()['권장식품']
    # for i in curdis1:
    #     recommend1.extend(i['권장식품'])
    #     bul1.extend(i['주의식품'])
    #
    # recommend = list(set(recommend1))
    # c = recommend.copy()
    # bul = list(set(bul1))
    #
    # recommend1 = recommend.copy()
    # bul1 = bul.copy()
    #
    # nl = []
    # cnt = 0
    # error = []
    # for recipe in cur:
    #     recipe_name = recipe['food_name']
    #     ho_count = 0
    #     bul_count = 0
    #     total_leng = len(recipe['ingredient'])
    #     for d in recipe['ingredient']:
    #         for ingredient in d:
    #             for i in recommend1:
    #                 try:
    #                     if ingredient in foodDict[i]:
    #                         ho_count = ho_count + 1
    #                         break
    #                 except:
    #                     # continue
    #                     if ingredient in i:
    #                         ho_count = ho_count + 1
    #                         break
    #             for j in bul1:
    #                 try:
    #                     if ingredient in foodDict[j]:
    #                         bul_count = bul_count + 1
    #                         break
    #                 except:
    #                     # continue
    #                     if ingredient in j:
    #                         bul_count = bul_count + 1
    #                         break
    #     try:
    #         p = ho_count / total_leng
    #         nl.append(p)
    #         q = bul_count / total_leng
    #         r = 1 - p - q
    #         #     print(count)
    #
    #         dic[recipe_name] = {'권장률': p, '위험률': q, '추천지수': p - q}
    #
    #         if p > 1:
    #             error.append(recipe_name)
    #             cnt = cnt + 1
    #     except:
    #         continue
    #         # print(recipe_name)
    print('query load')
    with open("pickles/" + str(index_dic[dname1]) + ".pickle", 'rb') as f:
        dic = pickle.load(f)
    print('query load end')
    return dic


def temp(dname1, dname2):  # 질병 두개 계싼
    db = connection.recipeDB2
    recipe = db.recipe
    food = db.food
    disease = db.disease

    foodDict = dict()
    for i in food.find():
        foodDict[i['food']] = i['element']

    dic = dict()

    cur = recipe.find()  # 레시피만 가져오기
    curdis1 = disease.find({'disease_name': {"$eq": dname1}})
    curdis2 = disease.find({'disease_name': {"$eq": dname2}})
    recommend1 = []
    recommend2 = []
    bul1 = []
    bul2 = []

    # recommend1 = curdis1.next()['권장식품']
    # recommend2 = curdis2.next()['권장식품']
    for i in curdis1:
        recommend1.extend(i['권장식품'])
        bul1.extend(i['주의식품'])
    for i in curdis2:
        recommend2.extend(i['권장식품'])
        bul2.extend(i['주의식품'])

    recommend = list(set(recommend1 + recommend2))
    c = recommend.copy()
    bul = list(set(bul1 + bul2))
    for i in c:
        if i in bul:
            recommend.remove(i)

    recommend1 = recommend.copy()
    bul1 = bul.copy()

    nl = []
    cnt = 0
    error = []
    for recipe in cur:
        recipe_name = recipe['food_name']
        ho_count = 0
        bul_count = 0
        total_leng = len(recipe['ingredient'])
        for d in recipe['ingredient']:
            for ingredient in d:
                for i in recommend1:
                    try:
                        if ingredient in foodDict[i]:
                            ho_count = ho_count + 1
                            break
                    except:
                        # continue
                        if ingredient in i:
                            ho_count = ho_count + 1
                            break
                for j in bul1:
                    try:
                        if ingredient in foodDict[j]:
                            bul_count = bul_count + 1
                            break
                    except:
                        # continue
                        if ingredient in j:
                            bul_count = bul_count + 1
                            break
        try:
            p = ho_count / total_leng
            nl.append(p)
            q = bul_count / total_leng
            r = 1 - p - q
            #     print(count)
            # dic[recipe_name] = {'권장률': p, '위험률': q, '추천지수': p - q}
            if p - q < 1:
                dic[recipe_name] = {'권장률': p, '위험률': q, '추천지수': p - q}

            if p > 1:
                error.append(recipe_name)
                cnt = cnt + 1
        except:
            continue
            # print(recipe_name)
    return dic
    # print(cnt)
    # print(dic['초간단 순대국 만들기 뭐야.. 이 맛은'])
    # print(sorted(nl))


def getRecommend(dname):  # 특정 메뉴의 권장/주의 식품 리턴
    db = connection.recipeDB2
    disease = db.disease
    d = disease.find({'disease_name': {"$eq": dname}}).next()
    return d['권장식품'], d['주의식품']



def getRecipe(fname):  # 특정 메뉴의 데이터를 읽어옴 single-recipe에서 레시피 보여줄 때 사용
    db = connection.recipeDB2
    recipe = db.recipe
    print(fname)

    data = recipe.find({'food_name': {'$eq': fname}})
    # print(data)
    print(data.count())
    data = data.next()
    print(data)
    return data


def selectFood(fnames, dic):
    result = dict()
    print('selectfnames', fnames, type(fnames))
    fnames = fnames.split(', ')
    print(type(fnames))

    for i in dic:
        for j in fnames:
            if j in i:
                # print('func', i)
                result[i] = dic[i]

    return result


def selectIngre(plus_ingredient, minus_ingredient, dic):
    db = connection.recipeDB2
    recipe = db.recipe
    food = db.food
    foodDict = dict()
    for i in food.find():
        foodDict[i['food']] = i['element']

    plus_ingredient = plus_ingredient.split(", ")
    minus_ingredient = minus_ingredient.split(", ")


    menu = []
    for name in dic:
        menu.append(name)
    print(len(menu))

    recipeList = recipe.find()

    result = []
    foodDictList = list(foodDict.keys())  # 음식 종류 리스트(곡류...)

    flag = 1
    for plus in plus_ingredient:  # 들어가야할 재료가 있는 메뉴 추가
        flag = 0
        for recipe_item in recipeList:
            if plus in foodDictList:
                for foodDict_item in foodDict[plus]:
                    if foodDict_item in [list(k.keys())[0] for k in recipe_item['ingredient']]:  # 재료 리스트에 있는지 확인
                        result.append(recipe_item['food_name'])
                        break
            else:
                if plus in [list(k.keys())[0] for k in recipe_item['ingredient']]:
                    result.append(recipe_item['food_name'])

    if flag:  # 들어가야할 재료가 없는 경우 전체 메뉴를 result에 저장하고 밑에서 빼야할 재료가 있는 메뉴를 제거한다
        result = menu

    result = list(set(result))  # 중복 제거
    if '' in result:
        print('@')
    if not recipeList:
        print('find')
        recipeList = recipe.find()
    for minus in minus_ingredient:  # 빼야할 재료가 있는 메뉴 제거
        for recipe_item in recipeList:
            if minus in foodDictList:
                for foodDict_item in foodDict[minus]:
                    if foodDict_item in [list(k.keys())[0] for k in recipe_item['ingredient']]:
                        result.remove(recipe.item['food_name'])
                        break
            else:
                if minus in [list(k.keys())[0] for k in recipe_item['ingredient']]:  # 재료명으로 리스트를 만듦
                    result.remove(recipe_item['food_name'])
    try:
        result.remove('')
    except:
        pass

    newDict = dict()

    for i in result:
        newDict[i] = dic[i]


    return newDict


def getRecipeAll():
    db = connection.recipeDB2
    recipe = db.recipe
    v = 0
    temp = recipe.find()
    print('getRecipeAll : ', temp.count())
    result = []

    for i in temp:
        result.append(i)


    return result
