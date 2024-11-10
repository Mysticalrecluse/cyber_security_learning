username=["kubi","curry","james","durant","harden"]
password=["123","456","789","101","112"]
for i in range(3):
    user=input("请输入用户名：")
    passwd=input("请输入密码：")
    if user in username:
        if passwd==password[username.index(user)]:
            print("登录成功")
            break
        else:
            print("用户名或密码错误")
    else:
        print("用户名或密码错误")
else:
    print("登录失败")