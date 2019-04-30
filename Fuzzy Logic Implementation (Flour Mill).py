q=float(input("Enter quantity "))
q_value=[]
if(q<0):
    q_value.append(0)
elif(q>=0 and q<=20):
    q_value.append((q-0)/(20-0))
elif(q>20 and q<=40):
    q_value.append((40-q)/(40-20))
elif(q>40):
    q_value.append(0)

if(q<30):
    q_value.append(0)
elif(q>=30 and q<=50):
    q_value.append((q-30)/(50-30))
elif(q>50 and q<=80):
    q_value.append((80-q)/(80-50))
elif(q>80):
    q_value.append(0)

if(q<65):
    q_value.append(0)
elif(q>=65 and q<=85):
    q_value.append((q-65)/(85-65))
elif(q>85 and q<=100):
    q_value.append((100-q)/(100-85))
elif(q>100):
    q_value.append(0)



m=float(input("Enter material type "))
m_value=[]
if(m<0):
    m_value.append(0)
elif(m>=0 and m<=20):
    m_value.append((m-0)/(20-0))
elif(m>20 and m<=45):
    m_value.append((45-m)/(45-20))
elif(m>45):
    m_value.append(0)

if(m<40):
    m_value.append(0)
elif(m>=40 and m<=55):
    m_value.append((m-40)/(55-40))
elif(m>55 and m<=75):
    m_value.append((75-m)/(75-55))
elif(m>75):
    m_value.append(0)

if(m<60):
    m_value.append(0)
elif(m>=60 and m<=80):
    m_value.append((m-60)/(80-60))
elif(m>80 and m<=100):
    m_value.append((100-m)/(100-80))
elif(m>100):
    m_value.append(0)

print(q_value)
print(m_value)

slow=[]
intm=[]
fast=[]

slow.append(min(q_value[0],m_value[0]))
slow.append(min(q_value[0],m_value[1]))

intm.append(min(q_value[0],m_value[2]))
intm.append(min(q_value[1],m_value[0]))
intm.append(min(q_value[1],m_value[1]))
intm.append(min(q_value[2],m_value[0]))

fast.append(min(q_value[1],m_value[2]))
fast.append(min(q_value[2],m_value[1]))
fast.append(min(q_value[2],m_value[2]))


slow_max=max(slow)
intm_max=max(intm)
fast_max=max(fast)

center_of_gravity = slow_max*(0+5+10+15+20+25+30)
#print(center_of_gravity)
center_of_gravity+= intm_max*(35+40+45+50+55+60+65)
#print(center_of_gravity)

center_of_gravity+= fast_max*(70+75+80+85+90+95+100)
#print(center_of_gravity)

center_of_gravity/=((slow_max*7)+(intm_max*7)+(fast_max*7))

print(center_of_gravity)





