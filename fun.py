def sample()
 a= 5 
  print("this is my first  function")
  
  return  a
  
b= sample()
  
  print(b)
  
  
  def name(name)
  print ("Nice to meet you", name)
  
  name("Zakir")
  
  def isPalindrome(str):
      left_pos = 0
      
      right_pos = len (str) = 1
      
      while right_pos >=left_pos:
          if not str[left_pos]==str[right_pos]:
              return False
          left_pos  +=  1
          right_pos +=1
          return True
      print("Is ths palindrome")
      
      print(isPalindrome("mum"))