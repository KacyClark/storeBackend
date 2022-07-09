

def start_tests():
    print("--------List Tests--------")

    nums = [1,2,3,4,5,6]
    # read from the list
    print (nums[0])
    print (nums[1])


    # add elements to a list
    nums.append(9)
    print(nums)


    # for loop
    for n in nums:
        print(n)


    # for loop from 0 to 20
    for number in range(0,21):
        print(number)


    def test1():
        print("test 1")   

        ints = [123,3,23,6475,58,89,45,34,87,34,-12,23,123,-23,-123,0,123,0,-29,10]
        for n in ints:
            if n < 50:
            print(n)

        count = 0
        for n in ints:
            if n < 50:
                print(n)
                count += 1
        print("There are (count) numbers lower than 50")

        count = 0
        sum = 0
        sum_greater_than = 0
        zeros = 0
        for n in ints:
            sum += n
          
            if n >= 0:
                sum_greater_than += n
            
            if n == 0:
               zeros += 1            


        # 1 print numbers lower than 50
        # 2 count how many numbers are lower than 50
        # 3 the sum of all numbers
        # 4 the sum of all numbers greater than zero
        # 5 count how many zeros there are

        def test2():
            print("-------TEST 2-------")

users = [
    {
    "gender":"F",
    "name": "Louis",
    "color": "Green"
    },
    {
    "gender":"M",
    "name": "Manuel",
    "color": "Gray"
    },
    {
    "gender":"F",
    "name": "Rossy",
    "color": "Pink"
     },
    {
    "gender":"F",
    "name": "Genny",
    "color": "pink"
    },
    {
    "gender":"M",
    "name": "Roman",
    "color": "Purple"
    },
    {
    "gender":"m",
    "name": "John",
    "color": "Pink"
    },
    {
    "gender":"F",
    "name": "Susan",
    "color": "Black"
    }
]            
for user in users:
    print(user["name"])
    print(len(users))

for user in users:
    if user["color"].lower() == "pink":
        print(user["name"])    


            # 1 print all the names
            # 2 print how many users there are in the list
            # 3 print the names of users who like pink, any version     

def test3()
    print("---------TEST 3---------")

    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23,123,-23,-123,0,123,0,-29,10]

    # find the most expensive product price
    # solution = prices[0]
    # for price in prices
    # if price is greater than your solution
    # your final solution is equal to price

solution = prices[0]
for price in prices:
    if price > solution:
        solution = price


    start_tests()
    test1()
    test2()
    test3()