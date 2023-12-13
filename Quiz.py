import os

# Questions
Q1 = "Is this readable? "

# Types
TorF = "True or False?: "
ABC = "A B or C: "
ABCD = "A B C or D: "
ABCDE = "A B C D or E: "
ShortResponse = "Please write a Short Response to answer this Question: "
LongResponse = "Please write a Long-form Response to answer this Question: "

# Run
Answer1 = input(Q1 + TorF)
Score = 0
if Answer1.lower() == "t" or Answer1.lower() == "true":
    Score += 1
    print("That is correct")
else:
    print("That is incorrect")

# Save
print("Score:", Score)

try:
    with open('AnswersForQuiz.txt', 'w') as file_object:
        file_object.write(f"Answer 1: {Answer1}\n")
except Exception as e:
    print(f'An error occurred: {e}')
