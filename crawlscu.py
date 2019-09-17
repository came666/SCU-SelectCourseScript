import requests
import json
import time
import os
from bs4 import BeautifulSoup
# import cv2
# import pytesseract
from PIL import Image
from io import BytesIO
from io import StringIO

class course(object):
    def __init__(self):
        self.begin = 0
        self.end = 0
class Login(object):
    def __init__(self):
        self.headers = {
        'Referer':'http://202.115.47.141/login',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Host':'202.115.47.141'
        }
        self.evaheaders={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://202.115.47.141',
            'Referer': 'http://202.115.47.141/student/teachingEvaluation/teachingEvaluation/evaluationPage',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        #get
        self.login_url = 'http://202.115.47.141/login'  
        self.login_css = 'http://202.115.47.141/css/login/login.css'
        self.jquery = 'http://202.115.47.141/js/jQuery/jquery.js'
        #
        self.post_url = 'http://202.115.47.141/j_spring_security_check'
        self.get_user_url = 'http://202.115.47.141/index.jsp'
        #get
        self.logined_url = 'http://202.115.47.141/index.jsp'
        self.course_url = 'http://202.115.47.141/student/courseSelect/thisSemesterCurriculum/ajaxStudentSchedule/callback'
        #get courseSelectIndex
        self.courseSelect_index = 'http://202.115.47.141/student/courseSelect/courseSelect/index'
        self.courseSelect_index2 = 'http://202.115.47.141/student/courseSelect/planCourse/index'
        self.checkInputCodeAndSubmit = 'http://202.115.47.141/student/courseSelect/selectCourse/checkInputCodeAndSubmit'
        self.getYzmPic = 'http://202.115.47.141/student/courseSelect/selectCourse/getYzmPic'
        # ?fajhh=4304
        #post courseList
        self.courseList = 'http://202.115.47.141/student/courseSelect/freeCourse/courseList'
        self.postcourse = 'http://202.115.47.141/student/courseSelect/selectCourses/waitingfor'
        self.quitcourse = 'http://202.115.47.141/student/courseSelect/quitCourse/index'
        self.quitpost = 'http://202.115.47.141/student/courseSelect/delCourse/deleteOne'
        self.query = 'http://202.115.47.141/student/courseSelect/selectResult/query'
        #
        self.evaluatedCourseInfo = 'http://202.115.47.141/student/teachingEvaluation/teachingEvaluation/search'
        self.evaluationPage = 'http://202.115.47.141/student/teachingEvaluation/teachingEvaluation/evaluationPage'
        self.evaluationpost = 'http://202.115.47.141/student/teachingEvaluation/teachingEvaluation/evaluation'
        self.search_course = 'http://202.115.47.141/student/courseSelect/freeCourse/courseList'
        self.session = requests.Session()
        self.user = ''
        self.examget = 'http://202.115.47.141/student/examinationManagement/examPlan/index'
        self.examinfo = 'http://202.115.47.141/student/examinationManagement/examPlan/detail?'
        self.logincaptcha = 'http://202.115.47.141/img/captcha.jpg'
        self.reco = "http://127.0.0.1:6000/b"

    def login(self,username,passwd):
        imgbuf = self.session.get(self.logincaptcha).content
        f = Image.open(BytesIO(imgbuf))
        f.save('Logincap.jpg')
        # fImg = cv2.imread("Logincap.jpg")
        # cv2.imshow("Image",fImg)
        vercode = input("Please input vercode(Image file is same as the file location):")
        # f = open('Logincap.jpg','rb')
        # files = {'image_file': ('Logincap.jpg', f, 'application')}
        # vercode = self.session.post(url=self.reco,files=files).text
        # f.close()

        post_data = {
            'j_username':username,
            'j_password':passwd,
            'j_captcha':str(vercode)
        }

        response = self.session.get(self.login_url,headers = self.headers)
        # response = self.session.get(self.login_css,headers = self.headers)
        # response = self.session.get(self.jquery,headers = self.headers)
        response = self.session.post(self.post_url,data=post_data,headers=self.headers)
        response = self.session.get(self.get_user_url,headers = self.headers)
        data = response.content
        data = BeautifulSoup(data,'lxml')
        # print(data)
        user = data.find('span',attrs = {"class":"user-info"})
        # user= user.text
        self.user = user
        #output test login information.
        # print(response.text)

    def getExaminfo(self):
        h = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': '202.115.47.141',
            'Referer': 'http://202.115.47.141/student/examinationManagement/examPlan/index',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        parm = {
            'start': '2019-01-07',
            'end': '2019-03-10',
            '_': '1546088952500'
        }
        response = self.session.get(self.examget,headers=self.headers)
        response = self.session.get(self.examinfo,params = parm,headers=h).json()
        l = len(response)-1
        fp = open('examInfo.txt','w')
        while (l>=0):
            info = response[l]
            print("考试日期"+info['start'])
            print(info['title'])
            print("考试日期"+info['start'],file=fp)
            print(info['title'],file=fp)
            l-=1

        fp.close()
        print("考试信息文件已存储在本文件根目录 examInfo.txt中.")
        # print(response)

    def evaluatedCourse(self):
        response = self.session.post(self.evaluatedCourseInfo,headers=self.headers)
        response = response.json()
        coursesInfo = response.get('data')

        for course in coursesInfo:
            evaluatedPeople = course['evaluatedPeople']
            evaluatedContent = course['evaluationContent']

            coureSequenceNumber_id = course['id']['coureSequenceNumber']
            evaluatedPeople_id = course['id']['evaluatedPeople']
            evaluationContentNumber_id = course['id']['evaluationContentNumber']
            questionnaireCoding_id = course['id']['questionnaireCoding']
            questionnaireName = course['questionnaire']['questionnaireName']
            isEvaluated = course['isEvaluated']
            if (isEvaluated == "是"):
                print(evaluatedPeople + '的' + evaluatedContent + '课程已经评教..自动跳过..ヾ|≧_≦|〃')
                continue
            evaluationPage_postdata = {
                'evaluatedPeople': evaluatedPeople,
                'evaluatedPeopleNumber': evaluatedPeople_id,
                'questionnaireCode': questionnaireCoding_id,
                'questionnaireName': questionnaireName,
                'evaluationContentNumber': evaluationContentNumber_id,
                'evaluationContentContent': ''
            }
            evaluatedPage = self.session.post(self.evaluationPage,data=evaluationPage_postdata,headers=self.headers)
            evaluatedPage = evaluatedPage.content
            evaluatedPage = BeautifulSoup(evaluatedPage,'lxml')
            tokenValue = evaluatedPage.find('input',attrs = {"name":"tokenValue"})['value']

            ketang_postdata = {
#                 tokenValue: 3bace6196264448fffacdc3bcda2efdc
# questionnaireCode: 0000000084
# evaluationContentNumber: 311221020
# evaluatedPeopleNumber: 20042116
# count: 0
# 0000000107: 10_1
# 0000000108: 10_1
# 0000000123: 10_1
# 0000000127: 10_1
# 0000000128: 10_1
# 0000000129: 10_1
# 0000000131: 10_1
# zgpj: 同意.
                'tokenValue':tokenValue,
                'questionnaireCode':questionnaireCoding_id,
                'evaluationContentNumber':evaluationContentNumber_id,
                'evaluatedPeopleNumber':evaluatedPeople_id,
                '0000000036':'10_1',
                '0000000037':'10_1',
                '0000000038':'10_1',
                '0000000039':'10_1',
                '0000000040':'10_1',
                '0000000041':'10_1',
                '0000000042':'10_1',
                'zgpj':'test'
            }
            
            tiyu_postdata = {
                'tokenValue':tokenValue,
                'questionnaireCode':questionnaireCoding_id,
                'evaluationContentNumber':evaluationContentNumber_id,
                'evaluatedPeopleNumber':evaluatedPeople_id,
                '0000000096':'10_1',
                '0000000097':'10_1',
                '0000000098':'10_1',
                '0000000099':'10_1',
                '0000000100':'10_1',
                '0000000101':'10_1',
                '0000000102':'10_1',
                'zgpj':'test'
            }

            shiyan_postdata = {
                'tokenValue':tokenValue,
                'questionnaireCode':questionnaireCoding_id,
                'evaluationContentNumber':evaluationContentNumber_id,
                'evaluatedPeopleNumber':evaluatedPeople_id,
                '0000000082':'10_1',
                '0000000083':'10_1',
                '0000000084':'10_1',
                '0000000085':'10_1',
                '0000000086':'10_1',
                '0000000087':'10_1',
                '0000000088':'10_1',
                'zgpj':'test'
            }

            zhujiao_postdata = {
                'tokenValue':tokenValue,
                'questionnaireCode':questionnaireCoding_id,
                'evaluationContentNumber':evaluationContentNumber_id,
                'evaluatedPeopleNumber':evaluatedPeople_id,
                '0000000028':'10_1',
                '0000000029':'10_1',
                '0000000030':'10_1',
                '0000000031':'10_1',
                '0000000032':'10_1',
                '0000000033':'10_1',
                'zgpj':'test'
            }
            if (questionnaireName == "学生评教（课堂教学）"):
                self.session.post(self.evaluationpost,headers = self.evaheaders,data=ketang_postdata)
            if (questionnaireName == "学生评教（实验教学）"):
                self.session.post(self.evaluationpost,headers = self.evaheaders,data=shiyan_postdata)
            if (questionnaireName == "学生评教（体育教学）"):
                self.session.post(self.evaluationpost,headers = self.evaheaders,data=tiyu_postdata)
            if (questionnaireName == "研究生助教评价"):
                self.session.post(self.evaluationpost,headers = self.evaheaders,data=zhujiao_postdata)
                
            print(evaluatedPeople + '的' + evaluatedContent + '课程评教完成..自动等待2分钟ヾ|≧_≦|〃')
            i = 122
            while (i > 0):
                print('当前剩余:'+ str(i) + 's...')
                i-=1
                time.sleep(1)





    def crawlCourse(self):
        response = self.session.get(self.course_url,headers = self.headers)
        response = response.json()
        data = response.get('xkxx')[0]
        course = {}
        for i in range(7):
            course[i] = {}

        for key in data:
            # course[data[key]['classDay']][data[key]['courseName']] = data[key]['classSessions']
            # print(data[key]['courseName'])
            courseName = data[key]['courseName']
            timeAndPlaceList = data[key]['timeAndPlaceList']

            for course_ in timeAndPlaceList:  
                classDay = course_['classDay']
                classSession = course_['classSessions']
                teachingBuildingName = course_['teachingBuildingName']
                classroomName = course_['classroomName']
                course[classDay][classSession] = courseName + " " + teachingBuildingName + classroomName

            # classDay = data[key]['timeAndPlaceList'][0]['classDay']
            # classSession = data[key]['timeAndPlaceList'][0]['classSessions'] 
            # teachingBuildingName = data[key]['timeAndPlaceList'][0]['teachingBuildingName']
            # classroomName = data[key]['timeAndPlaceList'][0]['classroomName']
            # course[classDay][classSession] = courseName + " " + teachingBuildingName + classroomName
        courseData = open('course.txt','w')
        for i in range(7):
            keys = course[i].keys()
            values = course[i].values()
 
            list_one = [(key, val) for key, val in zip(keys, values)]
            list_sort = sorted(list_one, key=lambda x: x[0])
            print("Week day" + str(i))
            print("Week day" + str(i),file=courseData)
            # print(list_sort)
            for data in list_sort:
                print("Class begins: " + str(data[0]))
                print("Class name: " + data[1])

                print("Class begins: " + str(data[0]),file = courseData)
                print("Class name: " + data[1],file = courseData)
            print("   ")
            print("   ",file=courseData)
            # print("Week day" + str(i),file=courseData)
            # print(list_sort,file=courseData)
        
        courseData.close()

    def allCourses(self):
        response = self.session.get(self.course_url,headers = self.headers)
        response = response.json()
        data = response.get('xkxx')[0]
        for key in data:
            courseName = data[key]['courseName']
            attendClassTeacher = data[key]['attendClassTeacher']
            timeAndPlaceList = data[key]['timeAndPlaceList']
            print(key + ": " + courseName + " "+attendClassTeacher)
            for course_ in timeAndPlaceList:  
                classDay = course_['classDay']
                classSession = course_['classSessions']
                print("Begin: "+ str(classDay) + "  length:"+str(classSession))
            print('')
    def quitc(self,kch_,kxh_):
        response = self.session.get(self.courseSelect_index,headers = self.headers)
        response = self.session.get(self.courseSelect_index2,headers = self.headers).content
        content = BeautifulSoup(response,"html5lib")
        tokenValue = content.find(name='input',attrs={"name":"tokenValue"})["value"]
        fajhh = content.find(name='input',attrs={"name":"fajhh"})["value"]
        p_data= {
            'fajhh' : fajhh,
            'kch':kch_,
            'kxh':kxh_,
            'tokenValue':tokenValue
        }
        response = self.session.get(self.quitcourse,headers=self.headers)
        self.session.post(self.quitpost,data=p_data,headers=self.headers)
        print("Quit Course done.")

    def del_noise(self,im_cut):
        for a in range(len(im_cut)):
            for b in range(len(im_cut[0])):
                if (im_cut[a][b][0] < 20 and im_cut[a][b][1] < 20 and im_cut[a][b][2] < 20):
                    im_cut[a][b][0] = 255
                    im_cut[a][b][1] = 255
                    im_cut[a][b][2] = 255
        im_cut = cv2.cvtColor(im_cut, cv2.COLOR_BGR2GRAY)
        for i in range(len(im_cut)):
            for j in range(len(im_cut[0])):
                if (im_cut[i][j] > 25 and im_cut[i][j] < 200):
                    im_cut[i][j] = 0
                else:
                    im_cut[i][j] = 255
        return im_cut
    def getCourseList(self,search_info):
        courseData = open(search_info+'.txt','w')
        post_data = {
            'searchtj': search_info,
            'xq': '0',
            'jc': '0',
            'kyl': '0',
            'kclbdm': ''
        }
        response = self.session.post(self.search_course,data=post_data,headers=self.headers)
        response = response.json()
        # print(response)
        course = response.get('rwRxkZlList')
        course = eval(course)
        size = len(course)
        print('课程查询_By SsorryQaQ',file=courseData)
        print('')
        print('******************************************************',file=courseData)
        for i in range(0,size):
            coursenumLast = course[i]["bkskyl"]
            coursepos = course[i]["kkxqm"]
            xueyuan = course[i]["kkxsjc"]
            kechengming = course[i]["kcm"]
            kch = course[i]["kch"]
            kxh = course[i]["kxh"]
            sjdd = course[i]["sjdd"]
            

            kechengID = '2018-2019-2-1_'+kch+'_'+kxh 
            teacher = course[i]["skjs"]
            # "教师:" + teacher + " "+coursepos

            coursesize = len(sjdd)


            print('******************************************************',file=courseData)
            print(kechengming + "  开设学院:" + xueyuan + " 上课地点:" + coursepos,file=courseData)
            for j in range(0,coursesize):
                cxjc = sjdd[j]['cxjc']
                skjc = sjdd[j]['skjc']
                skxq = sjdd[j]['skxq']
                jasm = sjdd[j]['jasm']
                print("上课时间: 星期" +str(skxq) + " 第"+str(skjc)+"节,"+"时长:"+str(cxjc)+"节",file=courseData)
                print("上课地点: "+jasm,file=courseData)
            print("课程号_课序号: "+kch+'_'+kxh + " 教师:" + teacher,file=courseData)
            print("课余量: " +str(coursenumLast),file=courseData)
            print('',file=courseData)
            print('******************************************************',file=courseData)
            print('',file=courseData)


        courseData.close()
        print("你的查询结果已经写入在此文件根目录   "+search_info+'.txt')
        
    def course(self,username,kcID,kechengh):
        # time.sleep(0.1)
        post_data = {
            'searchtj': kcID,
            'xq': '0',
            'jc': '0',
            'kyl': '0',
            'kclbdm': ''
        }
        response = self.session.post(self.search_course,data=post_data,headers=self.headers)
        response = response.json()
        course = response.get('rwRxkZlList')
        course = eval(course)
        size = len(course)
        kcm_enc = ""
        kechengming = ""
        kxh = ""
        kechengID = ""
        for i in range(0,size):
            coursenumLast = course[i]["bkskyl"]
            coursepos = course[i]["kkxqm"]
            xueyuan = course[i]["kkxsjc"]
            kechengming = course[i]["kcm"]
            kch = course[i]["kch"]
            kxh = course[i]["kxh"]
            kechengID = kcID + '_' + kechengh + '_2019-2020-1-1'

            teacher = course[i]["skjs"]
            if (kechengh==str(kxh)):
                print('')
                print("选择的课程:")
                print(kechengming + "  开设学院:" + xueyuan + " 上课地点:" + coursepos)
                print("课程号_课序号: "+kch+'_'+kxh + " 教师:" + teacher)
                print("课余量: " +str(coursenumLast))
                print('')
                print(kechengming)
                break
        if (kechengming == ""):
            print(kcID + '_' + kechengh +" select Done")
            return
        print(coursenumLast)
        if (coursenumLast == 0):
            print('当前课程没有课余量....')
            return

        for c in kechengming+'_'+kxh:
            kcm_enc = kcm_enc + str(ord(c))
            kcm_enc = kcm_enc + ","
        
        
        
        response = self.session.get(self.courseSelect_index,headers=self.headers)
        # print(response)
        # print(response.text)
        response = response.content
        
        response = BeautifulSoup(response,'html5lib')
        # img = self.session.get(self.getYzmPic,headers=self.headers).content

        # f = Image.open(BytesIO(img))
        # f.save(username + 'captcha.jpg')
        # f = open(username + 'captcha.jpg','rb')
        # files = {'image_file': (username + 'captcha.jpg', f, 'application')}
        # yzmres = self.session.post(url=self.reco,files=files).text
        # f.close()

        # print(yzmres)

        tokenValue = response.find('input',attrs = {"id":"tokenValue"})["value"]
        # fajhh = response.find(name='input',attrs={"name":"fajhh"})["value"]


        username = username + '2'

            # 'tokenValue':tokenValue,
        post_data2={
            'dealType': '5',
            'kcIds':kechengID,
            'kcms':kcm_enc,
            'fajhh':'',
            'sj':'0_0',
            'searchtj':kechengID,
            'kclbdm':'',
            'inputCode':'',
            'tokenValue':tokenValue
        }
        
        post_data3 = {
            'kcNum':'1',
            'redisKey':username
        }
        #response = self.session.post(self.courseList,data=post_data1,headers = self.headers)
        #response = self.session.post(self.postcourse,data=post_data2,headers=self.headers)
        
        response = self.session.post(self.checkInputCodeAndSubmit,data=post_data2,headers=self.headers)
        print(response.text)
        # if (len(response.text) == 61):
        #     wrongcap = 'D:\\备份。\\crawlscu\\wrongimg\\'
        #     ff = Image.open(BytesIO(img))
        #     ff.save(wrongcap + yzmres + '.jpg')
        # time.sleep(0.2)
        # for i in range(5):
        #     response = self.session.post(self.query,data=post_data3,headers=self.headers)
        #     print(response.text)


