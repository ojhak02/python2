college={
        "name":"lamaboy",
        "dept":"IT",
        "age":"18"
        }
print("student name is " +college["name"])
print("dept name is"+college["dept"])
print(college.keys())
print(college.values())
for x in college:
         print(x+"->"+college[x])
college["gender"]="male"
print(college)
if "age" in college:
        print("yes, age is a key of college")
##del college
##print(college)

college.pop("age")
print(college)

x=("123","abc","xyz")
y=0

college=dict.fromkeys(x,y)
print(college)