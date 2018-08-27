
def return_fin(filtered_foodL, food_name):
    # filtering.csv 파일 불러오기(이 파일은 모든 3만개 음식에 대한 음식명과 재료data)
    import pandas as pd
    aa = pd.read_csv('filtering.csv', encoding='utf-8')

    # 불러온 aa파일에 na값 정리하기
    aa.dropna(axis=0, inplace=True)

    # 불러온 aa파일중 병에서 필터링된 food만 불러오기
    aa = aa[aa.음식명.isin(filtered_foodL)]

    # 핑터링된 aa데이터셋을 onehot encoding 하기
    dum = pd.get_dummies(aa, columns=['재료'])

    # 음식명 리스트 만들기
    dum_food = dum[['음식명']]
    dum_food = dum_food.drop_duplicates()  # 좀있다가 concat할 데이터프레임

    food_name_L = []
    for i in range(len(dum_food)):
        food_name_L.append(dum_food.iloc[i][0])

    # df_real를 return 해주는 함수 만들기
    def num(i):
        cc = dum[dum['음식명'] == food_name_L[i]].iloc[:, 1:]

        cl = cc.iloc[0]
        for j in range(1, len(cc)):
            cl += cc.iloc[j]

        cl_df = pd.DataFrame(cl)
        cl_fin = cl_df.T
        name_fin = dum_food.iloc[i:i + 1, :]
        df_real = pd.concat([name_fin, cl_fin], axis=1)

        return df_real

    # df_base만들기
    df_base = num(0)

    for i in range(1, len(food_name_L)):
        df_base = pd.concat([df_base, num(i)], axis=0, ignore_index=True)

    # df_base의 인덱스값 없애기
    df_base.set_index('음식명', inplace=True)

    # df_base T하기
    df_T = df_base.T

    # 음식끼리 상관계수 계산하기
    df_cor = df_T.corr()

    # 해당음식의 추천지수 보여주기
    fin = df_cor[food_name]

    # 정렬
    fin_sorted = fin.sort_values(ascending=False)

    # index리스만들기
    rec_index_L = []
    for i in range(1, 13):
        rec_index_L.append(fin_sorted[i])

    # name리스트 만들기
    rec_name_L = []
    for i in range(1, 13):
        rec_name_L.append(fin_sorted.index[i])

    # 상위 12개만 추려서 dic만들기
    rec_dic = {a: b for a, b in zip(rec_name_L, rec_index_L)}

    return rec_dic


def fin_recommend(dic, q):
    list_dic = sorted(dic.items(), key=lambda dic: dic[1]['추천지수'], reverse=True)
    d=[]
    newlist_dic = []
    try:
        for t in list_dic:
            if t[1]['추천지수'] > 0.6:
                newlist_dic.append(t[0])

        fin = return_fin(newlist_dic, q)
        d = [{i: dic[i]} for i in fin]
    except Exception as e:
        print(e)

    return d
