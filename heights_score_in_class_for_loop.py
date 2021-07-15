student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

heighst_score = student_scores[0]
for score in student_scores:
  if score > heighst_score:
    heighst_score = score
print(f"The heighst score in the class is {heighst_score}") 
