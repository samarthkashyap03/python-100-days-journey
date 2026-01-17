auction_set={}
print("Welcome to the Auction!!")
while True:
    name=input("Enter your name:")
    bid=int(input("Enter bid value:"))
    if bid in auction_set.values():
        print("Bid value already present, change the bid")
        continue
    auction_set[name]=bid
    if input("Is there another person to do the bid, Y or N:").lower()=="y":
        continue
    else:
        break
max_bid=max(auction_set,key=auction_set.get)
print(f"The highest bidder is {max_bid} with bid of {auction_set[max_bid]}")

