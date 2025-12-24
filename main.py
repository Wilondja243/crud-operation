
"""
    USER MANAGEMENT
"""

from crud.views import User
from services.action import actions


while True:
    print(
        """
            ========= USER MANAGEMENT ==========

            1. Show users list
            2. Add user
            3. Update user
            4. Delete user
            5. Quite
        """
    )

    try:
        action = input("Enter an action to perform : ")

        if action == '5':
            print("==== END PROGRAMME ====")
            break
        
        if action.isdigit():
            actions(action, User)
        else:
            print("Enter the action number.")
    except Exception as e:
        print(str(e))