h = input("Enter Hours")
r = input("Enter Rate")
fh = float(h)
fr = float(r)
#print(fh,fr)
if fh > 40 :
    reg = fr*fh
    otp = (fh - 40.00) * (fr*0.5)
    xp = reg + otp 
else:
    xp = fh*fr
print("Pay:", xp)
