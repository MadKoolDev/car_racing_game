import random
import time
from colorama import Fore, Style
from cars import Cars
from time import sleep
from track import Track


def show_results():
    with open("racing_game_results.txt", "r") as racing_game_results:
        print(racing_game_results.read())


def save_time(start_time, car=None, tie=False):
    if tie:
        text = "TIE! Race finished in " \
               f"{format(time.time() - start_time, '.2f')} seconds! \n"
    else:
        text = f"{car.car_name} finished in " \
               f"{format(time.time() - start_time, '.2f')} seconds! \n"
    with open("racing_game_results.txt", "a") as racing_game_results:
        racing_game_results.write(text)
        sleep(0.5)


def racing_game():
    race_ended = False
    while not race_ended:
        car_1 = Cars(f"{Fore.RED}car{Style.RESET_ALL}", random.randint(1, 5))
        car_2 = Cars(f"{Fore.BLUE}car{Style.RESET_ALL}", random.randint(1, 5))
        track = Track(random.randint(10, 17))
        track.lane1.insert(0, car_1.car_name)
        track.lane2.insert(0, car_2.car_name)
        for _ in range(len(track.lane1)):
            start_time = time.time()
            current_pos = track.lane1.index(car_1.car_name)
            current_pos_pc = track.lane2.index(car_2.car_name)
            next_pos = current_pos + car_1.car_speed
            next_pos_pc = current_pos_pc + car_2.car_speed
            track.lane1.pop(current_pos)
            track.lane2.pop(current_pos_pc)
            track.lane1.insert(next_pos, car_1.car_name)
            track.lane2.insert(next_pos_pc, car_2.car_name)
            print(*track.lane1)
            print(*track.lane2)
            sleep(0.5)

            if track.lane2.index(car_2.car_name) < track.lane1.index(car_1.car_name) >= track.length + 1:
                print(f"{car_1.car_name} won!")
                sleep(1)
                print(f"with time {format(time.time() - start_time, '.2f')}")
                save_time(start_time, car_1)
                sleep(1)
                break

            elif track.lane1.index(car_1.car_name) < track.lane2.index(car_2.car_name) >= track.length + 1:
                print(f"{car_2.car_name} won!")
                sleep(1)
                print(f"with time {format(time.time() - start_time, '.2f')}")
                save_time(start_time, car_2)
                sleep(1)
                break

            elif track.lane1.index(car_1.car_name) >= track.length + 1 \
                    and track.lane2.index(car_2.car_name) >= track.length + 1:
                print(f"It's a TIE!")
                sleep(1)
                print(f"The race ended with the time {format(time.time() - start_time, '.2f')}")
                save_time(start_time=start_time, tie=True)
                sleep(1)
                break

        while True:
            another_round = input("Do you want to have another go? (yes/no): ")
            if another_round == "yes":
                race_ended = False
                break
            elif another_round == "no":
                print("Thanks for playing")
                return None
            else:
                print("yes/no only, please")


game_ended = False
game_menu = False

print("========================================")
print("Welcome to the great racing game!")
print("========================================")

sleep(1)

while not game_ended:

    while not game_menu:
        user_choice = input(" \n1 - Let's start the race! \n2 - See the scoreboard! \n3 - QUIT! \nType option number: ")
        check_action = user_choice.isnumeric()
        if check_action is False or int(user_choice) not in range(1, 4):
            print("Wrong input. Please type option number 1, 2 or 3!")
            continue
        elif int(user_choice) == 1:
            print("Alrighty! Here we go!")
            sleep(1)
            racing_game()
        elif int(user_choice) == 2:
            show_results()
        elif int(user_choice) == 3:
            print(" \nThank you for playing!")
            quit()

# Def is used to define variables.
# Classes is used to shorten the code by implementing different variables in it.
