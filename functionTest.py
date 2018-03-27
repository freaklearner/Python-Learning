def my_function():
    print("this is my function");


my_function();


def func_with_args(username,greeting):
    print("Welcome %s, %s" % (username,greeting));

func_with_args("shubham","greetings..!");


def sum(a,b):
    return a+b;

print("Sum of 5 and 6: %d"% (sum(5,6)));


def list_benefits():
    str = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return str;

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit;

list_coll = list_benefits();
for x in list_coll:
    print(build_sentence(x));
