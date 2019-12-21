import crawlscu
import os
import requests
import time

if __name__ == "__main__":
    login = crawlscu.Login()
    # p = input("请输入软件密码: ")
    # if (p != 'sorry'):
    #     print('Wrong password!')
    #     exit(0)
    
    print('******************************************************')
    print("欢迎使用SsorryQaQ的小工具:自动抢课")
    print('******************************************************')
    print('')
    username = input('请输入学号: ')
    passwd =  input('请输入密码: ')
    

    login.login(username,passwd)
    print(login.user)

    courses = {}
    
    while (1):
        kcId = input("请输入要需要抢的课程号(格式 201051020)(0 to finish): ")
        kcm = input("请输入要需要抢的课序号(格式 01)(0 to finish): ")
        if (str(kcId) == '0'):
            break
        courses[kcId] = kcm
    cnt = 1
    while (1):
        # login.session = requests.Session()
        # login.login(username,passwd)
        time.sleep(0.1)
        for key in courses:
            login.course(username,key,courses[key])
        # 105395020_221
        # try:
        # login.course(username,'105395020','229')
        
        
            # login.course(username,'999005030','03')
            # login.course(username,'999005030','05') 
            # login.course(username,'999005030','06')
            # login.course(username,'999005030','07')
            # login.course(username,'999006030','03') 
            #login.course(username,'999007030','01')
            #login.course(username,'999007030','02') have 3
            #login.course(username,'999007030','03')
            # login.course(username,'105395020','210')
        # except:
        #     time.sleep(1)
        #     login.login(username,passwd)
        #     continue

        # 女性学(107055020_01)	
        # 健康传播概论(504416020_01)
        # 全球健康概论(504415020_01)
        # 中华文化（艺术篇）(999008030_01)	
        # 中华文化（历史篇）(999005030_02)
        # 中华文化（历史篇）(999005030_03)	
        # 中华文化（历史篇）(999005030_05)	
        # 中华文化（历史篇）(999005030_06)	
        # login.course(username,'107117000','04')
        # img = login.session.get(login.getYzmPic,headers=login.headers).content
        # f = open('./img/'+ str(cnt) + '.png','wb')
        # f.write(img)
        # f.close()
        # time.sleep(0.1)
        # cnt += 1
        # if (cnt > 5000):
        #     break
        # 105368020_105
        # login.course(username,'311039030','02')

    # login.getCourseList('数学')
# 999005030 01
# 999006030 05
# 999007030 02
# 311039030 02