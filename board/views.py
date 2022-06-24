from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
from board.models import board


def list(request):
#게시판 목록 보기
    bdlist = board.objects.values('id','title','userid','regdate','views')\
    .order_by('-id')

    context={'bds':bdlist}
    return render(request, 'board/list.html',context)

#게시판 본문 보기
def view(request):
    return render(request, 'board/view.html')


#게시판 글쓰기
#get : board/write.html
#post:작성한 글을 디비에 저장, board/list.html로 이동
def write(request):
    returnPage = 'board/write.html'
    error = ''
    form = ''
    if request.method =='GET':
        pass
    elif request.method == 'POST':
        form=request.POST.dict()

        #유효성 검사1

        if not (form['title'] and form['contents']):
            error='제목이나 본문을 작성하세요!'
        else:
            # 입력한 게시글을 Board 객체에 담음

            bd=board(title=form['title'],
                     contents=form['contents'],
                     #새글을 작성한 작성한 회원에 대한 정보는
                     #회원테이블에 존재하는 회원아이디를 조회해서
                     #userid속성에 저장
                     userid=Member.objects.get(pk=form['memberid'])
                     )
            bd.save() #Board객체에 담은 게시글을 테이블에 저장
            return  redirect('/list')
    context = {'form': form, 'error': error}

    return render(request, returnPage,context)

