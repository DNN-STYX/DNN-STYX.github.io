#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("../")
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'

from xlrd import open_workbook

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False



def collect(dir):
    tra = []
    adv = []
    mut1 = []
    mut2 = []
    mut3 = []
    mut4 = []
    filename1 = open_workbook(dir)
    sheet1 = filename1.sheets()[0]
    line_num = 1
    while True:
        try:
            sheet1.cell_value(line_num, 0)
        except IndexError:
            break
        else:
            tra.append(float(sheet1.cell_value(line_num, 4)))
            mut1.append(float(sheet1.cell_value(line_num, 7)))
            mut2.append(float(sheet1.cell_value(line_num, 10)))
            mut3.append(float(sheet1.cell_value(line_num, 13)))
            mut4.append(float(sheet1.cell_value(line_num, 16)))
            adv.append(float(sheet1.cell_value(line_num, 19)))
            line_num += 1
    tra_test_value = float(sheet1.cell_value(1, 3))
    tra_robust_value = sum(tra) / (line_num - 1)
    mut1_test_value = float(sheet1.cell_value(1, 6))
    mut1_robust_value = sum(mut1) / (line_num - 1)
    mut2_test_value = float(sheet1.cell_value(1, 9))
    mut2_robust_value = sum(mut2) / (line_num - 1)
    mut3_test_value = float(sheet1.cell_value(1, 12))
    mut3_robust_value = sum(mut3) / (line_num - 1)
    mut4_test_value = float(sheet1.cell_value(1, 15))
    mut4_robust_value = sum(mut4) / (line_num - 1)
    mut_test_value = (mut1_test_value + mut2_test_value + mut3_test_value + mut4_test_value) / 4
    mut_robust_value = (mut1_robust_value + mut2_robust_value + mut3_robust_value + mut4_robust_value) / 4
    adv_test_value = float(sheet1.cell_value(1, 18))
    adv_robust_value = sum(adv) / (line_num - 1)

    test_value = [tra_test_value, mut_test_value, adv_test_value]
    robust_value = [tra_robust_value, mut_robust_value, adv_robust_value]

    # print("test: \n" + str(tra_test_value) + "\n" + str(mut1_test_value) + "\n" + str(mut2_test_value) + "\n" + str(mut3_test_value) + "\n" + str(mut4_test_value) + "\n"  + str(adv_test_value))
    # print("===================")
    # print("robust: \n" + str(tra_robust_value) + "\n" + str(mut1_robust_value) + "\n" + str(mut2_robust_value) + "\n" + str(mut3_robust_value) + "\n" + str(mut4_robust_value) + "\n" + str(adv_robust_value))

    # print("test: \n" + str(tra_test_value) + "\n" + str(mut_test_value) + "\n" + str(adv_test_value))
    # print("===================")
    # print("robust: \n" + str(tra_robust_value) + "\n" + str(mut_robust_value) + "\n" + str(adv_robust_value))

    return test_value, robust_value


attack_names = ["FGM", "BIM", "DeepFool"]

# intuition-1  关于防御的局限性
if 0:
    filename1 = open_workbook("./Intuition/evaluation.xls")
    sheet1 = filename1.sheets()[0]

    # 为数据收集做准备
    # ===========================FGM========================= #
    FGM_acc_ori = []
    FGM_acc_robust = []
    # ===========================BIM========================= #
    BIM_acc_ori = []
    BIM_acc_robust = []
    # ===========================DeepFool========================= #
    DeepFool_acc_ori = []
    DeepFool_acc_robust = []

    line_num = 1
    while True:
        try:
            sheet1.cell_value(line_num, 0)
        except IndexError:
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            plt.figure(figsize=(10, 6))
            plt.plot(x, FGM_acc_ori, c='black', ls='-', marker='o', label="FGSM-tra")
            plt.plot(x, FGM_acc_robust, c='black', ls=':', marker='*', label="FGSM-adv")
            plt.plot(x, BIM_acc_ori, c='r', ls='-', marker='o', label="BIM-tra")
            plt.plot(x, BIM_acc_robust, c='r', ls=':', marker='*', label="BIM-adv")
            plt.plot(x, DeepFool_acc_ori, c='b', ls='-', marker='o', label="DeepFool-tra")
            plt.plot(x, DeepFool_acc_robust, c='b', ls=':', marker='*', label="DeepFool-adv")
            plt.legend()
            plt.xlabel(u"Configuration Index")
            plt.ylabel("Robustness")
            plt.title("Adversarial Training-Robustness")
            if not os.path.exists("./figure"):
                os.system("mkdir figure")
            plt.savefig("./figure/Intuition-robustness.pdf")
            plt.close()
            break
        else:
            attack_name = sheet1.cell_value(line_num, 0)

            if "FGM" in attack_name:
                FGM_acc_ori.append(float(sheet1.cell_value(line_num, 2)))
                FGM_acc_robust.append(float(sheet1.cell_value(line_num, 5)))
            elif "BIM" in attack_name:
                BIM_acc_ori.append(float(sheet1.cell_value(line_num, 2)))
                BIM_acc_robust.append(float(sheet1.cell_value(line_num, 5)))
            elif "DeepFool" in attack_name:
                DeepFool_acc_ori.append(float(sheet1.cell_value(line_num, 2)))
                DeepFool_acc_robust.append(float(sheet1.cell_value(line_num, 5)))
            line_num += 1

# intuition-2   关于准确率
if 0:
    tra_test = []
    mut_test = []
    adv_test = []
    for model_name in ["mnist_MLP", "mnist_CNN", "fmnist_MLP", "fmnist_CNN", "cifar10_CNN"]:
        dir = "./FGM/" + model_name + "/evaluation.xls"
        [test_value, robust_value] = collect(dir)
        tra_test.append(test_value[0])
        mut_test.append(test_value[1])
        adv_test.append(test_value[2])

    x = np.array([1, 2, 3, 4, 5])
    plt.figure(figsize=(10, 10))
    plt.bar(x, tra_test,
            width=0.2,
            color='black',
            align='center',
            label='traditional training',
            alpha=0.5
            )
    plt.bar(x + 0.2, mut_test,
            width=0.2,
            color='red',
            align='center',
            label='mutation training',
            alpha=0.5
            )
    plt.bar(x + 0.4, adv_test,
            width=0.2,
            color='blue',
            align='center',
            label='adversarial training',
            alpha=0.5
            )

    plt.legend(loc='upper right', fontsize=15)
    plt.xlabel(u"Model", fontsize=20)
    plt.ylabel(u"Test accuracy", fontsize=20)

    plt.xticks(x + 0.2, ["mnist_MLP", "mnist_CNN", "fmnist_MLP", "fmnist_CNN", "cifar10_CNN"], fontsize=17)
    plt.ylim(0.5, 1.0)
    # plt.yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1], fontsize=20)
    plt.yticks(fontsize=20)
    plt.title(u"Accuracy Difference", fontsize=20)


    if not os.path.exists("./figure"):
        os.system("mkdir figure")
    plt.savefig("./figure/accuracy.pdf")
    plt.close()

# all-result
if 1:
    for attack_name in attack_names:
        ave = 0
        tra_robust = []
        mut_robust = []
        adv_robust = []
        for model_name in ["mnist_MLP", "mnist_CNN", "fmnist_MLP", "fmnist_CNN", "cifar10_CNN"]:
            dir = "./" + attack_name + "/" + model_name + "/evaluation.xls"
            [test_value, robust_value] = collect(dir)
            tra_robust.append(robust_value[0])
            mut_robust.append(robust_value[1])
            adv_robust.append(robust_value[2])
            ave += robust_value[1] - robust_value[0]
        print(ave/5)

        x = np.array([1, 2, 3, 4 ,5])
        plt.figure(figsize=(10, 10))
        plt.bar(x, tra_robust,
                width=0.15,
                color='black',
                align='center',
                label='traditional training',
                alpha=0.5
                )
        plt.bar(x + 0.15, mut_robust,
                width=0.15,
                color='red',
                align='center',
                label='mutation training',
                alpha=0.5
                )
        plt.bar(x + 0.3, adv_robust,
                width=0.15,
                color='blue',
                align='center',
                label='adversarial training',
                alpha=0.5
                )

        plt.legend(loc='upper right', fontsize=15)
        plt.xlabel(u"Model", fontsize=20)
        plt.ylabel(u"Robustness", fontsize=20)
        if attack_name == "FGM":
            attack_name = "FGSM"
        plt.title(attack_name, fontsize=20)

        plt.xticks(x + 0.15, ["mnist_MLP", "mnist_CNN", "fmnist_MLP", "fmnist_CNN", "cifar10_CNN"], fontsize=15)
        plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], fontsize=20)

        if not os.path.exists("./figure"):
            os.system("mkdir figure")
        plt.savefig("./figure/" + attack_name + ".pdf")
        plt.close()
