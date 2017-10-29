count=0
for p1 in range(0,201):
    for p2 in range(0,201-p1,2):
       for p5 in range(0,201-(p1 + p2),5):
           for p10 in range(0,201-(p1 + p2 + p5),10):
               for p20 in range(0,201-(p1 + p2 + p5 + p10),20):
                   for p50 in range(0,201-(p1 + p2 + p5 + p10 + p20),50):
                       for p100 in range(0,201-(p1 + p2 + p5 + p10 + p20 + p50),100):
                           for p200 in range(0,201-(p1 + p2 + p5 + p10 + p20 + p50 + p100), 200):
                               if p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 == 200:
                                   count += 1
print("Total ways : ",count)                                
