from flask import Flask, render_template, request, session, make_response
from matplotlib import rc, font_manager
import io
import base64



app = Flask(__name__)

# TODO 메뉴 레시피 화면
@app.route('/recipe', methods=['get'])
def showRecipe():
    from query import getRecipe, index_dic
    from recommend import fin_recommend
    import pickle
    a = request.args
    name = a['value']
    print(name)
    q = getRecipe(name)

    ingredient = q['ingredient']
    description = q['description']
    img = q['img']

    a = request.cookies.get('a')
    data = a.split(', ')
    print('data len', len(data))
    if len(data) == 1:
        with open("pickles/" + str(index_dic[data[0]]) + ".pickle", 'rb') as f:
            dic = pickle.load(f)
    else :
        with open("pickles/" + str(index_dic[data[0]]) + ".pickle", 'rb') as f:
            dic = pickle.load(f)

    result = fin_recommend(dic, name)
    data = dict()
    print('result', result)
    for i in result:
        for j in i:
            data[j] = getRecipe(j)
    print(data)

    return render_template('single-recipe.html', menu=name, ingredient=ingredient, description = description, img = img, result = result, data=data)

@app.route('/')
def root():
    disease = {'후천성면역결핍증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022698',
               '후두암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022837',
               '화상식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022715',
               '호모시스틴뇨증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022779',
               '협심증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022787',
               '허혈성심장질환식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022838',
               '항문암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022807',
               '프로피온산혈증, 프로피온산증': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022841',
               '프라더 윌리 증후군식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022842',
               '폐렴식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022843',
               '폐경기 및 여성의 갱년기': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022844',
               '페닐케톤뇨증, PKU': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022845',
               '패혈증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022704',
               '파킨슨증후군식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022846',
               '크론병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022848',
               '콜레라식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022849',
               '췌장암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022850',
               '천식식단': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022851',
               '지방간식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022852',
               '제대혈조혈모세포식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022853',
               '전이성폐암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024105',
               '전이성간암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024107',
               '전립암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024106',
               '저혈압식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024108',
               '저혈당증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024111',
               '저퓨린식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022722',
               '저칼륨식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024109',
               '저신장증,왜소증,성장장애': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024110',
               '저마그네슘혈증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024112',
               '저나트륨혈증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024113',
               '장폐색식, 또는 장유착식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024114',
               '자궁내 성장지연식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024115',
               '자궁경부암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024116',
               '임신성고혈압식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024117',
               '임신성 당뇨식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024118',
               '유방암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024119',
               '윌슨병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024120',
               '위암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024121',
               '위식도역류질환식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024122',
               '위궤양식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024124',
               '요로결석식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024129',
               '열량조절식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000022776',
               '알콜성간질환식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024131',
               '알츠하이머식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024134',
               '아토피성 피부염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024135',
               '십이지장궤양식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024141',
               '심근경색식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024136',
               '신증후군식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024137',
               '식품 알레르기식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024138',
               '식중독식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024133',
               '식도정맥류식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024140',
               '식도염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024139',
               '식도암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024142',
               '소화불량식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024143',
               '셀리악병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024146',
               '섭식장애식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024144',
               '산모식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024145',
               '사구체신염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024147',
               '빈혈식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024148',
               '복수식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024149',
               '복막염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024150',
               '변비식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024151',
               '바이러스성 간염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024152',
               '말기신질환식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024153',
               '만성피로증후군식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024155',
               '만성폐쇄성폐질환식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024154',
               '만성신부전식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024157',
               '만성담낭염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024196',
               '만성 췌장염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024156',
               '덤핑증후군식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024158',
               '대장양성종양식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024161',
               '대장암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024159',
               '대사증후군식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024164',
               '대사성산증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024162',
               '당원병식/당원축적병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024160',
               '당뇨병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024163',
               '당뇨병성족부병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024167',
               '담낭암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024168',
               '단장증후군식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024166',
               '다발성골수종식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024165',
               '뇌졸중식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024176',
               '뇌경색식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024173',
               '노인식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024171',
               '급성췌장염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024174',
               '급성신부전식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024179',
               '급성골수성백혈병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024170',
               '급성/만성 위염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024175',
               '급만성 림프모구성백혈병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024178',
               '궤양성대장염식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024177',
               '구토식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024172',
               '구루병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024180',
               '골다공증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024181',
               '고혈압식 / 폐성 고혈압식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024182',
               '고칼슘혈증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024186',
               '고지혈증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024183',
               '고마그네슘혈증식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024184',
               '결핵식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024187',
               '갑상선암식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024188',
               '갑상선기능항진증': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024189',
               '갑상선기능저하증': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024190',
               '간이식후식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024191',
               '간성혼수식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024193',
               '간경화식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024192',
               '각기병식': 'http://www.amc.seoul.kr/asan/file/imageView.do?fileId=F000000024194'}
    nameList = list(disease.keys())
    nameList = sorted(nameList)
    return render_template('recipe-tag-index.html', disease=disease, nameList=nameList)

@app.route('/<path>')
def hello_world(path=None):
    if path =="/favicon.ico" or path == 'favicon.ico':
        return

    if path == 'recipe-tag-index.html':
        return root()

    if path:
        return render_template('{}'.format(path))
    else:
        return render_template('index.html')




@app.route('/find', methods=['POST'])
def find():

    return render_template('index.html')

# @app.route('/a/heat')
def getHeatmap(dname1, dname2, dic3, fnames):
    from heatmap import make_heatmap
    from query import query

    img = io.BytesIO()

    dic1 = query(dname1)
    dic2 = query(dname2)

    print('fnames', fnames)

    ax = make_heatmap(fnames, dic1, dic2, dic3, dname1, dname2)
    fig = ax.get_figure()
    fig.savefig(img, format='png')

    plot_url = base64.b64encode(img.getvalue()).decode()

    print(plot_url)
    img.close()
    del(img)
    del(fig)
    del(ax)
    return plot_url
    # return render_template('single-recipe2.html', name=plot_url)
#								<img src="data:image/jpeg;base64, {{ name }}" >




# TODO 추천지수 계산, 메뉴 리스트 출력
@app.route('/query', methods=['POST'])
def query():
    from query import query, temp, getRecommend, selectFood, selectIngre, getRecipe, getRecipeAll, getDisease
    from heatmap import bar
    try:
        a = request.form['search']
        print('type(a)', type(a))
        print('a', a)
        n = request.form['choice']
        print('n', n)
    except:
        print('e')
        # a = request.a
        a = request.cookies.get('a')
        n = request.cookies.get('choice')
        print('cookie a', a)
        print('cookie n', n)

    try:
        b = request.form['order']
        print(b)
        if b == 'recommend':
            flag = '권장률'
        elif b == 'caution':
            flag = '위험률'
        elif b == 'rc':
            flag = '추천지수'
    except:
        print('error')
        flag = '추천지수'

    try:
        foodName = request.form['food']
        print('foodName', foodName)
    except:
        try:
            foodName = request.cookies.get('foodName')
            print('cookie foodName', foodName)
        except:
            foodName = None

    try:
        insert = request.form['insert']
        print('insert', insert, type(insert))
    except:
        try:
            insert = request.cookies.get('insert')
            print('cookie insert', type(insert))
        except:
            insert = None

    try:
        remove = request.form['remove']
        print('remove', remove)
    except:
        try:
            remove = request.cookies.get('remove')
            print('cookie remove', remove)
        except:
            remove = None

    try:
        pageNum = request.form['pageNum']
        print('pageNum', pageNum)
    except:
        pageNum=1

    data = a.split(', ')
    print('data len', len(data))
    for i in data:
        print(i)




    try :
        if n == "1":  # 먹고 싶은 음식 있을 때
            if len(data) == 1: #질병이 하나 선택
                print('data length', len(data))
                q = query(data[0])
                recommend, caution = getRecommend(data[0])
                # print(q)

                img_url=""
                if foodName:
                    food = selectFood(foodName, q)
                    # print('food : ', food)
                    q = food
                    img_url = bar(foodName, q)
                    print('img_url1', img_url)



                disease=[]
                disease.append(getDisease(data[0])) # 질병정보 읽어오기
                print('disease : ', disease)




                if flag == '위험률':
                    recommend_rate = sorted(q, key=lambda k: q[k][flag])  # 추천지수 계산 오름차순
                else:
                    recommend_rate = sorted(q, key=lambda k: q[k][flag], reverse=True)  # 추천지수 계산 내림차순
                print('recommend_rate type', type(recommend_rate))
                print('recommend_rate', recommend_rate[0:10])

                recipeData = []
                for iter in recommend_rate[(int(pageNum) - 1) * 20: int(pageNum) * 20]:
                    print(str((int(pageNum) - 1) * 20), '~', str(int(pageNum) * 20))
                    recipeData.append(getRecipe(iter))

                resp = make_response(
                    render_template('index.html', dname=data[0], recommend=recommend, caution=caution,
                                    rate=recommend_rate,
                                    data=q, pageNum=pageNum, recipe=recipeData, img_url=img_url, disease = disease))
                resp.set_cookie('a', a)
                resp.set_cookie('choice', n)
                if foodName:
                    resp.set_cookie('foodName', foodName)
                return resp
            else:
                q = temp(data[0], data[1])
                recommend1, caution1 = getRecommend(data[0])
                recommend2, caution2 = getRecommend(data[1])

                img_url = ""
                if foodName:
                    food = selectFood(foodName, q)
                    # print('food : ', food)
                    q = food
                    img_url = getHeatmap(data[0], data[1], q, foodName)
                    print('img_url2', img_url)

                disease = []
                for name in data:
                    disease.append(getDisease(name))  # 질병정보 읽어오기
                print('disease : ', disease)



                # print(q)
                if flag == '위험률':
                    recommend_rate = sorted(q, key=lambda k: q[k][flag])
                else:
                    recommend_rate = sorted(q, key=lambda k: q[k][flag], reverse=True)
                print('recommend_rate type', type(recommend_rate))
                print('recommend_rate', recommend_rate[0:10])

                recipeData = []
                for iter in recommend_rate[(int(pageNum) - 1) * 20: int(pageNum) * 20]:
                    print(str((int(pageNum) - 1) * 20), '~', str(int(pageNum) * 20))
                    recipeData.append(getRecipe(iter))

                resp = make_response(
                    render_template('index.html', dname1=data[0], dname2=data[1], recommend1=recommend1,
                                    recommend2=recommend2, caution1=caution1, caution2=caution2,
                                    rate=recommend_rate, data=q, foodName=foodName, pageNum=pageNum, recipe=recipeData, img_url=img_url, disease=disease ))
                resp.set_cookie('a', a)
                resp.set_cookie('choice', n)
                if foodName:
                    resp.set_cookie('foodName', foodName)
                return resp
        else:  # 없을 때
            if len(data) == 1 :
                q = query(data[0])
                recommend, caution = getRecommend(data[0])
                # print(q)

                if insert and remove:
                    print('insert and remove')
                    temp = selectIngre(insert, remove, q)
                    if temp:
                        print('temp', temp)
                        q = temp
                elif insert:
                    print('insert')
                    temp = selectIngre(insert, "", q)
                    if temp:
                        print('temp', temp)
                        q = temp
                elif remove:
                    print('remove')
                    temp = selectIngre("", remove, q)
                    if temp:
                        print('temp', temp)
                        q = temp

                if flag == '위험률':
                    recommend_rate = sorted(q, key=lambda k: q[k][flag])  # 추천지수 계산 오름차순
                else:
                    recommend_rate = sorted(q, key=lambda k: q[k][flag], reverse=True)  # 추천지수 계산 내림차순
                print('recommend_rate type', type(recommend_rate))
                print('recommend_rate', recommend_rate[0:10])

                recipeData = []
                for iter in recommend_rate[(int(pageNum) - 1) * 20: int(pageNum) * 20]:
                    print(str((int(pageNum) - 1) * 20), '~', str(int(pageNum) * 20))
                    recipeData.append(getRecipe(iter))

                resp = make_response(
                    render_template('index2.html', dname=data[0], recommend=recommend, caution=caution,
                                    rate=recommend_rate,
                                    data=q, pageNum=pageNum, recipe=recipeData))
                resp.set_cookie('a', a)
                resp.set_cookie('choice', n)

                return resp
            else:
                q = temp(data[0], data[1])
                recommend1, caution1 = getRecommend(data[0])
                recommend2, caution2 = getRecommend(data[1])
                # print(q)
                print('sort start')
                if flag == '위험률':
                    recommend_rate = sorted(q, key=lambda k: q[k][flag])
                else:
                    recommend_rate = sorted(q, key=lambda k: q[k][flag], reverse=True)
                print('sort start')

                print('recommend_rate type', type(recommend_rate))
                print('recommend_rate', recommend_rate[0:10])

                recipeData = []
                for iter in recommend_rate[(int(pageNum) - 1) * 20: int(pageNum) * 20]:
                    print(str((int(pageNum) - 1) * 20), '~', str(int(pageNum) * 20))
                    recipeData.append(getRecipe(iter))


                resp = make_response(
                    render_template('index2.html', dname1=data[0], dname2=data[1], recommend1=recommend1,
                                    recommend2=recommend2, caution1=caution1, caution2=caution2,
                                    rate=recommend_rate, data=q, pageNum=pageNum, recipe=recipeData))
                resp.set_cookie('a', a)
                resp.set_cookie('choice', n)
                return resp
    except Exception as e :
        print(e)




if __name__ == '__main__':
    print('main')
    app.run()
