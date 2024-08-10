while (True):
  print ("calculator")
  print ("\033[0;31m[\033[1;37m1\033[0;31m]\033[0m+")
  print ("\033[0;31m[\033[1;37m2\033[0;31m]\033[0m-")
  print ("\033[0;31m[\033[1;37m3\033[0;31m]\033[0m×")
  print("\033[0;31m[\033[1;37m4\033[0;31m]\033[0m/")
  option=int(input("1,2,3,4:") )
  if(option in [1,2,3,4]):
    numb1=int(input ("\033[0;32menter numb:\033[0;34m") )
    numb2=int(input("\033[0;32mEnter  numb:\033[0;34m") )

    if (option == 1):
      result= numb1 +numb2
    elif (option ==2):
      result= numb1 - numb2
    elif (option == 3):
      result= numb1 * numb2
    elif (option == 4):
      result= numb1 / numb2
    else:
      print("Enter again")

    print(" \033[1;33mthe results is {}".format(result) )
