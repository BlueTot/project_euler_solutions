#The sequence 

sum = 0

seq = []

for i in range(0, 12):
    x = 0
    x = 1-i+i**2-i**3+i**4-i**5+i**6-i**7+i**8-i**9+i**10
    seq.append(x)

print(seq)

diff1 = []
diff2 = []
diff3 = []
diff4 = []
diff5 = []
diff6 = []
diff7 = []
diff8 = []
diff9 = []
diff10=[]

for i in range(0,10):
    diff1.append(seq[i+1]-seq[i])


for i in range(0,len(diff1)-1):
                   diff2.append(diff1[i+1]-diff1[i])

for i in range(0,len(diff2)-1):
                   diff3.append(diff2[i+1]-diff2[i])

for i in range(0,len(diff3)-1):
                   diff4.append(diff3[i+1]-diff3[i])

                   
for i in range(0,len(diff4)-1):
                   diff5.append(diff4[i+1]-diff4[i])

for i in range(0,len(diff5)-1):
                   diff6.append(diff5[i+1]-diff5[i])


for i in range(0,len(diff6)-1):
                   diff7.append(diff6[i+1]-diff6[i])


for i in range(0,len(diff7)-1):
                   diff8.append(diff7[i+1]-diff7[i])


for i in range(0,len(diff8)-1):
                   diff9.append(diff8[i+1]-diff8[i])

for i in range(0,len(diff9)-1):
                   diff10.append(diff9[i+1]-diff9[i])



sum += (seq[1] +diff1[0])

sum += (seq[2]+diff1[1])

sum +=(seq[3]+diff1[2]+diff2[1])

sum += (seq[4]+diff1[3]+diff2[2]+diff3[1])

sum += (seq[5]+diff1[4]+diff2[3]+diff3[2]+diff4[1])

sum += (seq[6]+diff1[5]+diff2[4]+diff3[3]+diff4[2]+diff5[1])

sum += (seq[7]+diff1[6]+diff2[5]+diff3[4]+diff4[3]+diff5[2]+diff6[1])

sum +=(seq[8]+diff1[7]+diff2[6]+diff3[5]+diff4[4]+diff5[3]+diff6[2]+diff7[1])

sum += (seq[9]+diff1[8]+diff2[7]+diff3[6]+diff4[5]+diff5[4]+diff6[3]+diff7[2]+diff8[1])

sum += (seq[10]+diff1[9]+diff2[8]+diff3[7]+diff4[6]+diff5[5]+diff6[4]+diff7[3]+diff8[2]+diff9[1])

print(diff1)

print(seq[3]+diff1[2]+diff2[1])
print(sum)
