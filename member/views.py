from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from member.models import Member

# Create your views here.
def join(request):
    returnPage='member/join.html'
    if request.method == 'GET':
        return render(request,'member/join.html')
    elif request.method=='POST':
        #폼으로 전송된 데이터들을 dict 형태로 저장
        form =request.POST.dict()
        # print(form,form['userid'])#전송된 데이터 확인

        # 유효성 검사 1/2만 3/4/5/
        error = ''  # 검사 결과 저장용 변수
        if not(form['userid'] and form['passwd'] and form['repasswd'] and form['name'] and form['email']):
            error = '입력값이 누락되었습니다.'
        elif (form['passwd'] != form['repasswd']) :
            error = '비밀번호가 일치하지 않습니다.!'
        else:
            #입력한 회원 정보를 Member 객체에 담음


            member= Member(userid=form['userid'],
                           passwd=make_password(form['passwd']),# 비밀번호는 암호화
                           name=form['name'],email=['email']
            )

            #Member객체에 담은 회원정보를 member 테이블에 저장
            member.save()

            #회원 가입 성공시 joinok.html를 뛰움
            returnPage='member/joinok.html'

        #유효성 검사를 실패하는 경우 오류내용을 join.html에 표시하기 위해 dict변수에 저장
        #또한 , 이미 입력했던 회원정보를 다시 join.html에 표시하기위해
        #form이라는 dict변수 생성

        context = {'form':form,'error':error}

        return  render(request,returnPage,context)


def login(request):
    return render(request,'member/login.html')


def myinfo(request):
    return render(request,'member/myinfo.html')