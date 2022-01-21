while True:
    try:
        import csv,re

        with open("drug.csv", newline="", encoding="UTF-8-sig") as project: #newline 解決系統問題, encoding 解決 \ufeff 問題.
            reader = csv.reader(project)

            target_medicine = input("Please enter the English name of the medicine you want to search. Or enter \"q\" to quit\nInput : ")
            
            if target_medicine == "q":
                print("exit successfully")
                break

            str_match = [row for row in reader if re.search(rf"{target_medicine}.*", row[10], re.IGNORECASE)]

            if len(str_match) == 0:
                print("Can't find this medicine in the list, please re-enter")
                continue

            content = [
                "許可證字號",
                "註銷狀態",
                "註銷日期",
                "註銷理由",
                "有效日期",
                "發證日期",
                "許可證種類",
                "舊證字號",
                "通關簽審文件編號",
                "中文品名",
                "英文品名",
                "適應症",
                "劑型",
                "包裝",
                "藥品類別",
                "管制藥品分類級別",
                "主成分略述",
                "申請商名稱",
                "申請商地址",
                "申請商統一編號",
                "製造商名稱",
                "製造廠廠址",
                "製造廠公司地址",
                "製造廠國別",
                "製程",
                "異動日期",
                "用法用量",
                "包裝與國際條",
            ]

            print("```````````````````````````````````````````````````````````````````````````````````")
            for i, j in zip(content, str_match[0]): #只列出第一筆資料
                print(i + " : " + j)
            print("```````````````````````````````````````````````````````````````````````````````````")

    except:
        print("some thing wrong, process will exit.")
        exit()
