x=int(input("enter sale amount:"))
if x<=5000:
    discount=5/100 * x
    print("discount:",end=" " ); print(discount)
    Netpay= x-discount
    print("Net pay:", end="");print(Netpay)
if x>5000 and x<=10000:
    discount=10/100*x
    print("discount:", end=" " );print(discount)
    Netpay= x-discount
    print("Net pay:", end="");print(Netpay)
if x>10000 and x<=15000:
    discount=20/100*x
    print("discount:", end=" " );print(discount)
    Netpay= x-discount
    print("Net pay:", end="");print(Netpay)



    