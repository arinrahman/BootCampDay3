print('''                      .   `:
                        :   :  .
                     __.'_ .'   :
                _.--'     `-._.'
             .-'..     ..    `.
            : .-.    .--.`.    :
           : :  :   :   :       :
           : :`;;   :`; ;       :
           `.`O;'   `O;.'       :
          .' .---.  .--.        ;
  .      :  '._   :'           ;
  ::     :   .-`-.;       .  .'
 .':     `.   ``` `.      :-'
:  :       `-.__   ._   _.'
 : ;           :    ;```
  : `.    _.-.' .  ``-._
   :  `.-'   : :        `-.
    :      _.: `  `-._     `,
     `._.-'   ;     `.`-.   ;_,  _.,
              :       `.:  ;' ;-'  ;
             :         ``.___.'   :
             :             ;_..--'
             `.            ;
               `-.__   ...'
                   : :  :
              jgs  :-:__;
                   : :  :
        .-~~~--..__: :  :___..---..
      .'.'           :             `,
     :,'             :            `; ;
     `:           _.'`._           :,'
       `~~~'----''     `'-.____....'
       ''')
print("Welcome to Looney Tunes Island!\nYour mission is to find Tweety bird!\nYou are at a crossroad. Where do you want to go?\n")
input_1= input("    Type L for left and R for right.\n")
if input_1== "L" or input_1=="l":
    input_2 = input("    Type S to swim and W to wait .\n")
    if input_2== "W" or input_2== "w":
        input_3 = input("    Type R to pick the red door, Y to pick the yellow door or B to pick the blue door.\n")
        if input_3 == "Y" or input_3 == "y":
            print("You found Tweety Bird! Way to go!")
        if input_3 == "R" or input_3 == "r":
            print("Game over! Try again.")
        if input_3 == "B" or input_3 == "b":
            print("Game over! Try again.")

    else:
        print("Game over! Try again.")

else:
    print("Game over! Try again.")

