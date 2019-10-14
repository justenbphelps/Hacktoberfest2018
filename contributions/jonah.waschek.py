# This is my short program about me and why I choose to become a programmer.

def intro_func(name,age):

    print("Hello Hacktoberfest 2019!");
    print("My name is: " + name + ", and I am: " + age + " years old.");
    
def job_func():
    print("I currently work as a web developer for the past year, doing mostly backend"); 
    print("I became a programmer because I enjoy solving problems and always learning new things\n");

# Below is one of my favorite basic programs, but can handle custom values/words
def fizzBuzz(word1 = "Fizz", word2 = "Buzz", num1 = 3, num2 = 5, num3 = 7, begin = 1, end = 25):
    print("-------------------------------------------------------------------------");
    print("("+word1+") will print out if current value is divisible by: "+str(num1));
    print("("+word2+") will print out if current value is divisible by: "+str(num2));
    print("("+word1+word2+") will print out if current value is divisible by: "+str(num3));
    print("-------------------------------------------------------------------------");
    
    for i in range(begin,end+1):
        if(i % num3 == 0):
            print(word1+word2);
        elif(i % num1 == 0):
            print(word1);
        elif(i % num2 == 0):
            print(word2);
        else:
            print(i);
    print("-------------------------------------------------------------------------");

intro_func("Jonah Waschek","24");
job_func();

# Different values can be bassed to fizzBuzz to change results if needed.
# examble -> 
# fizzBuzz("foo","bar",2,3,4,1,50);

fizzBuzz();

