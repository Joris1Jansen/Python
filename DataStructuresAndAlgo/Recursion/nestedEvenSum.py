def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum
    

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup",
      "som": 4,
    }
  }
}

print(nestedEvenSum(obj1))