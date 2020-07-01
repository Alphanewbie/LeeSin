from .models import *
from . import main_crawling, model_crud

from django.http import JsonResponse
from django.db.models import Subquery
from django.shortcuts import render
from django.db.models import Count

import time
import requests
from matplotlib import pyplot as plt

# Create your views here.


def index(request):
    # main_crawling.init_setting()

    return render(request, 'mains/index.html')


def menu(request):

    return render(request, 'mains/menu.html')


def rank(request):

    # for item in stk_cnt:
    #     print(item)
    return render(request, 'mains/rank.html')


def content(request):
    stk_rank = SkillStack.objects.values('name', 'stackshareLink', 'img').annotate(
        Count('posted_recruit')).order_by('-posted_recruit__count')[:20]
    # print(stk_rank[0].img)
    context = {
        'stk_rank': stk_rank,
    }
    return render(request, 'mains/content.html', context)


def content1(request):
    return render(request, 'mains/content1.html')


def insite(request):
    return render(request, 'mains/insite.html')

def filter(request, lang):
    filtered = Recruit.objects.filter(id__in=Subquery(SkillStack.objects.get(name__iexact=lang).
                posted_recruit.values('id'))).values('wants_stacks').\
                    annotate(Count("wants_stacks")).order_by('-wants_stacks__count')

    context = {
        'filtered' : filtered,
    }

    return JsonResponse(context)



# DB 생성용


def issue(request):
    URL = 'https://api.github.com/search/issues?q=language:'
    params = ['JavaScript', 'Java', 'Python', 'C', 'C#', 'C++', 'Go', 'Ruby',
              'TypeScript', 'PHP', 'Scala', 'Rust', 'Kotlin', 'Swift', 'Shell']
    langcount = []

    for param in params:
        response = requests.get(URL+param)
        issue = response.json().get('total_count')
        langcount.append(issue)
        time.sleep(7)

    print(langcount)

    issuecounting = CountIssue(
        javascript=langcount[0],
        java=langcount[1],
        python=langcount[2],
        c=langcount[3],
        csharp=langcount[4],
        cplus=langcount[5],
        go=langcount[6],
        ruby=langcount[7],
        typescript=langcount[8],
        php=langcount[9],
        scala=langcount[10],
        rust=langcount[11],
        kotlin=langcount[12],
        swift=langcount[13],
        shell=langcount[14]
    )

    issuecounting.save()
    return render(request, 'mains/insite.html')


def repository(request):
    URL = 'https://api.github.com/search/repositories?q=language:'
    params = ['JavaScript', 'Java', 'Python', 'C', 'C#', 'C++', 'Go', 'Ruby',
              'TypeScript', 'PHP', 'Scala', 'Rust', 'Kotlin', 'Swift', 'Shell']
    langcount = []

    for param in params:
        response = requests.get(URL+param)
        issue = response.json().get('total_count')
        langcount.append(issue)
        time.sleep(7)
    #print(langcount)

    repocounting = CountRepository(
        javascript=langcount[0],
        java=langcount[1],
        python=langcount[2],
        c=langcount[3],
        csharp=langcount[4],
        cplus=langcount[5],
        go=langcount[6],
        ruby=langcount[7],
        typescript=langcount[8],
        php=langcount[9],
        scala=langcount[10],
        rust=langcount[11],
        kotlin=langcount[12],
        swift=langcount[13],
        shell=langcount[14]
    )

    repocounting.save()
    return render(request, 'mains/insite.html')


def setting(request):
    issues = CountIssue.objects.all()
    javascript = []
    java = []
    python = []
    c = []
    csharp = []
    cplus = []
    go = []
    ruby = []
    typescript = []
    php = []
    scala = []
    rust = []
    kotlin = []
    swift = []
    shell = []
    date = []
    
    for issue in issues:
        javascript.append(int(issue.javascript))
        java.append(int(issue.java))
        python.append(int(issue.python))
        c.append(int(issue.c))
        csharp.append(int(issue.csharp))
        cplus.append(int(issue.cplus))
        go.append(int(issue.go))
        ruby.append(int(issue.ruby))
        typescript.append(int(issue.typescript))
        php.append(int(issue.php))
        scala.append(int(issue.scala))
        rust.append(int(issue.rust))
        kotlin.append(int(issue.kotlin))
        swift.append(int(issue.swift))
        shell.append(int(issue.shell))
        date.append(issue.date)
    # print(javascript)
    # print(java)

    # language = ['javascript', 'java', 'python', 'c', 'csharp', 'cplus', 'go', 'ruby',
    #  'typescript', 'php', 'scala', 'rust', 'kotlin', 'swift', 'shell', 'date']
    # langcount = [javascript, java, python, c, csharp, splus, go, ruby, typescript, php
    # scala, rust, kotlin, swift, shell, date]

    plt.plot(date, javascript,'rs--')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/javascriptgraph.png')

    plt.cla()
    plt.plot(date, java, 'mo--')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/javagraph.png')

    plt.cla()
    plt.plot(date, python, 'c.-')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/pythongraph.png')

    plt.cla()
    plt.plot(date, c, 'rs-')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/cgraph.png')

    plt.cla()
    plt.plot(date, csharp, 'm.-')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/csharpgraph.png')

    plt.cla()
    plt.plot(date, cplus, 'co--')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/cplusgraph.png')

    plt.cla()
    plt.plot(date, go, 'ro-')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/gograph.png')

    plt.cla()
    plt.plot(date, ruby, 'g^-.')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/rubygraph.png')

    plt.cla()
    plt.plot(date, typescript, 'yv--')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/typescriptgraph.png')

    plt.cla()
    plt.plot(date, php, 'mD:')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/phpgraph.png')

    plt.cla()
    plt.plot(date, scala, 'b*-')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/scalagraph.png')

    plt.cla()
    plt.plot(date, rust, 'r>-')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/rustgraph.png')
    
    plt.cla()
    plt.plot(date, kotlin, 'kx--')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/kotlingraph.png')

    plt.cla()
    plt.plot(date, swift, 'c_:')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/swiftgraph.png')

    plt.cla()
    plt.plot(date, shell, 'gh--')
    plt.savefig('C:/Sohottoday/LeeSin/LeeSin/mains/static/mains/images/shellgraph.png')
    return render(request, 'mains/insite.html')





# def issuepython(request):
#     URL = 'https://api.github.com/search/issues?q=language:'

#     response = requests.get(URL+'python')
#     issue = response.json().get('total_count')

#     javascript = CountIssue(python=issue)     # f'{language}'
#     javascript.save()
#     return render(request, 'mains/insite.html')
