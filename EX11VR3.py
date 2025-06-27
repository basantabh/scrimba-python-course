#It's...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
# Adventure Game - Store Shopping

grocery = {
    'bread': 10,
    'cheese': 15,
    'wine': 50
}
botanical_nursery = {
    'rose': 5,
    'herbs': 8,
    'magic beans': 100
}
farmers_market = {
    'apple': 2,
    'carrot': 1,
    'potato': 3
}
freelancers = {
    '1brian': 700,
    '2black knight': 200,
    '3biccus diccus': 1000,
    '4grim reaper': 5000,
    '5minstrel': -150,
    '6minstrel': -150,
    '7god': 1000000,
    '8nordic': 2000,
    '9mage': 5000,
    '01ze germane': 1000,
}
antiques = {
    'french castle': 400,
    'wooden grail': 3,
    'scythe': 1500,
    'catapult': 75,
    'german joke': 5,
    'spear': 100,
    'axe': 200,
    'peace': -2000,
    'rock': 10000,
    'healing potion': 200,
    'body armor': 2000,
}
pet_shop = {
    'blue parrot': 100,
    'white rabbit': 50,
    'newt': 20,
    'wolf': 250,
    'dragon': 1000,
    'serpent': 500
}

stores = [ 
'1-Freelancers', 
'2-Antiques', 
'3-Pet Shop', 
'4-Grocery', 
'5-Botanical Nursery', 
'6-Farmers Market',
]
o1=['1-attacke ze germanz', 
    '2-run away from the village',
    '3-cower in fear in your home and wait it out',
    '4-play dead beside other corpses',
    '5-thry zo ally withz ze germanz '
]

o2=[]
#ALREADY GIVEN INSTRUCTIONS BELOW:

#create an empty shopping cart
gold=10000
prepack="healing potion"
cart = [f"{gold},{prepack}"]
shop_names = ["Freelancers", "Antiques", "Pet Shop", "Grocery", "Botanical Nursery", "Farmers Market"]
shop_dicts = [freelancers, antiques, pet_shop, grocery, botanical_nursery, farmers_market]


game_stat=input("Shall we begin our adventure?:y/n")
if (game_stat=="y"):
    uid=input("Enter chracter name:")
    print(f"""Sir {uid}! Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, 
    and probably some good looking girl or boy you want to marry. All prices in are gold pieces,get a buddy to help and battle chop chop!! ze germanz are coming!
    PRESS 'i' TO CHECK INVENTORY""")
    user_input=input()
    if (user_input=='i'):
        print(f"you have {gold}. gold")
        shop_usin=input("Do you want to go to shops?y/n")
        if shop_usin=='y':
            print(f"""Your village has six shops that you can see! examine the shop?
            PRESS 'v' TO VEIW SHOPS.""")
            shop_usin2=input()
            if (shop_usin2=='v'):
                # Main shop loop - integrated with manual navigation
                while True:
                    print(f"""THE SHOPS YOU SEE ARE:
                    {stores}
                    WHICH SHOP WILL YOU VISIT?(1,2,3,4,5,6) or '//' to go back or 'auto' for auto-shop:""")
                    shop_usin3=input()
                    
                    if shop_usin3 == '//':
                        break
                        # Auto shop loop - visits all shops automatically
                        #paste
                            # Check if item exists in shop
                            if buy_item in shop:
                                price = shop[buy_item]
                                if gold >= price and price > 0:
                                    cart.update({buy_item: shop.pop(buy_item)})
                                    gold -= price
                                    print(f"You bought {buy_item} for {price} gold!")
                                elif price < 0:
                                    cart.update({buy_item: shop.pop(buy_item)})
                                    gold += abs(price)
                                    print(f"You took {buy_item} and gained {abs(price)} gold!")
                                else:
                                    print(f"Not enough gold! {buy_item} costs {price} but you only have {gold}")
                            else:
                                print(f"Item '{buy_item}' not found in {shop_names[i]}!")
                                print("Exiting shop...")
                                buy_items = ", ".join(list(cart.keys()))
                                print(f'You Purchased: {buy_items}')
                                print(f'Gold remaining: {gold}')
                                print("Have a nice day of mayhem!")
                                break
                        
                    elif (shop_usin3=='1'):
                        print(f"""{freelancers}
                        PRESS ITEM KEY TO BUY """)
                        shop_usin4=input()
                        if(shop_usin4=='1'):
                            print(f"""You have freelanced brian!
                            You have {gold-700} gold
                            PRESS 'i' TO VIEW INVENTORY.     
                            PRESS'bttl' TO BATTLE ZE GERMANZ
                            """)
                            cart.append('brian')
                            gold -= 700
                            bttl1=input()
                            if(bttl1==bttl):
                                print(f"""You used brain in the battle......
                                as an meatshield.You used the element of suprise on ze germanz.
                                You defeated ze germanz and now,you're the village king,you also got an refund.
                                YOU WON!Thanks for playing.""")
                                break
                            elif(bttl1==bttl):
                                print(f"""INVENTORY:
                                {cart}""")
                            
                        elif(shop_usin4=='2'):
                            print(f"""You have freelanced black knight!
                            You have {gold-200} gold
                            PRESS'bttl' TO BATTLE ZE GERMANZ
                            PRESS 'i' TO VIEW INVENTORY.""")
                            cart.append('black knight')
                            gold -= 200
                            if(bttl1==bttl):
                                print(f"""You put black knight in the battle.
                                he dies heriocaly in battle,(wins it)
                                you revive him using a hp potion from your inventory.
                                he gets praised and celebrated.you get peace and....GOLD!!!!
                                You have defeated ze germanz
                                YOU WON!Thanks for playing!!
                                """)
                                break
                            elif(bttl1==i):
                                print(f"""INVENTORY:
                                {cart}""")
                            else:
                                ("INVALID INPUT!try again.")
                        elif(shop_usin4=='3'):
                            print(f"""You have freelanced biccus diccus!
                            You have {gold-1000} gold
                            PRESS'bttl' TO BATTLE ZE GERMANZ
                            PRESS 'i' TO VIEW INVENTORY.""")
                            cart.append('biccus diccus')
                            gold -= 1000
                            if(bttl1==bttl):
                                print(f"""Biccuz runs away leaving his arteliry
                                You used it..........
                                YOU WON!Thanks for playing!!""")
                                break
                            elif(bttl1==i):
                                print(f"""INVENTORY:
                                {cart}""")
                            else:
                                ("INVALID INPUT!try again.")
                        elif(shop_usin4=='4'):
                            print(f"""You have freelanced THE GRIM REAPER!
                            You have {gold-5000} gold
                            The thing 'bout mr.grim is he loves justice
                            he uses ' GRIM EYES' ABILITY
                            REAPING...............
                             ___       ___
                            (_o_)     (_o_)
                           . |     /\      |.
                          (   )   /  \     (  )
                           \  /           /  /
                            \.............../
                             \_____________/       
                            You have defeated ze germanz,
                            You have become village king,
                            You loot the bodies to gain 20000 gold
                            YOU WON!Thanks for playing!!""")
                            cart.append('grim reaper')
                            gold += 20000
                            break
                        elif(shop_usin4=='5'):
                            print(f"""You have freelanced minstrel!
                            The minsterl killed and looted you.
                            YOU DIED!Thanks for playing.
                            """)
                            cart.append('minstrel')
                            gold -= 10000
                            break
                        elif(shop_usin4=='6'):
                            print(f"""You have freelanced minstrel!
                            The minsterl killed and looted you.
                            YOU DIED!Thanks for playing.
                            """)
                            cart.append('minstrel')
                            gold -= 10000
                            break
                        elif(shop_usin4=='7'):
                            print(f"""You have tried freelanced GOD!
                            You have {gold*10} gold
                            GOD APPRICIATES JUSTICE,
                            GOD LIKES BALANCE,
                            GOD LOVES TO PLAY GOD,
                            god used 'BRIGT EYE'!
                            ⠀⠀⢀⡠⠔⠊⠁⣀⣀⡀⢀⣀⣀⠈⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠒⠁⣀⠔⠒⠉⡀⠁⠀⠀⠈⠱⡈⠑⠢⢄⡈⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⣠⡔⠉⠀⠀⠀⠀ ⡆⠀⠀⠀⠀⠀⡇⠀⠀⠀⠉⠢⣌⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠐⠒⠤⠌. ⣦⣀⣀⣠⠬⠤⠄⠒⠒⠈⠉⠉⠁
                            You have recived the blessing of god(2)
                            You have defeated ze germanz
                            YOU WON!Thanks for playing!!
                            PRESS 'i' TO VIEW INVENTORY.""")
                            cart.append('blessing of god')
                            gold *= 10
                            break
                        elif(shop_usin4=='8'):
                            print(f"""You have freelanced nordic guy!
                            You have {gold-2000} gold
                            PRESS 'bttl' TO USE BATTLE
                            PRESS 'i' TO VIEW INVENTORY.""")
                            cart.append('nordic guy')
                            gold -= 2000
                            if(bttl1==bttl):
                                print(f"""
                                Nordic guy axes out ze germanz
                                Splatteer!Sclice!THud!
                                 defeated ze germanz are defeated
                                YOU WON!Thanks for playing!!""")
                                break
                            elif(bttl1==i):
                                print(f"""INVENTORY:
                                {cart}""")
                            else:
                                print("INVAILD INPUT!try again.")
                        elif(shop_usin4=='9'):
                            print(f"""You have freelanced THE MAGE OF ZE ALPS!
                            You have {gold-5000} gold
                            PRESS 'bttl' TO USE BATTLE
                            PRESS 'i' TO VIEW INVENTORY.""")
                            cart.append('mage')
                            gold -= 5000
                            if(bttl1==bttl):
                                print(f"""
                                Mage uses staff of urope.
                                -----\-
                                (<o>) ============
                                -----/
                                BLAAST!
                                Yay!u zefted ze germanz!
                                YOU WON!Thanks for playing!!""")
                                break
                            elif(bttl1==i):
                                print(f"""INVENTORY:
                                {cart}""")
                            else:
                                print("INVAILD INPUT!try again.")
                            break
                        elif(shop_usin4=='10'):
                            print(f"""You have freelanced ze germane!
                            You have {gold-1000} gold
                            Ze germane betrays you immediately!
                            YOU DIED!Thanks for playing!""")
                            cart.append('ze germane')
                            gold -= 1000
                            break
                        else:
                            print("Item not found! Exiting store...")
                        print(f"Your cart: {cart}")
                        print(f"Your gold: {gold}")
                        print("Press any key to continue or '//' to go back to shops")
                        back_input = input()
                        if back_input == '//':
                            continue
                    elif (shop_usin3=='2'):
                        print(f"""{antiques}
                        PRESS ITEM  TO BUY or 'exit' to leave:""")
                        shop_usin4=input()
                        if shop_usin4 == 'exit':
                            print("You left the antique shop.")
                            print("PRESS // TO GO BACK")
                        elif (shop_usin4 in antiques):
                            price = antiques[shop_usin4]
                            if gold >= price and price > 0:
                                cart.append(shop_usin4)
                                gold -= price
                                antiques.pop(shop_usin4)
                                print(f"You bought {shop_usin4} for {price} gold!")
                            elif price < 0:
                                cart.append(shop_usin4)
                                gold += abs(price)
                                antiques.pop(shop_usin4)
                                print(f"You took {shop_usin4} and gained {abs(price)} gold!")
                            else:
                                print("Not enough gold!")
                        else:
                            print("Item not found!")
                        print(f"Your cart: {cart}")
                        print(f"Your gold: {gold}")
                        print("Press any key to continue or '//' to go back to shops")
                        back_input = input()
                        if back_input == '//':
                            continue
                            
                    elif (shop_usin3=='3'):
                        print(f"""{pet_shop}
                        PRESS ITEM KEY TO BUY or 'exit' to leave:""")
                        shop_usin4=input()
                        if shop_usin4 == 'exit':
                            print("You left the pet shop.")
                        elif shop_usin4 in pet_shop:
                            price = pet_shop[shop_usin4]
                            if gold >= price:
                                cart.append(shop_usin4)
                                gold -= price
                                pet_shop.pop(shop_usin4)
                                print(f"You bought {shop_usin4} for {price} gold!")
                                if shop_usin4 == 'newt':
                                    print("The newt looks at you knowingly... something special about this one!")
                            else:
                                print("Not enough gold!")
                        else:
                            print("Item not found!")
                        print(f"Your cart: {cart}")
                        print(f"Your gold: {gold}")
                        print("Press any key to continue or '//' to go back to shops")
                        back_input = input()
                        if back_input == '//':
                            continue
                            
                    elif (shop_usin3=='4'):
                        print(f"""{grocery}
                        PRESS ITEM  TO BUY or 'exit' to leave:""")
                        shop_usin4=input()
                        if shop_usin4 == 'exit':
                            print("You left the grocery store.")
                        elif shop_usin4 in grocery:
                            price = grocery[shop_usin4]
                            if gold >= price:
                                cart.append(shop_usin4)
                                gold -= price
                                grocery.pop(shop_usin4)
                                print(f"You bought {shop_usin4} for {price} gold!")
                            else:
                                print("Not enough gold!")
                        else:
                            print("Item not found!")
                        print(f"Your cart: {cart}")
                        print(f"Your gold: {gold}")
                        print("Press any key to continue or '//' to go back to shops")
                        back_input = input()
                        if back_input == '//':
                            continue
                            
                    elif (shop_usin3=='5'):
                        print(f"""{botanical_nursery}
                        PRESS ITEM  TO BUY or 'exit' to leave:""")
                        shop_usin4=input()
                        if shop_usin4 == 'exit':
                            print("You left the botanical nursery.")
                        elif shop_usin4 in botanical_nursery:
                            price = botanical_nursery[shop_usin4]
                            if gold >= price:
                                cart.append(shop_usin4)
                                gold -= price
                                botanical_nursery.pop(shop_usin4)
                                print(f"You bought {shop_usin4} for {price} gold!")
                                if shop_usin4 == 'magic beans':
                                    print("These beans tingle with magical energy... they might grow into something amazing!")
                            else:
                                print("Not enough gold!")
                        else:
                            print("Item not found!")
                        print(f"Your cart: {cart}")
                        print(f"Your gold: {gold}")
                        print("Press any key to continue or '//' to go back to shops")
                        back_input = input()
                        if back_input == '//':
                            continue
                            
                    elif (shop_usin3=='6'):
                        print(f"""{farmers_market}
                        PRESS ITEM  TO BUY or 'exit' to leave:""")
                        shop_usin4=input()
                        if shop_usin4 == 'exit':
                            print("You left the farmers market.")
                        elif shop_usin4 in farmers_market:
                            price = farmers_market[shop_usin4]
                            if gold >= price:
                                cart.append(shop_usin4)
                                gold -= price
                                farmers_market.pop(shop_usin4)
                                print(f"You bought {shop_usin4} for {price} gold!")
                            else:
                                print("Not enough gold!")
                        else:
                            print("Item not found!")
                        print(f"Your cart: {cart}")
                        print(f"Your gold: {gold}")
                        print("Press any key to continue or '//' to go back to shops")
                        back_input = input()
                        if back_input == '//':
                            continue
                            
                    else:
                        print("Invalid shop number! Try again.")
            else:
                print("""What will you do?
                PRESS 'o1' TO SEE OPTIONS""")
                opt_usin1=input()
                if(opt_usin1=='o1'):
                    print(f"""{o1}
                    WHICH WILL YOU CHOOSE?(1,2,3,4,5)""")
                    opt_usind=input()
                    if(opt_usind=='1'):
                        print("""You get stabbed and decapitated by ze germanz!
                        YOU DIED!Thanks for playing!""") 
                    elif(opt_usind=='2'):
                        print("""You run away go to a foreset.You start a new life:
                        build a hut, start foreging and hunting and farming,tame a wolf,life is going go-You Got Torn Apart by a  Medival Bear.
                        YOU DIED!Thanks for playing!""")
                    elif(opt_usind=='3'):
                        print("""You hid away in your home,nice tactic dude!But..... ze germznz ravaezed the vilaze and burnt it all down!
                        YOU DIED!Thanks for playing! """)
                    elif(opt_usind=='4'):
                        print("""Well they stabbed and killed all corpses to ensure no survivors...
                        YOU DIED!Thanks for playing!""")
                    elif(opt_usind=='5'):
                        print("""You ally with ze germanz they give you some stuff and ask you to give them your gold as 'peace offering'.
                        on the way  xu ze germane lyand, they literally stab you in the back!
                        YOU DIED!Thanks for playing!""")
                else:
                    print("Invalid input!,try again.")
        else:
            print(f"""What will you do?
            PRESS 'o2' TO SEE OPTIONS""")
            opt_usin2=input()
            if(opt_usin2=='o2'):
                print(f"""{o1}
                WHICH WILL YOU CHOOSE?(1,2,3,4,5)""")
                opt_usind3=input()
                if(opt_usind3=='1'):
                    print("""You get stabbed and decapitated by ze germanz!
                    YOU DIED!Thanks for playing!""") 
                elif(opt_usind3=='2'):
                    print("""You run away go to a foreset.You start a new life:
                    build a hut, start foreging and hunting and farming,tame a wolf,life is going go-You Got Torn Apart by a  Medival Bear.
                    YOU DIED!Thanks for playing!""")
                elif(opt_usind3=='3'):
                    print("""You hid away in your home,nice tactic dude!But..... ze germznz ravaezed the vilaze and burnt it all down!
                    YOU DIED!Thanks for playing! """)
                elif(opt_usind3=='4'):
                    print("""Well they stabbed and killed all corpses to ensure no survivors...
                    YOU DIED!Thanks for playing!""")
                elif(opt_usind3=='5'):
                    print("""You ally with ze germanz they give you some stuff and ask you to give them your gold as 'peace offering'.
                    on the way  xu ze germane lyand, they literally stab you in the back!
                    YOU DIED!Thanks for playing!""")
    elif(user_input!='i'):
            print(f"""What will you do?
            PRESS 'o3' TO SEE OPTIONS""")
            opt_usin4=input()
            if(opt_usin4=='o3'):
                    print(f"""{o1}
                    WHICH WILL YOU CHOOSE?(1,2,3,4,5)""")
                    opt_usind=input()
                    if(opt_usind=='1'):
                        print("""You get stabbed and decapitated by ze germanz!
                        YOU DIED!Thanks for playing!""") 
                    elif(opt_usind=='2'):
                        print("""You run away go to a foreset.You start a new life:
                        build a hut, start foreging and hunting and farming,tame a wolf,life is going go-You Got Torn Apart by a  Medival Bear.
                        YOU DIED!Thanks for playing!""")
                    elif(opt_usind=='3'):
                        print("""You hid away in your home,nice tactic dude!But..... ze germznz ravaezed the vilaze and burnt it all down!
                        YOU DIED!Thanks for playing! """)
                    elif(opt_usind=='4'):
                        print("""Well they stabbed and killed all corpses to ensure no survivors...
                        YOU DIED!Thanks for playing!""")
                    elif(opt_usind=='5'):
                        print("""You ally with ze germanz they give you some stuff and ask you to give them your gold as 'peace offering'.
                        on the way  xu ze germane lyand, they literally stab you in the back!
                        YOU DIED!Thanks for playing!""")
else:
    print("cancled!")