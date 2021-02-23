def speedup(cspeed):
    fspeed = int(input('What speed do you want to get to?(mps) '))
    if fspeed > cspeed:
        timec = int(input('How fast do you want to accelerate?(seconds) '))
        timet = int(input('How long do you want to travel at this speed?(seconds) '))
        acc = acceleration(cspeed, fspeed, timec)
        print(f"You've travelled  {Distance(cspeed, fspeed, acc, timec, timet)} (m) ")
    return fspeed

def brake(cspeed):
    fspeed = int(input('What speed do you want to get to?(mps) '))
    if fspeed < cspeed:
        print(f"You're travelling at  {fspeed} (m) ")
    return fspeed

def Distance(cspeed, fspeed, acceleration, timec, timet):
    d1 = fspeed*timet
    d2 = timec*cspeed+(0.5*acceleration*(timec)**2)
    return d1+d2

def acceleration(currentspeed,finalspeed,time):
    return (finalspeed-currentspeed)/(time)

def main():
    print('You are currently stationary.')
    cspeed = 0
    t = True
    while t:
        cam = input('Do you want to speed up, brake, reverse or exit game.(A/B/R/E) ').lower()
        if cam == 'a':
            cspeed=speedup(cspeed)
        elif cam == 'b':
            cspeed=brake(cspeed)
        elif cam == 'r':
            if cspeed == 0:
                fspeed = int(input('How fast do you want to reverse?(mps) '))
                print(f"You're reversing at  -{fspeed} (m) ")
                cspeed = -fspeed
            else:
                print('You need to brake first')
        elif cam == 'e':
            t = False
        else:
             print('Invalid command try again ')
    return
main()