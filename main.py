
import time
from decimal import Decimal
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#独自モジュールのインポート
from FinanceModules import processing, machine_lerninig, scraping, technical_index, traid



def main():
    process = processing.Processing()
    machine = machine_lerninig.Machine_learning()
    ScrapingData =  scraping.ScrapingData
    technical = technical_index.Technical_indicator()
    traid = traid.Simulated_traid()


    potision = "put"
    learning_con = 0
    c = 0
    error_con = 0
    error_list = []
    error_time = []
    process_time1 = []
    process_time2 = []
    divi_list = []
    pre_list = []
    pre_adit_list = []
    pre_real_list = []
    while True:
        x_coordinates = 0
        con = 0
        loop_con = 0
        principal = 100000
        score_list = []
        pre_result = []
        real_result = []
        determination_list = []
        usdjpy_data = []
        eurjpy_data = []
        gbpjpy_data = []
        eurusd_data = []
        usdchf_data = []
        gbpusd_data = []
        eurgbp_data = []
        five_seconds_usdjpy = []
        five_seconds_eurjpy = []
        five_seconds_gbpjpy = []
        five_seconds_eurusd = []
        five_seconds_usdchf = []
        five_seconds_gbpusd = []
        five_seconds_eurgbp = []

        usdjpy_sta10m_list = []
        eurjpy_sta10m_list = []
        gbpjpy_sta10m_list = []
        eurusd_sta10m_list = []
        usdchf_sta10m_list = []
        gbpusd_sta10m_list = []
        eurgbp_sta10m_list = []
        usdjpy_sta20m_list = []
        eurjpy_sta20m_list = []
        gbpjpy_sta20m_list = []
        eurusd_sta20m_list = []
        usdchf_sta20m_list = []
        gbpusd_sta20m_list = []
        eurgbp_sta20m_list = []
        usdjpy_sta30m_list = []
        eurjpy_sta30m_list = []
        gbpjpy_sta30m_list = []
        eurusd_sta30m_list = []
        usdchf_sta30m_list = []
        gbpusd_sta30m_list = []
        eurgbp_sta30m_list = []

        usdjpy_5ave_list = []
        usdjpy_15ave_list = []
        usdjpy_25ave_list = []
        usdjpy_48ave_list = []
        usdjpy_75ave_list = []
        usdjpy_135ave_list = []
        usdjpy_5devation_list = []
        usdjpy_25devation_list = []
        usdjpy_75devation_list = []
        usdjpy_30bollinger_list = []
        usdjpy_least_list = []

        usdjpy_5ave_list_n = []
        usdjpy_15ave_list_n = []
        usdjpy_25ave_list_n = []
        usdjpy_48ave_list_n = []
        usdjpy_75ave_list_n = []
        usdjpy_135ave_list_n = []
        if_url = 0

        for i in range(135):
            # 45分間データ取得
            time1 = time.time()
            x_coordinates += 1
            if_url = 0
            while if_url < 7:
                try:
                    if if_url == 0:
                        # 米国と日本の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX")
                        bid = data.exchange_usdjpy()
                        five_seconds_usdjpy = process.make_determinant(bid, five_seconds_usdjpy)
                        that_data = [x_coordinates, bid]
                        usdjpy_data = process.make_determinant(that_data, usdjpy_data)

                    elif if_url == 1:
                        # ユーロと日本の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=EURJPY=FX")
                        bid = data.exchange_eurjpy()
                        five_seconds_eurjpy = process.make_determinant(bid, five_seconds_eurjpy)
                        that_data = [x_coordinates, bid]
                        eurjpy_data = process.make_determinant(that_data, eurjpy_data)

                    elif if_url == 2:
                        # ポンドと日本の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=GBPJPY=FX")
                        bid = data.exchange_gbpjpy()
                        five_seconds_gbpjpy = process.make_determinant(bid, five_seconds_gbpjpy)
                        that_data = [x_coordinates, bid]
                        gbpjpy_data = process.make_determinant(that_data, gbpjpy_data)

                    elif if_url == 3:
                        # ユーロと米国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=EURUSD=FX")
                        bid = data.exchange_eurusd()
                        five_seconds_eurusd = process.make_determinant(bid, five_seconds_eurusd)
                        that_data = [x_coordinates, bid]
                        eurusd_data = process.make_determinant(that_data, eurusd_data)

                    elif if_url == 4:
                        # スイスと米国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=USDCHF=FX")
                        bid = data.exchange_usdchf()
                        five_seconds_usdchf = process.make_determinant(bid, five_seconds_usdchf)
                        that_data = [x_coordinates, bid]
                        usdchf_data = process.make_determinant(that_data, usdchf_data)

                    elif if_url == 5:
                        # 英国と米国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=GBPUSD=FX")
                        bid = data.exchange_gbpusd()
                        five_seconds_gbpusd = process.make_determinant(bid, five_seconds_gbpusd)
                        that_data = [x_coordinates, bid]
                        gbpusd_data = process.make_determinant(that_data, gbpusd_data)

                    elif if_url == 6:
                        # ユーロと英国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=EURGBP=FX")
                        bid = data.exchange_eurgbp()
                        five_seconds_eurgbp = process.make_determinant(bid, five_seconds_eurgbp)
                        that_data = [x_coordinates, bid]
                        eurgbp_data = process.make_determinant(that_data, eurgbp_data)

                    if_url = if_url + 1

                # 取得ができなかった場合
                except ValueError as e:
                    error_list.append(e)

            time2 = time.time()
            time3 = time2 - time1
            process_time1.append(round(time3, 2))
            t = "学習中...    ループ回数：" + str(i + 1) + "回目　　　" + str(round(time3, 2)) + "秒        "
            print("\r" + t, end="")
            #if time3 < 20:
                #time.sleep(20 - time3)

        while True:
            time1 = time.time()
            set_time1 = time.time()
            x_coordinates += 1
            if_url = 0
            while if_url < 7:
                try:
                    if if_url == 0:
                        # 米国と日本の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX")
                        usdjpy_bid = data.exchange_usdjpy()
                        five_seconds_usdjpy = process.make_determinant(usdjpy_bid, five_seconds_usdjpy)
                        that_data = [x_coordinates, usdjpy_bid]
                        usdjpy_data = process.make_determinant(that_data, usdjpy_data)

                    elif if_url == 1:
                        # ユーロと日本の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=EURJPY=FX")
                        eurjpy_bid = data.exchange_eurjpy()
                        five_seconds_eurjpy = process.make_determinant(eurjpy_bid, five_seconds_eurjpy)
                        that_data = [x_coordinates, eurjpy_bid]
                        eurjpy_data = process.make_determinant(that_data, eurjpy_data)

                    elif if_url == 2:
                        # ポンドと日本の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=GBPJPY=FX")
                        gbpjpy_bid = data.exchange_gbpjpy()
                        five_seconds_gbpjpy = process.make_determinant(gbpjpy_bid, five_seconds_gbpjpy)
                        that_data = [x_coordinates, gbpjpy_bid]
                        gbpjpy_data = process.make_determinant(that_data, gbpjpy_data)

                    elif if_url == 3:
                        # ユーロと米国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=EURUSD=FX")
                        eurusd_bid = data.exchange_eurusd()
                        five_seconds_eurusd = process.make_determinant(eurusd_bid, five_seconds_eurusd)
                        that_data = [x_coordinates, eurusd_bid]
                        eurusd_data = process.make_determinant(that_data, eurusd_data)

                    elif if_url == 4:
                        # スイスと米国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=USDCHF=FX")
                        usdchf_bid = data.exchange_usdchf()
                        five_seconds_usdchf = process.make_determinant(usdchf_bid, five_seconds_usdchf)
                        that_data = [x_coordinates, usdchf_bid]
                        usdchf_data = process.make_determinant(that_data, usdchf_data)

                    elif if_url == 5:
                        # 英国と米国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=GBPUSD=FX")
                        gbpusd_bid = data.exchange_gbpusd()
                        five_seconds_gbpusd = process.make_determinant(gbpusd_bid, five_seconds_gbpusd)
                        that_data = [x_coordinates, gbpusd_bid]
                        gbpusd_data = process.make_determinant(that_data, gbpusd_data)

                    elif if_url == 6:
                        # ユーロと英国の取得
                        data = ScrapingData("https://info.finance.yahoo.co.jp/fx/detail/?code=EURGBP=FX")
                        eurgbp_bid = data.exchange_eurgbp()
                        five_seconds_eurgbp = process.make_determinant(eurgbp_bid, five_seconds_eurgbp)
                        that_data = [x_coordinates, eurgbp_bid]
                        eurgbp_data = process.make_determinant(that_data, eurgbp_data)

                    if_url = if_url + 1

                except ValueError as e:
                    error_list.append(e)

            # 移動平均線の計算
            move_line_5 = technical.move_average_line(five_seconds_usdjpy, 5)
            move_line_15 = technical.move_average_line(five_seconds_usdjpy, 15)
            move_line_25 = technical.move_average_line(five_seconds_usdjpy, 25)
            move_line_48 = technical.move_average_line(five_seconds_usdjpy, 48)
            move_line_75 = technical.move_average_line(five_seconds_usdjpy, 75)
            move_line_135 = technical.move_average_line(five_seconds_usdjpy, 135)

            # 標準化した各為替価格
            usdjpy_sta10m_list = process.make_determinant(technical.standard_index(usdjpy_bid, five_seconds_usdjpy, 30),
                                                          usdjpy_sta10m_list)
            eurjpy_sta10m_list = process.make_determinant(technical.standard_index(eurjpy_bid, five_seconds_eurjpy, 30),
                                                          eurjpy_sta10m_list)
            gbpjpy_sta10m_list = process.make_determinant(technical.standard_index(gbpjpy_bid, five_seconds_gbpjpy, 30),
                                                          gbpjpy_sta10m_list)
            eurusd_sta10m_list = process.make_determinant(technical.standard_index(eurusd_bid, five_seconds_eurusd, 30),
                                                          eurusd_sta10m_list)
            usdchf_sta10m_list = process.make_determinant(technical.standard_index(usdchf_bid, five_seconds_usdchf, 30),
                                                          usdchf_sta10m_list)
            gbpusd_sta10m_list = process.make_determinant(technical.standard_index(gbpusd_bid, five_seconds_gbpusd, 30),
                                                          gbpusd_sta10m_list)
            eurgbp_sta10m_list = process.make_determinant(technical.standard_index(eurgbp_bid, five_seconds_eurgbp, 30),
                                                          eurgbp_sta10m_list)
            usdjpy_sta20m_list = process.make_determinant(technical.standard_index(usdjpy_bid, five_seconds_usdjpy, 60),
                                                          usdjpy_sta20m_list)
            eurjpy_sta20m_list = process.make_determinant(technical.standard_index(eurjpy_bid, five_seconds_eurjpy, 60),
                                                          eurjpy_sta20m_list)
            gbpjpy_sta20m_list = process.make_determinant(technical.standard_index(gbpjpy_bid, five_seconds_gbpjpy, 60),
                                                          gbpjpy_sta20m_list)
            eurusd_sta20m_list = process.make_determinant(technical.standard_index(eurusd_bid, five_seconds_eurusd, 60),
                                                          eurusd_sta20m_list)
            usdchf_sta20m_list = process.make_determinant(technical.standard_index(usdchf_bid, five_seconds_usdchf, 60),
                                                          usdchf_sta20m_list)
            gbpusd_sta20m_list = process.make_determinant(technical.standard_index(gbpusd_bid, five_seconds_gbpusd, 60),
                                                          gbpusd_sta20m_list)
            eurgbp_sta20m_list = process.make_determinant(technical.standard_index(eurgbp_bid, five_seconds_eurgbp, 60),
                                                          eurgbp_sta20m_list)
            usdjpy_sta30m_list = process.make_determinant(technical.standard_index(usdjpy_bid, five_seconds_usdjpy, 90),
                                                          usdjpy_sta30m_list)
            eurjpy_sta30m_list = process.make_determinant(technical.standard_index(eurjpy_bid, five_seconds_eurjpy, 90),
                                                          eurjpy_sta30m_list)
            gbpjpy_sta30m_list = process.make_determinant(technical.standard_index(gbpjpy_bid, five_seconds_gbpjpy, 90),
                                                          gbpjpy_sta30m_list)
            eurusd_sta30m_list = process.make_determinant(technical.standard_index(eurusd_bid, five_seconds_eurusd, 90),
                                                          eurusd_sta30m_list)
            usdchf_sta30m_list = process.make_determinant(technical.standard_index(usdchf_bid, five_seconds_usdchf, 90),
                                                          usdchf_sta30m_list)
            gbpusd_sta30m_list = process.make_determinant(technical.standard_index(gbpusd_bid, five_seconds_gbpusd, 90),
                                                          gbpusd_sta30m_list)
            eurgbp_sta30m_list = process.make_determinant(technical.standard_index(eurgbp_bid, five_seconds_eurgbp, 90),
                                                          eurgbp_sta30m_list)

            # 標準化補正なしのテクニカル指標
            usdjpy_5ave_list = process.make_determinant(move_line_5, usdjpy_5ave_list)  # 短期移動平均2分半
            usdjpy_15ave_list = process.make_determinant(move_line_15, usdjpy_15ave_list)  # 短中期移動平均5分
            usdjpy_25ave_list = process.make_determinant(move_line_25, usdjpy_25ave_list)  # 中期移動平均８.3分
            usdjpy_48ave_list = process.make_determinant(move_line_48, usdjpy_48ave_list)  # 中長期移動平均16分
            usdjpy_75ave_list = process.make_determinant(move_line_75, usdjpy_75ave_list)  # 長期移動平均２５分
            usdjpy_135ave_list = process.make_determinant(move_line_135, usdjpy_135ave_list)  # 超長期移動平均4５分
            usdjpy_5devation_list = process.make_determinant(
                technical.average_devation_rate(usdjpy_bid, five_seconds_usdjpy, 5), usdjpy_5devation_list)  # 短期移動平均乖離率
            usdjpy_25devation_list = process.make_determinant(
                technical.average_devation_rate(usdjpy_bid, five_seconds_usdjpy, 25), usdjpy_25devation_list)  # 中期移動平均乖離率
            usdjpy_75devation_list = process.make_determinant(
                technical.average_devation_rate(usdjpy_bid, five_seconds_usdjpy, 75),
                usdjpy_75devation_list)  # 長期移動平均乖離率
            usdjpy_30bollinger_list = process.make_determinant(technical.bollinger_band(five_seconds_usdjpy, 30),
                                                               usdjpy_30bollinger_list)  # ボリンジャーバンド
            array_data = np.array(usdjpy_data)
            a, b = technical.least_squares(array_data.T[1])
            usdjpy_least_list = process.make_determinant(a, usdjpy_least_list)  # 最小二乗法

            if x_coordinates > 145:
                # 標準化したテクニカル指標
                usdjpy_5ave_list_n = process.make_determinant(technical.standard_index(move_line_5, usdjpy_5ave_list, 10),
                                                              usdjpy_5ave_list_n)
                usdjpy_15ave_list_n = process.make_determinant(
                    technical.standard_index(move_line_15, usdjpy_15ave_list, 10), usdjpy_15ave_list_n)
                usdjpy_25ave_list_n = process.make_determinant(
                    technical.standard_index(move_line_25, usdjpy_25ave_list, 10), usdjpy_25ave_list_n)
                usdjpy_48ave_list_n = process.make_determinant(
                    technical.standard_index(move_line_48, usdjpy_48ave_list, 10), usdjpy_48ave_list_n)
                usdjpy_75ave_list_n = process.make_determinant(
                    technical.standard_index(move_line_75, usdjpy_75ave_list, 10), usdjpy_75ave_list_n)
                usdjpy_135ave_list_n = process.make_determinant(
                    technical.standard_index(move_line_135, usdjpy_135ave_list, 10), usdjpy_135ave_list_n)

                df = pd.DataFrame({
                    "米ドル/円": five_seconds_usdjpy[145:],
                    "ユーロ/円": five_seconds_eurjpy[145:],
                    "ポンド/円": five_seconds_gbpjpy[145:],
                    "ユーロ/米ドル": five_seconds_eurusd[145:],
                    "米ドル/スイスフラン": five_seconds_usdchf[145:],
                    "米ドル/ポンド": five_seconds_gbpusd[145:],
                    "ユーロ/ポンド": five_seconds_eurgbp[145:],
                    "米ドル/円（標準:10m）": usdjpy_sta10m_list[10:],
                    "ユーロ/円（標準:10m）": eurjpy_sta10m_list[10:],
                    "ポンド/円（標準:10m）": gbpjpy_sta10m_list[10:],
                    "ユーロ/米ドル（標準:10m）": eurusd_sta10m_list[10:],
                    "米ドル/スイスフラン（標準:10m）": usdchf_sta10m_list[10:],
                    "米ドル/ポンド（標準:10m）": gbpusd_sta10m_list[10:],
                    "ユーロ/ポンド（標準:10m）": eurgbp_sta10m_list[10:],
                    "米ドル/円（標準:20m）": usdjpy_sta20m_list[10:],
                    "ユーロ/円（標準:20m）": eurjpy_sta20m_list[10:],
                    "ポンド/円（標準:20m）": gbpjpy_sta20m_list[10:],
                    "ユーロ/米ドル（標準:20m）": eurusd_sta20m_list[10:],
                    "米ドル/スイスフラン（標準:20m）": usdchf_sta20m_list[10:],
                    "米ドル/ポンド（標準:20m）": gbpusd_sta20m_list[10:],
                    "ユーロ/ポンド（標準:20m）": eurgbp_sta20m_list[10:],
                    "米ドル/円（標準:30m）": usdjpy_sta30m_list[10:],
                    "ユーロ/円（標準:30m）": eurjpy_sta30m_list[10:],
                    "ポンド/円（標準:30m）": gbpjpy_sta30m_list[10:],
                    "ユーロ/米ドル（標準:30m）": eurusd_sta30m_list[10:],
                    "米ドル/スイスフラン（標準:30m）": usdchf_sta30m_list[10:],
                    "米ドル/ポンド（標準:30m）": gbpusd_sta30m_list[10:],
                    "ユーロ/ポンド（標準:30m）": eurgbp_sta30m_list[10:],
                    "短期移動平均": usdjpy_5ave_list[10:],
                    "短中期移動平均": usdjpy_15ave_list[10:],
                    "中期移動平均": usdjpy_25ave_list[10:],
                    "中長期移動平均": usdjpy_48ave_list[10:],
                    "長期移動平均": usdjpy_75ave_list[10:],
                    "超長期移動平均": usdjpy_135ave_list[10:],
                    "短期移動平均乖離率": usdjpy_5devation_list[10:],
                    "中期移動平均乖離率": usdjpy_25devation_list[10:],
                    "長期移動平均乖離率": usdjpy_75devation_list[10:],
                    "ボリンジャーバンド": usdjpy_30bollinger_list[10:],
                    "最小二乗法": usdjpy_least_list[10:]
                })
                set_time2 = time.time()
                if x_coordinates > 945:
                    df_sli = df.drop(c)
                    c += 1
                else:
                    df_sli = df
                if x_coordinates > 315:
                    set_time = set_time2 - set_time1
                    x, y, df_formation, ud_down_list = machine.random_forest_datamake(df_sli)  # x,yデータの作成
                    score, ramdom_model = machine.cross_val(x, y, set_time)  # 交差検証でモデルの正解率を算出
                    score_list.append(score)
                    # if score > 0.8: #交差検証の結果が80％以上の正答率だった場合計算処理
                    latest_data = machine.prediction_data(df_sli)
                    result = machine.random_predict(ramdom_model, latest_data)  # 現在値の１5分後のリスクを計算
                    if result == 2:
                        t2 = "up2  "
                    elif result == 1:
                        t2 = "up1  "
                    elif result == 0:
                        t2 = "not up,down"
                    elif result == -1:
                        t2 = "down1  "
                    elif result == -2:
                        t2 = "down2  "
                    an_x, an_y, pre_data = machine.data_model_5analysis(df_sli, ud_down_list, result)
                    pre_y, determination = machine.analysis_fit(an_x, an_y, pre_data)
                    determination_list.append(determination)
                    pre_result.append(result)
                    pre_list.append(pre_y)
                    if x_coordinates > 355:
                        real_result.append(result)
                        before_pre = pre_list[0 + (x_coordinates - 356)]
                        pre_divi = Decimal(pre_y) - Decimal(before_pre)
                        ratio = Decimal(pre_divi) / Decimal(before_pre)
                        rate = Decimal(usdjpy_bid) * ratio
                        pre_price = Decimal(usdjpy_bid) + rate
                        pre_adit_list.append(pre_price)
                        pre_real_list.append(usdjpy_bid)
                        print_pre_price = pre_price
                        if potision == "put":
                            if pre_divi > 0.006:  # result == 2 and
                                call_time = time.time()
                                before_principal = principal
                                have_doll, potision = traid.buy(principal, usdjpy_bid)
                                t0 = "call    "
                        elif potision == "call":
                            if time.time() - call_time > 900:
                                principal, potision = traid.sell(have_doll, usdjpy_bid)
                                divi_list = traid.profit(before_principal, principal, divi_list)
                                t0 = "put    "
                        else:
                            t0 = "potision: None   "
                    else:
                        t0 = "potision: None   "
                        print_pre_price = 0.00000
                    time2 = time.time()
                    time3 = time2 - time1
                    t = t0 + "RF予測結果：" + t2 + "正解率：" + str(round(score, 2) * 100) + "%   現在価格：" + str(
                        usdjpy_bid) + "円" + "   15分後の予測価格：" + str(round(print_pre_price, 3)) + "円   決定係数：" + str(
                        round(determination, 2)) + "   " + str(
                        round(time3, 2)) + "秒                                                          "
                    process_time2.append(round(time3, 2))
                else:
                    time2 = time.time()
                    time3 = time2 - time1
                    t = "学習中...   ループ回数：" + str(x_coordinates) + "回目　　　" + str(round(time3, 2)) + "秒        "
                time2 = time.time()
                time3 = time2 - time1
                process_time2.append(round(time3, 2))
            else:
                time2 = time.time()
                time3 = time2 - time1
                process_time1.append(round(time3, 2))
                t = "学習中...   ループ回数：" + str(x_coordinates) + "回目　　　" + str(round(time3, 2)) + "秒        "
            print("\r" + t, end="")
            #if time3 < 20:
                #time.sleep(20 - time3)


if __name__ == "__main__":
    main()

