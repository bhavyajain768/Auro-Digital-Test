import heapq as h

class OrderBook:
    def __init__(self) -> None:
        self.buy,self.sell = [],[]
    

orderBooks = []
def addOrder(book,type,price,volume,id):
    if(len(orderBooks)<book):
        while(len(orderBooks)<book):
            orderBooks.append(OrderBook())
    orderBook = orderBooks[book-1]
    if(type=="BUY"):
        n = len(orderBook.sell)
        if(n==0 or orderBook.sell[0][0]>price):
            h.heappush(orderBook.buy,(-price,volume,id))
        else:
            if(orderBook.sell[0][1]==volume):
                h.heappop(orderBook.sell)
            elif(orderBook.sell[0][1]>volume):
                orderBook.sell[0][1] -= volume
            else:
                volume -= orderBook.sell[0][1]
                h.heappop(orderBook.sell)
                addOrder(book,type,price,volume,id)

    else:
        n = len(orderBook.buy)
        if(n==0 or -orderBook.buy[0][0]<price):
            h.heappush(orderBook.sell,(price,volume,id))
        else:
            if(orderBook.buy[0][1]==volume):
                h.heappop(orderBook.buy)
            elif(orderBook.buy[0][1]>volume):
                orderBook.buy[0][1] -= volume
            else:
                volume -= orderBook.buy[0][1]
                h.heappop(orderBook.buy)
                addOrder(book,type,price,volume,id)

def deleteOrder(book,id):
    if(len(orderBooks)<book):
        return
    orderBook = orderBooks[book-1]
    for i in range(len(orderBook.buy)):
        if(orderBook[i][2]==id):
            orderBook[i] = orderBook[-1]
            orderBook.pop()
            h.heapify(orderBook)
            return
    for i in range(len(orderBook.sell)):
        if(orderBook[i][2]==id):
            orderBook[i] = orderBook[-1]
            orderBook.pop()
            h.heapify(orderBook)
            return


                