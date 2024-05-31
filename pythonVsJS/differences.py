# Lab 1

#Javascript code
#const getName = () => {
#    let name = prompt("What is your name?");
#    return name;
#}

#Python code
user_input = input("What is your name? ")
print(user_input)

#Javascript code
#const reverseIt = () => {
#    let string = ("a man, a plan, a canal, frenemies!");

#    let reverse = "";

#    for (let i=0: i < string.length; i++) {
#        reverse += string[string.length - (i + 1)];
#    };

#    alert(reverse);
#};

#Python code
string = "a man, a plan, a canal, frenemies!"
reverse = ""

for i in range(len(string)):
    reverse += string[len(string) - (i + 1)]

print(reverse)

#Javascript code
#const swapEm = () => {
#    let a = 10;
#    let b = 30;
#    let temp;

#    temp = b;
#    b = a;
#    a = temp;

# alert("a is now " + a + ", and b is now " + b);
#};

#Python code
a = 10
b = 30
temp = 0

temp = b
b = a
a = temp

print("a is now " + str(a) + ", and b is now " + str(b))

#Javascript code
#const multiplyArray = (ary) => {
#  if (ary.length == 0) { return 1; };

#  let total = 1;
#  // let total = ary[0];

#  for (let i=0; i < ary.length; i++) {
#    total = total * ary[i];
#  };

#  return total;
#};

#Python code
def multiplyArray(ary):
    if len(ary) == 0:
        return 1

    total = 1

    for i in range(len(ary)):
        total = total * ary[i]

    return total

print(multiplyArray([1, 2, 3, 4]))

#Javascript code
#const fizzbuzzer = (x) => {
#  if( x%(3*5) == 0 ) {
#    return 'fizzbuzz'
#  } else if( x%3 == 0 ) {
#    return 'fizz'
#  } else if ( x%5 == 0 ) {
#    return 'buzz'
#  } else {
#    return 'archer'
#  }
#};

#Python code
def fizzbuzzer(x):
    if x % (3 * 5) == 0:
        return 'fizzbuzz'
    elif x % 3 == 0:
        return 'fizz'
    elif x % 5 == 0:
        return 'buzz'
    else:
        return 'archer'
    
print(fizzbuzzer(15))
print(fizzbuzzer(3))
print(fizzbuzzer(5))
print(fizzbuzzer(7))

#Javascript code
#const nthFibonacciNumber = () => {
#  let fibs = [1, 1];
#  let num = prompt("which fibonacci number do you want?");

#  while (fibs.length < parseInt(num)) {
#    let length = fibs.length;
#    let nextFib = fibs[length - 2] + fibs[length - 1];
#    fibs.push(nextFib);
#  }

#  alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
#};

#Python code
def nthFibonacciNumber():
    fibs = [1, 1]
    num = input("which fibonacci number do you want? ")

    while len(fibs) < int(num):
        length = len(fibs)
        nextFib = fibs[length - 2] + fibs[length - 1]
        fibs.append(nextFib)

    print(str(fibs[len(fibs) - 1]) + " is the fibonacci number at position " + num)

nthFibonacciNumber()

#Javascript code
#const searchArray = (array, value) => {
#  for(let i = 0; i < array.length-1; i++) {
#    if(array[i] == value) {
#      return true;
#      break;
#    }
#  }
#  return -1;
#};

#Python code
def searchArray(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return True
            break
    return -1

print(searchArray([1, 2, 3, 4, 5], 3))
print(searchArray([1, 2, 3, 4, 5], 6))

#Javascript code
#const isPalindrome = (str) => {
#  for(let i = 0; i < str.length/2; i++){
#    if(str[i] != str[str.length-i-1]){
#      return false;
#      break;
#    }
#  }
#  return true;
#};

#Python code
def isPalindrome(str):
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
            break
    return True

print(isPalindrome("racecar"))
print(isPalindrome("hello"))

#Javascript code
#const hasDupes = (arr) => {
#  let obj = {};
#  for (let i = 0; i < arr.length; i++) {
#    if(obj[arr[i]]) {
#      return true;
#    } else {
#      obj[arr[i]] = true;
#    }
#  }
#  return false;
#};

#Python code
def hasDupes(arr):
    obj = {}
    for i in range(len(arr)):
        if obj.get(arr[i]):
            return True
        else:
            obj[arr[i]] = True
    return False

print(hasDupes([1, 2, 3, 4, 5]))
print(hasDupes([1, 2, 3, 4, 5, 1]))
