def Best_Time_to_Buy_and_Sell_Stock(prices):
    res = 0
    for i in range(len(prices)):
        j = i+1
        while j < len(prices):
            if prices[i] > prices[j]:
                break
            res = max(res,prices[j]-prices[i])
            j+=1
    return res

prices = [10,1,5,6,7,1]
print(Best_Time_to_Buy_and_Sell_Stock(prices))