import hashlib
import datetime

#current date time in string now
now = datetime.datetime.now()
now=now.strftime("%I:%M%S%p %B %d %Y")
print("Current date-time is: ")
print(now)

#hash of 'now' is stored in 'hash
hash=hashlib.sha256(now.encode('utf-8'))
print("Hash of Current date-time is: ")
print(hash.digest())

#4 digit otp
otp= int(hash.hexdigest(), 16) % (10 ** 4)
print("OTP generated from hash is: ")
print(otp)


otpInput=int(input("Please Input OTP: "))
if(int(hash.hexdigest(), 16) % (10 ** 4)==otpInput):
	print("Verified!")
else:
	print("Wrong OTP Entered.")
