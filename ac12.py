math=int(input("math:Enter your marks="))
science=int(input("science:Enter your marks="))
english=int(input("english:Enter your marks="))
if math>science and math>english:
    print("you are good in maths")
elif science>math and science>english:
    print("You are good in science")
else:
    print("you are good in english")
