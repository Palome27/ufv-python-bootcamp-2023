reality = "Real World"  # This is the global variable


def dream_level_1():
    x = "Dream Level 1: Paris"  # local variable to dream_level_1

    def dream_level_2():
        x = "Dream Level 2: Hotel"  # local variable to dream_level_2

        def dream_level_3():
            y = "Dream Level 3: Snow Fortress"  # local variable to dream_level_3

            def limbo():
                global reality  # Declare global first before using the name x in any way.
                print(f"In Limbo, reality is: {reality}")
                reality = "Real World, but altered"  # modifying global reality

                nonlocal x  # Going back to Dream Level 3's x
                print(f"In Limbo, after altering reality, the Dream Level 3 is: {x}")
                x = "Dream Level 2, Hotel but altered"  # modifying the dream level 3 reality

                nonlocal y
                y = "Dream Level 3, Ice Fortress but altered"

            print(f"In {x}, starting to go deeper...")
            limbo()
            print(f"Back in {y}, after Limbo.")

        print(f"In {x}, starting to go deeper...")
        dream_level_3()
        print(f"Back in {x}, after Dream Level 3.")

    print(f"In {x}, starting to go deeper...")
    dream_level_2()
    print(f"Back in {x}, after Dream Level 2.")


print(f"In the {reality}, starting to dream...")
dream_level_1()
print(f"Back in the {reality}.")
