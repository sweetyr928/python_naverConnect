astr = 'Hello connect'
gotr = 'good'
detr = 'night'

try:
    istr=int(istr)
    gotr='have'
    print(istr)
except:
    try:
        print(gotr)
    except:
        print(detr)
