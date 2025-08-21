while True:
    try:
        A = input().strip()
        B = input().strip()
        C = input().strip()

        print(f"A = {A}, B = {B}, C = {C}")
        print(f"A = {B}, B = {C}, C = {A}")
        print(f"A = {C}, B = {A}, C = {B}")
    except EOFError:
        break