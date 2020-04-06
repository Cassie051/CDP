import time, profile, data
import lab1, lab2, lab2pmtn, lab3

Srows = data.Rows.copy()
Rrows = data.Rows.copy()
RQrows = data.Rows.copy()
Crows = data.Rows.copy()

def millis(t):
    t = t * 1000
    multiplier = 10 ** 3
    return int(t * multiplier) / multiplier

def main():
    # print("Normal calculate:", calculate(Crows))
    start = time.time()
    print("\nRsort calculate:", lab1.Rsort(Rrows))
    end = time.time()
    print(millis(end - start))
    start = time.time()
    print("\nRQsort calculate:", lab1.RQsort(RQrows))
    end = time.time()
    print(millis(end - start))

    start = time.time()
    print("\nNormal Schrage calculate:", lab1.calculate(lab2.schrage(Srows)))
    end = time.time()
    print(millis(end - start))
    # print("Queue Schrage calculate:", lab1.calculate(lab2.schrageOnQueue(Srows)))

    start = time.time()
    print("\nNormal SchragePmtn calculate:", lab2pmtn.schragePmtn(Srows))
    end = time.time()
    print(millis(end - start))
    # print("Queue SchragePmtn calculate:", lab2pmtn.schragePmtnOnQueue(Srows))

    start = time.time()
    print("\nCarlier calculate:", lab3.carlier(Crows))
    end = time.time()
    print(millis(end - start))

main()

# 641 ,1267, 1492, 3070, 6398