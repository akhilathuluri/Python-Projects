import random
import time

print("Welcome to my game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10
points = 0

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health and", points, "points.")
        print("Let's play!")
        time.sleep(1)

        path = input("Choose a path: climb a mountain or explore a forest (mountain/forest)? ").lower()

        if path == "mountain":
            print("You climb the mountain and reach the top.")
            time.sleep(1)
            encounter = random.choice(["friendly", "hostile"])
            if encounter == "friendly":
                print("Suddenly, you hear a voice behind you...")
                time.sleep(1)
                print("You turn around and see a wise old man who offers you a health potion.")
                health += 5
                points += 10
            else:
                print("As you reach the top, you hear a loud roar...")
                time.sleep(1)
                print("You turn around and see a fierce dragon blocking your path.")
                time.sleep(1)
                print("It breathes fire at you and you lose 5 health.")
                health -= 5

        else:
            print("You enter the forest and hear strange noises.")
            time.sleep(1)
            encounter = random.choice(["friendly", "hostile"])
            if encounter == "friendly":
                print("You see a light in the distance...")
                time.sleep(1)
                print("As you get closer, you realize it's a group of friendly elves.")
                time.sleep(1)
                print("They offer you a treasure map as a reward for your good deeds.")
                points += 15
            else:
                print("You hear buzzing all around you...")
                time.sleep(1)
                print("You look down and see a swarm of angry bees attacking you.")
                time.sleep(1)
                print("You lose 3 health.")
                health -= 3

        print("Your current health is:", health)

        if health <= 0:
            print("You have 0 health and you lost the game...")
        else:
            ans = input("You come across a river. Do you swim across or look for a bridge (swim/bridge)? ").lower()

            if ans == "bridge":
                print("You find a bridge and cross the river safely.")
                time.sleep(1)
                print("As you cross the bridge, you notice something shiny on the ground.")
                time.sleep(1)
                print("You pick it up and gain 5 points.")
                points += 5
            else:
                encounter = random.choice(["friendly", "hostile"])
                if encounter == "friendly":
                    print("You jump into the river and start swimming...")
                    time.sleep(1)
                    print("Suddenly, something catches your eye...")
                    time.sleep(1)
                    print("You swim towards it and discover a friendly mermaid who offers you a magic pearl.")
                    points += 10
                else:
                    print("You jump into the river and start swimming...")
                    time.sleep(1)
                    print("Suddenly, something grabs your leg and pulls you under...")
                    time.sleep(1)
                    print("You struggle to break free but it's too strong.")
                    time.sleep(1)
                    print("You lose 7 health as a giant sea monster attacks you.")
                    health -= 7
                print("Your current health is:", health)

                if health <= 0:
                    print("You have 0 health and you lost the game...")
                else:
                    print("You cross the river and continue on your journey.")
                    time.sleep(1)
                    print("You reach a fork in the road and have to make a decision.")
                    time.sleep(1)
                    choice = input("Do you go left or right? ").lower()

                    if choice == "left":
                        print("You take the left path and come across a dark cave.")
                        time.sleep(1)
                        print("You enter the cave and see a glowing crystal.")
                        time.sleep(1)
                        encounter = random.choice(["friendly", "hostile"])
                        if encounter == "friendly":
                            print("You approach the crystal and it starts to glow brighter...")
                            time.sleep(1)
                            print("Suddenly, you hear a voice...")
                            time.sleep(1)
                            print("The crystal speaks to you and offers you a choice.")
                            time.sleep(1)
                            print("You can either gain 10 points or restore 5 health.")
                            choice = input("Which do you choose, points or health? ").lower()
                            if choice == "points":
                                points += 10
                            else:
                                health += 5
                        else:
                            print("As you approach the crystal, you hear a low growl...")
                            time.sleep(1)
                            print("A giant spider jumps out from behind a rock and attacks you.")
                            time.sleep(1)
                            print("You lose 5 health.")
                            health -= 5

                    else:
                        print("You take the right path and see a beautiful meadow.")
                        time.sleep(1)
                        print("You walk through the meadow and see a unicorn.")
                        time.sleep(1)
                        encounter = random.choice(["friendly", "hostile"])
                        if encounter == "friendly":
                            print("The unicorn walks up to you and nuzzles your hand.")
                            time.sleep(1)
                            print("It then gives you a gift, a magical amulet.")
                            points += 20
                        else:
                            print("As you approach the unicorn, it rears up and snorts.")
                            time.sleep(1)
                            print("It then charges at you and you have to defend yourself.")
                            time.sleep(1)
                            print("You lose 3 health.")
                            health -= 3

                    if health <= 0:
                        print("You have 0 health and you lost the game...")
                    else:
                        print("Congratulations, you have completed the game!")
                        print("Your final score is:", points)
    else:
        print("Ok, maybe another time.")
else:
    print("Sorry, you are not old enough to play this game.")