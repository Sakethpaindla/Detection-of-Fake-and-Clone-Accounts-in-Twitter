
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Count,Subquery
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import clone_accounts_model,clone1_accounts_model,ClientRegister_Model,review_Model,recommend_Model,tweet_accuracy_model,fake_accounts_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            tweet_accuracy_model.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = clone_accounts_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=clone_accounts_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_Account(request): # Search
    if request.method == "POST":
        kword = request.POST.get('keyword')
        obj = clone_accounts_model.objects.all().filter(Q(uname__contains=kword) | Q(names__contains=kword))
        return render(request, 'SProvider/Search_Account.html', {'objs': obj})
    return render(request, 'SProvider/Search_Account.html')

def View_Fake_Account(request): # Using SVM
    atype='Fake'

    obj1 = clone_accounts_model.objects.values('uname',
'dob',
'gender',
'address',
'location',
'mailid',
'mobile_no',
'names',
'tweet_desc',
'tweet_loc',
'tweet_date',
'score'
)

    fake_accounts_model.objects.all().delete();
    for t in obj1:
        uname = t['uname']
        dob = t['dob']
        gender= t['gender']
        address= t['address']
        location= t['location']
        emailid= t['mailid']
        mobile_no= t['mobile_no']
        names= t['names']
        tweet_desc= t['tweet_desc']
        tweet_loc= t['tweet_loc']
        tweet_date= t['tweet_date']
        score= t['score']

        if location!=tweet_loc:
           fake_accounts_model.objects.create(uname=uname,dob = dob,gender = gender,address = address,location = location,mailid=emailid,mobile_no=mobile_no,names =names,tweet_desc =tweet_desc,tweet_loc =tweet_loc,tweet_date =tweet_date,score=score)

    obj2 = fake_accounts_model.objects.all()

    count=obj2.count()
    count1=obj1.count()
    accuracy=count/count1

    if accuracy !=0:
          tweet_accuracy_model.objects.create(names=atype,accuracy=accuracy)


    return render(request, 'SProvider/View_Fake_Account.html', {'objs': obj2,'count':accuracy})


def View_Clone_Account(request): # Positive # Using SVM
    atype = 'Clone'
    obj1=''
    kword=''
    obj2 = ''
    ratio=''
    if request.method == "POST":
        kword = request.POST.get('keyword')
        obj1 = clone_accounts_model.objects.values('uname',
                                               'dob',
                                               'gender',
                                               'address',
                                               'location',
                                               'mailid',
                                               'mobile_no',
                                               'names',
                                               'tweet_desc',
                                               'tweet_loc',
                                               'tweet_date',
                                               'score'
                                               )
        count=0
        clone1_accounts_model.objects.all().delete();
        for t in obj1:
            uname = t['uname']
            dob = t['dob']
            gender = t['gender']
            address = t['address']
            location = t['location']
            emailid = t['mailid']
            mobile_no = t['mobile_no']
            names = t['names']
            tweet_desc = t['tweet_desc']
            tweet_loc = t['tweet_loc']
            tweet_date = t['tweet_date']
            score = t['score']

            if uname == kword:
                count=count+1
                if(count>1):
                  clone1_accounts_model.objects.create(uname=uname, dob=dob, gender=gender, address=address, location=location,mailid=emailid, mobile_no=mobile_no, names=names, tweet_desc=tweet_desc,tweet_loc=tweet_loc, tweet_date=tweet_date, score=score)

        obj2 = clone1_accounts_model.objects.all()
        obj1 = clone_accounts_model.objects.all()
        count = obj2.count()
        count1 = obj1.count()
        ratio = count / count1
        if ratio != 0:
             tweet_accuracy_model.objects.create(names=atype, accuracy=ratio)

    return render(request, 'SProvider/View_Clone_Account.html', {'objs': obj2,'count':ratio})


def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = clone_accounts_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = clone_accounts_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = clone_accounts_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def charts(request,chart_type):
    chart1 = tweet_accuracy_model.objects.values('names').annotate(dcount=Avg('accuracy'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def View_TweetDataSets_Details(request):
    obj = clone_accounts_model.objects.all()
    return render(request, 'SProvider/View_TweetDataSets_Details.html', {'list_objects': obj})

def View_Account_Ratio(request):
    obj = tweet_accuracy_model.objects.all()
    return render(request, 'SProvider/View_Account_Ratio.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts = clone_accounts_model.objects.values('names').annotate(dcount=Avg('score'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})






