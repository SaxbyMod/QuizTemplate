import os
# Questions
Q1 = "Is this readable? "

# Types
TorF = "True or False?: "
ABC = "A B or C: "
ABCD = "A B C or D: "
ABCDE = "A B C D or E: "
ShortResponse = "Please write a Short Response to awnser this Question: "
LongResponse = "Please write a Long form Response to awnser this Question: "

# Run
Awnser1 = input(Q1 + TorF)
Score = 0
if Awnser1 == "t" or Awnser1 == "T" or Awnser1 == "True" or Awnser1 == "true" or Awnser1 == "TrUe" or Awnser1 == "tRuE" or Awnser1 == "TRUE":
	Score = Score+1
	print("That is correct")
else:
	print("That is incorrect")

# Save

print(Score)
try:
    os.mknod('AwnsersForQuiz.txt')
except FileExistsError as e:
    print(f'An error occurred: {e}')
file_object = open(AwnsersForQuiz.txt, w)
write(Awnser1)
file_object.close()
