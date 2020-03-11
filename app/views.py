from django.shortcuts import render
import random
p1 = 0
p2 = 0
r_1 = 0
r_2 = 0
count_1 = 0
count_2 = 0
def function(request):
    return render(request,"index.html",{"p1":p1,"p2":p2})

def player1(request):
    global p1
    global p2
    global r_1
    global r_2
    global count_1
    global count_2
    if p1 == 99 or p1 <= 99:
        min = 1
        max = 6
        r1 = random.randint(min, max)
        global r_1
        r_1 = r1
        p1 = p1 + r1
        count_1 = count_1+1
        return render(request, "index.html", {"p1": p1, "r1": r1, "p2": p2, "r2": r_2,"c1":count_1,"c2":count_2})
    else:
        p1 = 0
        p2 = 0
        r_1 = 0
        r_2 = 0
        count_1 = 0
        count_2 = 0
        return render(request,"index.html",{"message":"win1"})

def player2(request):
    global p2
    global p1
    global r_1
    global r_2
    global count_2
    global count_1
    if p2 == 99 or p2 <= 99:
        min = 1
        max = 6
        r2 = random.randint(min, max)
        global r_2
        r_2 = r2
        p2 = p2 + r2
        count_2 = count_2+1
        return render(request, "index.html", {"p2": p2, "r2": r2, "p1": p1, "r1": r_1,"c2":count_2,"c1":count_1})
    else:
        p1 = 0
        p2 = 0
        r_1 = 0
        r_2 = 0
        count_2 = 0
        count_1 = 0
        return render(request, "index.html", {"message": "win2"})