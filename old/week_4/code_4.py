if __name__ == "__main__":
   while True:
    print("hello leeds beckett!")
    #ask for the users name
    name = input("whats your name? ")
    print(f"nice to meet you, {name}!!!!!")
    #ask for the users age
    age = int(input("how old are you mate?"))
    #respond based on their age
    if age >= 18:
        print("you're old lol")
    else:
        print("you're pretty young tbf")
    #ask if they want to continue
    again = input("Want me to ask again? (yes/no): ").lower()
    if again != "yes":
        print("goodbye then!")
        break
    
#code works, wrote it myself. when copying from tony's examples, "#!/usr/bin/env python3" doesnt matter for code
#its there to tell the OS how to run the file when you execute it directly from the terminal
#problem: adding break at the end didnt work, telling me it was outside the loop. this was because
#i had to add "while True:" at the start so that a loop could start forever until something stops it. without adding this, there is no loop for break to exit from.
