from sklearn.linear_model  import LinearRegression #重回帰分析
from sklearn.ensemble import RandomForestClassifier#ランダムフォレスト
from sklearn.metrics import  accuracy_score#スコア吐き出し
from sklearn.metrics import  classification_report
from sklearn.model_selection import KFold #交差検証
from sklearn.model_selection import GridSearchCV #最適パラメーターの算出
from sklearn.model_selection import cross_val_score #交差検証用のスコア排出
import numpy as np



class Machine_learning:

    def x_make(self, x):
        x = x.drop("米ドル/円（標準:10m）", axis=1)
        x = x.drop("ユーロ/円（標準:10m）", axis=1)
        x = x.drop("ポンド/円（標準:10m）", axis=1)
        x = x.drop("ユーロ/米ドル（標準:10m）", axis=1)
        x = x.drop("米ドル/スイスフラン（標準:10m）", axis=1)
        x = x.drop("米ドル/ポンド（標準:10m）", axis=1)
        x = x.drop("ユーロ/ポンド（標準:10m）", axis=1)
        x = x.drop("米ドル/円（標準:20m）", axis=1)
        x = x.drop("ユーロ/円（標準:20m）", axis=1)
        x = x.drop("ポンド/円（標準:20m）", axis=1)
        x = x.drop("ユーロ/米ドル（標準:20m）", axis=1)
        x = x.drop("米ドル/スイスフラン（標準:20m）", axis=1)
        x = x.drop("米ドル/ポンド（標準:20m）", axis=1)
        x = x.drop("ユーロ/ポンド（標準:20m）", axis=1)
        x = x.drop("米ドル/円（標準:30m）", axis=1)
        x = x.drop("ユーロ/円（標準:30m）", axis=1)
        x = x.drop("ポンド/円（標準:30m）", axis=1)
        x = x.drop("ユーロ/米ドル（標準:30m）", axis=1)
        x = x.drop("米ドル/スイスフラン（標準:30m）", axis=1)
        x = x.drop("米ドル/ポンド（標準:30m）", axis=1)
        x = x.drop("ユーロ/ポンド（標準:30m）", axis=1)
        return x

    def data_model_5analysis(self, df, fluctuation_list, rf_result):
        # 重回帰分析用のデータ形成
        usjp = [i for i in df["米ドル/円"]]
        y1_data = []
        for i in range(len(usjp)):
            if i > 44:
                y1_data.append(usjp[i])  # 15分後の価格を格納
        y_data = []
        for i in y1_data:
            y_data.append(i)
        x = df[["米ドル/円", "ユーロ/円", "ポンド/円", "ユーロ/米ドル", "米ドル/スイスフラン", "米ドル/ポンド", "ユーロ/ポンド", "最小二乗法"]]
        x1_data = x.drop(range(len(x) - 45, len(x)))
        x_data = []
        for i in range(len(x1_data)):
            xa = []
            for n in x1_data.iloc[i]:
                xa.append(n)
            x_data.append(xa)
        prediction_data = df[["米ドル/円", "ユーロ/円", "ポンド/円", "ユーロ/米ドル", "米ドル/スイスフラン", "米ドル/ポンド", "ユーロ/ポンド", "最小二乗法"]].tail(
            1)
        return x_data, y_data, prediction_data


    def analysis_fit(self, x, y, prediction_data):
        # 重回帰分析にて学習して予測
        lr = LinearRegression(normalize=True)
        lr.fit(x, y)
        determination = lr.score(x, y)  # 決定係数
        pre_y = lr.predict(prediction_data)
        return pre_y[0], determination


    def random_forest_lern(self, x, y):
        # ランダムフォレスト学習関数
        model_random = RandomForestClassifier(random_state=42, max_depth=20)
        model_random.fit(x, y)  # 学習
        return model_random


    def random_predict(self, model_random, data):
        # ランダムフォレスト推定関数
        y_pred = model_random.predict(data)  # 推定処理
        return y_pred

    def random_precision(self, y_pred, y_test):
        # ランダムフォレスト精度計算
        print("precisionが精度、recallが再現度、f1-scoreが精度と再現度の調和平均、supportが正解ラベルの数")
        print(classification_report(y_test, y_pred))
        print("正解率　＝　", accuracy_score(y_test, y_pred))


    def random_forest_datamake(self, df):
        # 15分後の分類分けのランダムフォレスト用のdataの加工関数
        d_adit = [i for i in df["米ドル/円"]]
        ud_down_list = []
        l = len(d_adit)
        for i in range(l):
            if i + 45 > l:
                break
            g = d_adit[i]  # その時の価格
            f = d_adit[i + 44]  # 20分後の価格
            if f > g:
                if f - g > 0.006:  # スプレット０.３銭以上上昇してたら
                    a = 2
                else:
                    a = 1  # 値上がりしていた場合
            elif f < g:
                if g - f > 0.006:
                    a = -2  # 値下がりしていた場合
                else:
                    a = -1
            elif f == g:
                a = 0
            ud_down_list.append(a)
        df = df.drop(range(len(df) - 44, len(df)))  # 15分後のdataに合わせて削ぎ落とし
        df["価格変動"] = ud_down_list
        y = df["価格変動"]
        x = df.drop("価格変動", axis=1)
        x = Machine_learning().x_make(x)
        if len(y) > 200:
            y = y.tail(200)
            x = x.tail(200)
        return x, y, df, ud_down_list


    def prediction_data(self, df):
        x = df.tail(1)
        x = Machine_learning().x_make(x)
        return x


    def cross_val(self, x, y, time):
        kf = KFold(n_splits=10, shuffle=True, random_state=42)  # 交差検証セット
        best_model, scores, x, y = Machine_learning().random_forest_grid_kf(kf, x, y, time)  # 交差検証も含めたグリットリサーチ関数
        best_model.fit(x, y)  # 最適モデルで学習
        averege_score = np.mean(scores)  # スコア平均
        return averege_score, best_model


    def random_forest_grid_kf(self, kf, x, y, time):
        # 交差検証も併せたグリットリサーチ分析
        # 最適モデル（best_model）と最適モデルで行った交差検証結果(scores)を吐き出す
        model = RandomForestClassifier(random_state=42)  # ランダムフォレストセット
        if time < 5:
            depth = [10, 20, 30]
        else:
            depth = [20, 30]
        parameter = {
            'criterion': ["gini", "entropy"],
            'max_depth': depth
        }  # グリットリサーチパラメーター
        grid_search = GridSearchCV(estimator=model, param_grid=parameter, cv=kf)  # グリットリサーチセット
        grid_search.fit(x, y)  # 最適パラメータ学習
        scores = cross_val_score(grid_search, x, y, cv=kf)  # 最適パラメータで交差検証
        # ↓最適パラメーター でモデル作成
        best_model = RandomForestClassifier(random_state=42, criterion=grid_search.best_params_['criterion'],
                                            max_depth=grid_search.best_params_['max_depth'])
        return best_model, scores, x, y


    # 未実装（異常検出）
    def mahalanobi(self, df):
        # マハラノビス距離
        max_row = 42
        target_column = 45
        row = []
        column = []
        ave = [0.0 for i in range(target_column)]
        diff = np.zeros((1, target_column))
        vcm = np.zeros((max_row, target_column, target_column))
        mahal = np.zeros(max_row)
        tmp = np.zeros(target_column)
        for i in range(max_row):
            row.append(list(df.ix[i]))  # 時間毎の価格リスト
        for i in range(target_column):
            column.append(list(df.ix[:, i]))  # カテゴリー毎の価格リスト
        for i in range(target_column):  # カテゴリー毎の平均
            ave[i] = np.average(column[i])
        row = np.array(row)
        ave = np.array(ave)
        for i in range(max_row):
            diff = (row[i] - ave)
            diff = np.array([diff])
            vcm[i] = (diff * np.swapaxes(diff, 0, 1)) / target_column
        for i in range(max_row):
            #vcm[i] = sc.linalg.pinv(vcm[i])
            vcm[i] = vcm[i].transpose()
            vcm[i] = np.identity(target_column)
            diff = (row[i] - ave)
            for j in range(target_column):
                tmp[j] = np.dot(diff, vcm[i][j])
            mahal[i] = np.dot(tmp, diff)
        mahal_avera = np.average(mahal)
        return