#!/usr/bin/env python
###################################################################################################
#
# Title: bank_loan_calculator.py
# Usage: To make a calculation for the bank loan
# Author: Wi1s0n
# Date: 2021/09/15
#
###################################################################################################

import prettytable as pt
import matplotlib.pyplot as plt


class LoanCalculation(object):
    """
    [住房贷款计算器]
    1、支持等额本息、等额本金两种计算方式；
    2、还款周期以月为单位，输出当前期数、月供总额、月供本金、月供利息、剩余本金；
    3、交互式菜单输入，并以表格形式显示结果，增加可读性。
    """

    def __init__(self):
        """
        @param installment_list: 月供清单
        @param total_payment: 还款总额
        @param total_interest: 利息总额
        """
        # self.installment_list = []
        # self.total_payment = 0
        # self.total_interest = 0

    def equal_interest(self, P, R, N):
        equal_interest_res = {}
        installment_list = []
        total_payment = 0
        total_interest = 0
        """等额本息"""
        Pi = P
        A = (P * R / 1200 * (1 + R / 1200) ** N) / ((1 + R / 1200) ** N - 1)
        for i in range(1, N + 1):
            B = (P * R / 1200 * (1 + R / 1200) ** (i - 1)) / ((1 + R / 1200) ** N - 1)
            r = A - B
            Pi -= B
            installment_dict = {"time_num": i,
                                "monthly_payment": round(A, 2),
                                "monthly_principal": round(B, 2),
                                "monthly_interest": round(r, 2),
                                "rest_loan": round(Pi, 2)}
            installment_list.append(installment_dict)
        total_payment = (round(sum([x["monthly_payment"] for x in installment_list])))
        total_interest = (round(sum([x["monthly_interest"] for x in installment_list])))

        equal_interest_res["installment_list"] = installment_list
        equal_interest_res["total_payment"] = total_payment
        equal_interest_res["total_interest"] = total_interest
        return equal_interest_res

    def equal_principal(self, P, R, N):
        equal_principal_res = {}
        installment_list = []
        total_payment = 0
        total_interest = 0
        """等额本金"""
        B = P / N
        for i in range(1, N + 1):
            A = P / N + (P - P / N * (i - 1)) * R / 1200
            r = A - B
            installment_dict = {"time_num": i,
                                "monthly_payment": round(A, 2),
                                "monthly_principal": round(B, 2),
                                "monthly_interest": round(r, 2),
                                "rest_loan": round(P - P / N * i, 2)}
            installment_list.append(installment_dict)
        total_payment = (round(sum([x["monthly_payment"] for x in installment_list])))
        total_interest = (round(sum([x["monthly_interest"] for x in installment_list])))

        equal_principal_res["installment_list"] = installment_list
        equal_principal_res["total_payment"] = total_payment
        equal_principal_res["total_interest"] = total_interest
        return equal_principal_res

    def show_as_table_output(self, installment_list):
        """输出表格"""
        tb = pt.PrettyTable()
        tb.field_names = list(installment_list[0].keys())
        for i in installment_list:
            tb.add_row(list(i.values()))
        # self.installment_list.clear() # 清空列表
        print(tb)

    @staticmethod
    def print_menu():
        """程序菜单提示"""
        main_menu = pt.PrettyTable()
        main_menu.field_names = ["The Bank Loan Calculator V1.0"]
        main_menu.add_row(["[1] Equality principal and interest" + " " * 18])
        main_menu.add_row(["[2] Equality principal" + " " * 32])
        main_menu.add_row(["[0] quit" + " " * 46])
        main_menu.junction_char = "#"
        main_menu.horizontal_char = "*"
        main_menu.vertical_char = "|"
        return main_menu

    @staticmethod
    def option_info(opcode, P, R, N):
        """用户选项信息"""
        user_scheme_info = pt.PrettyTable()
        user_scheme_info.field_names = ["Loan scheme", "Principal (RMB)", "Annual interest rate (%)",
                                        "Loan time (month)"]
        if opcode == 1:
            user_scheme_info.add_row(["Equality principal&interest", P, R, N])
        else:
            user_scheme_info.add_row(["Equality principal", P, R, N])
        return user_scheme_info

    def calculate(self, opcode, P, R, N):
        """计算结果显示"""
        # print("Your loan scheme details is as follow:")
        # print(self.option_info(opcode, P, R, N))
        calculate_result = {}
        if opcode == 1:
            calculate_result = self.equal_interest(P, R, N)
        else:
            calculate_result = self.equal_principal(P, R, N)
        return calculate_result

    def find_half_sum_index(self, arr):
        total_sum = sum(arr)
        half_sum = total_sum // 2
        current_sum = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum >= half_sum:
                return i
        return -1  # 如果没有找到符合条件的位置，返回-1

    def show_as_chart(self, calculate_result):
        installment_list = calculate_result.get("installment_list")
        total_payment = calculate_result.get("total_payment")
        total_interest = calculate_result.get("total_interest")
        principals = []
        interests = []
        months = []
        monthly_payment = []
        for item_dict in installment_list:
            months.append(item_dict["time_num"])
            principals.append(item_dict["monthly_principal"])
            interests.append(item_dict["monthly_interest"])
            monthly_payment.append(item_dict["monthly_payment"])

        plt.bar(months, principals, label="principals")
        plt.bar(months, interests, bottom=principals, label="interests")

        print(sum(interests[:35]))
        half_month = self.find_half_sum_index(interests)
        print("total_payment, total_interest ", total_payment, total_interest)
        print("half_month", half_month)
        plt.axvline(x=half_month, color='r', linestyle='--')
        # 设置横坐标和纵坐标的标签
        plt.xlabel('time_num')
        plt.ylabel('currency')
        # 设置图表标题
        plt.title('load detail')
        # 添加图例
        plt.legend()
        # 显示图表
        plt.show()

    def get_P_R_N(self, opcode):
        if opcode in [0, 1, 2]:
            if opcode == 0:
                return
            P = float(input("Please input the principal:"))
            R = float(input("Please input the annual interest rate (%):"))
            N = int(input("Please input the loan time (month):"))
        else:
            print("[Warning] Invalid value,motherfucker!Please re-type your information.")
            return None

        return P, R, N

    def merge_installment_list(self, installment_lists):
        list1 = installment_lists[0]
        list2 = installment_lists[1]
        installment_list = []

        for i in range(0, len(list1) - 1):
            monthly1 = list1[i]
            monthly2 = list2[i]

            installment_dict = {"time_num": i,
                                "monthly_payment": monthly1["monthly_payment"] + monthly2["monthly_payment"],
                                "monthly_principal": monthly1["monthly_principal"] + monthly2["monthly_principal"],
                                "monthly_interest": monthly1["monthly_interest"] + monthly2["monthly_interest"],
                                "rest_loan" : monthly1["rest_loan"] + monthly2["rest_loan"]}
            installment_list.append(installment_dict)
        return installment_list

    def merge_calculate_res(self, calculate_results):
        if len(calculate_results) == 1:
            return calculate_results[0]

        calculate_result = {}
        total_payment = 0
        total_interest = 0
        installment_lists = []
        for item in calculate_results:
            installment_lists.append(item["installment_list"])
            total_payment += item["total_payment"]
            total_interest += item["total_interest"]
        installment_list = self.merge_installment_list(installment_lists)
        calculate_result["installment_list"] = installment_list
        calculate_result["total_payment"] = total_payment
        calculate_result["total_interest"] = total_payment
        return calculate_result
    def input_control(self):
        """用户输入控制"""
        while True:
            try:
                print("1 - 公积金或者商贷，2 - 公积金和商贷组合贷款")
                mode = int(input("Please input the mode you want:"))
                print(self.print_menu())
                opcode = int(input("Please input the option you want:"))
                array = []
                i = 0
                while i < mode:
                    P, R, N = self.get_P_R_N(opcode)
                    if P is None:
                        continue
                    item = {}
                    item["P"] = P
                    item["R"] = R
                    item["N"] = N

                    array.append(item)
                    i = i + 1
            except ValueError:
                print("[Warning] Invalid value,motherfucker!Please re-type your information.")
                continue

            calculate_results = []
            for obj in array:
                P = obj["P"]
                R = obj["R"]
                N = obj["N"]
                calculate_results.append(self.calculate(opcode, P, R, N))
            calculate_result = self.merge_calculate_res(calculate_results)
            self.show_as_table_output(calculate_result.get("installment_list"))
            self.show_as_chart(calculate_result)


if __name__ == '__main__':
    wilson = LoanCalculation()
    wilson.input_control()
    print("Goodbye,gentlemen！")
