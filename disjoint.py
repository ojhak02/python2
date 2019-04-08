x={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
z=x.isdisjoint(y)
print(z)

x={"a","b","c"}
y={"f","e","d","c","b","a"}
z=x.issubset(y)
print(z)

x={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
x.intersection_update(y)
print(x)

x={"a","b","c"}
z=x.issuperset(y)
print(z)

x={"Apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.symmetric_difference(y)
print(z)

x={"apple  ","banana","cherry"}
y={"google","microsoft","apple"}
z=x.union(y)
print(z)

a=[]
b={}
c=()
print(type(a))
print(type(b))
print(type(c))

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


college.pop("age")
print(college)

x=("123","abc","xyz")
y=0

college=dict.fromkeys(x,y)
print(college)


x=5
if x%2==0:
        print("even")
else:
    print("odd")










         
