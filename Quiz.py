Q1 = "Is this readable? "
Awnser = input(Q1 + "True or False?: ")
Score = 0
if Awnser == "t" or Awnser == "T" or Awnser == "True" or Awnser == "true" or Awnser == "TrUe" or Awnser == "tRuE" or Awnser == "TRUE":
	Score = Score+1
	print("That is correct")
else:
	Score = Score-1
	print("That is incorrect")

print(Score)