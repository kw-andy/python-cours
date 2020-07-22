def sum_pairs(pairs,k):
    counter = 0

    for i in pairs:
        print(i,"the num i is ")
        if k - i in pairs:
            print(k-i," k - i is ")
            counter += 1
    print(counter)

sum_pairs([3,5,7,10],17)    