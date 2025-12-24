
"""
    GESTION DES UTILISATEURS
"""

from operation.request import User

def inputs():
    first_name = input("Fist name: ")
    last_name = input("Last name: ")
    age = input("Age: ")
    email = input("Email: ")

    return (
        first_name,
        last_name,
        age,
        email
    )

def actions(action):
    if action == '1':
        users = User.select_user()
        print(f"\n ==> Users list <=== \n")
        if users:
            for user in users:
            
                print(f"{user[0]} {user[1]} {user[2]} {user[3]} {user[4]}")
        else:
            print(f"Aucun utilisateur disponible {users}")

    elif action == '2':
        user = inputs()
        if user:
            User(*user).insert_user()
        else:
            print("\n ===> Incorect infos")
    elif action == '3':
        user = inputs()
        if user:
            User(*user).update_user()
            
    elif action == '4':
        User.delete_user()
    else:
        print("\n ===> Enter a valid action.")

while True:
    print(
        """
            ========= GESTIONS DES UTILISATEURS ==========

            1. Show users list
            2. Add user
            3. Update user
            4. Delete user
            5. Quite
        """
    )

    try:
        action = input("Entrer une action à effectuée : ")

        if action == '5':
            print("==== FIN DU PROGRAMME ====")
            break
        
        if action.isdigit():
            actions(action)
        else:
            print("L'action doit etre un nombre dans la chaine.")
    except Exception as e:
        print(str(e))