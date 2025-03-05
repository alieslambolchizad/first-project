import random
user_score=0
pc_score=0
show=True
option = ['k', 's', 'q']

while show==True:
    
    user_choice=input('gozine khod ra vared konid [s,k,q]\ns')
    if user_choice in option:
        pc_choice=random.choice(option)
        print(f'pc_choice is : {pc_choice}')
        if pc_choice==user_choice:
            print('mosavi dobare bezan')
        elif user_choice=='s':
            if pc_choice=='k':
                print('pc bord')
                pc_score+=1
            else:
                print('user bord')
                user_score+=1
        elif user_choice=='k':
            if pc_choice=='q':
                print('pc bord')
                pc_score+=1
            else:
                print('user bord')
                user_score+=1
        elif user_choice=='q':
            if pc_choice=='s':
                print('pc bord')
                pc_score+=1
            else:
                print('user bord')
                user_score+=1
        print(f'User score: {user_score} / PC score: {pc_score}')
        if user_score==3 or pc_score==3:
            if user_score==3:
                print('user barande shod')
            else:
                print('pc barande shod')
            break
    else:
        print('gozine dorost ra vared kon')