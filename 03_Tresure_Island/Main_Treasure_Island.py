print(r'''

            ~        ~          ~            ~        ~
 ~                                  _.,-'=_.-'-._  ~        ~
         ~     ~           ~   ._.-'             '-._   ~
                      _.-':_.-'                      '-._   ~     ~
                  _.-'                                   '-._.'-._
   ~       .-'.-,'                                                '-.
           '-._                                             _.-'
 ~            
           ~      '-._         (/      /\ (           _.'-._,-'
                      '-._            /  \ )      _.-'   (o o)
 ~     ) ( ) (    ~     .-'               (     .'       ))~((  ~
      ) " ( " (        .-'                 )    '-._.,.            ~
     )  "  ("  (       '-._               /           '-._  ~ 
    )   "   (   ( ___      '-._          (                '.   ~
        "   "    |   | ~      .'          )                '-._
  ---._-|--|--|--|--/     _.-'           /  (o)(o)           _.'   ~
       \ o  o  o  o/     '-._           /    (  )           '-._-'-.
   ~~~~~~~~~~~~~~~~~         '-._      (                        _.-'
  ~          ~             ~     '-.    ) /\            _.-"._,'
                  ~              _.'   / /\ /\         '.  ~    (o o)
    (o o)              _.-'-._.-'     / /  \  \          '-._._ ))~((
    ))~(( ~        _.-'              /                         '-. ~
                .-'              .-'('-._                        '-.
 ~            _.'         _.-'-.-'~   ~  '.             _.'-.-'._  .'
     .-'=_.'-'         .-'  ~   ~   _ _.-'          _.-'     ~   '.'
  _.-'                 '-._,.-'._.-'    (o)(o)     '_   ~       ~
.'                                         \)         '-._   ~    ~
'-.- = .-'.     (o)(o)                                    '=._
          '._    (  )                                         '-.
LGB     ~    :_                                            _.-'.-' ~
     ~     ~   "._,-'.-'._    .-`-._;'-._.='._          .-'  ~
                    ~     '-_."      ~    ~   '-._:'=~_.'       ~
           ~     ~      ~        ~     ~        ~          ~    ~''')
print("Welcome to Treasure Island")
print("Your Mission is to find the treasure>")
choice = input('You are at the crossroad, where do you want to go ?" left " or " right".').lower()
if choice == "right":
    print("You have chosen the right door.")
    choice2 = input('You are at a lake , should you "wait" or "swim" ').lower()
    if choice2 == "wait":
        print("You have decided to wait")
        choice3 = input('You are at a crossroad "RED" "GREEN" "YELLOW", Which one will you pick').upper()
        if choice3 == "YELLOW":
            print("Congratulation, You have found the treasure")
        else:
            print("You have died by shock")
    else:
        print("You have drown while smimming and died")
else:
    print("You have died. ")