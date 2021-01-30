def solution(a,b):
    answer=""
    if a>=2:
        b+=31 #1월
        if a>=3:
            b+=29#2월
            if a>=4:
                b+=31#3월
                if a>=5:
                    b+=30
                    if a>=6:
                        b+=31
                        if a>=7:
                            b+=30
                            if a>=8:
                                b+=31
                                if a>=9:
                                    b+=31
                                    if a>=10:
                                        b+=30
                                        if a>=11:
                                            b+=31
                                            if a==12:
                                                b+=30
    b=b%7

    if b==1:answer="FRI"
    elif b==2:answer="SAT"
    elif b==3:answer="SUN"
    elif b==4:answer="MON"
    elif b==5:answer="TUE"
    elif b==6:answer="WED"
    else:answer="THU"
    return answer


def getDAYname(a,b):
    months= [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return days[(sum(months[:a-1])+b-1)%7]

print(getDAYname(5,24))