function calcPrice(numSeats)
	price = numSeats*15
	if seats >= 3 then
		price = price - 10
	endif
	return price
endfunction

tickets = 1
total = 0
while ticket != 0
	tickets = input("Enter the number of tickets")
	if tickets != 0 then
		total = total + calcPrice(tickets)
	end if
end while

print("The total price is " + total)
