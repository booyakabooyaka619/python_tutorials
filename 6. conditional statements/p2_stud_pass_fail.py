sub1 = int(input("Enter marks of subject 1 : "))
sub2 = int(input("Enter marks of subject 2 : "))
sub3 = int(input("Enter marks of subject 3 : "))
sub4 = int(input("Enter marks of subject 4 : "))

marks = (100 * (sub1 + sub2 + sub3 + sub4))/400

if(marks<40 or sub1<33 or sub2<33 or sub3<33 or sub4<33):
    print("You have failed with the score of", marks)

else:
    print("You have passed with a score of",  marks)