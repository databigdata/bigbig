import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import io
import base64

import pickle

def averageChuchun(fnames, dic):
    result = dict()

    fnames = fnames.split(', ')

    for i in dic:
        for j in fnames:
            if j in i:
                result[i] = dic[i]

    num = len(fnames)

    total = [0 for n in range(num)]
    cnt = [0 for n in range(num)]
    average = [0 for n in range(num)]

    for name, chuchun in result.items():
        for nu in range(num):
            if fnames[nu] in name:
                cnt[nu] = cnt[nu] + 1
                total[nu] = total[nu] + chuchun['추천지수']
    diction = {}
    for nuu in range(num):
        average[nuu] = total[nuu] / cnt[nuu]
        average[nuu] = round(average[nuu], 2) # 정수로
        diction[fnames[nuu]] = average[nuu]
    return diction


def make_heatmap(str_fnames, dic1, dic2, dic3, dname1, dname2):
    import seaborn as sns

    # str_fnames string  '카레, 볶음밥'
    # dic1 dname1 수치
    # dic2 dname2 수치
    from query import temp
    fnames = str_fnames.split(', ')
    diction1 = averageChuchun(str_fnames, dic1)
    diction2 = averageChuchun(str_fnames, dic2)
    dic3 = dic3 #temp(dname1, dname2)
    diction3 = averageChuchun(str_fnames, dic3)

    avr = []
    for value in diction1.values():
        avr.append(value * 100)
    for value2 in diction2.values():
        avr.append(value2 * 100)
    for value3 in diction3.values():
        avr.append(value3 * 100)

    disease = []
    disease.append(dname1)
    disease.append(dname2)
    disease.append('합병')

    print('make_heatmap avr length : ', len(avr))
    print('make_heatmap fnames length : ', len(fnames))
    print(fnames)
    heat_dic = {}
    heat_dic['식품군'] = [fname for i in range(len(disease)) for fname in fnames]
    heat_dic['질병'] = [d for d in disease for j in range(len(fnames))]
    heat_dic['추천지수'] = avr
    print('make_heatmap 식품군 legnth : ', len(heat_dic['식품군']))
    print('make_heatmap 질명 length : ', len(heat_dic['질병']))
    heat_dic = pd.DataFrame(heat_dic)
    recipe = heat_dic.pivot("식품군", "질병", "추천지수")

    sns.reset_orig()
    # 폰트 추가
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    font = {
        'family': font_name,
        'size': 14
    }

    rc('font', **font)

    cmap = sns.diverging_palette(10, 220, as_cmap=True)
    ax = sns.heatmap(recipe, annot=True, linewidths=1, cmap=cmap, annot_kws={"size": 20})


    ax.get_figure().savefig(str_fnames + ".png")

    return ax


def bar(fnames, dic):
    import seaborn as sns

    print('bar : ', fnames, dic)
    result_dic = averageChuchun(fnames, dic)

    # 폰트 추가
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    nameL = []
    meanL = []

    for i, j in result_dic.items():
        nameL.append(i)
        meanL.append(j)

    # result = sns.barplot(x=nameL, y=meanL, palette="rocket")

    result = sns.barplot(x=nameL, y=meanL, palette="pastel")
    for i in range(len(nameL)):
        plt.text(x=i, y=meanL[i] / 2, s=meanL[i], size=20, ha='center', va='bottom')


    img = io.BytesIO()

    fig = result.get_figure()
    fig.savefig(img, format='png')

    return base64.b64encode(img.getvalue()).decode()



# tempdic=temp(dname1,dname2)

def make_boxplot(key, tempdic): # key는 음식명, tempdic은 질병 두개 수치
    import seaborn as sns
    x=['권장률','위험률','추천지수']
    y=[tempdic[key]['권장률']*100,tempdic[key]['위험률']*100,tempdic[key]['추천지수']*100]
    result=sns.barplot(x=x, y=y, palette="pastel")
    for i in range(len(x)):
        plt.text(x = i , y = y[i]/2, s = round(y[i],0), size = 20, ha='center', va='bottom')
    return result