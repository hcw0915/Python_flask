# 例外處理情境：轉換資料型態失敗
# 使用者如果輸入的格式資料不能轉換成數字，請他重新輸入直到輸入成功為止。
while True:
  data = input("請輸入一個數字:")
  try:
    number = int(data)
    break
  except Exception:
    print("輸入格式錯誤，請重新輸入")

number = number * 2
print(number)