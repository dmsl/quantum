import constants
from QCLG_lvl1.qclg_lvl1_manager import SimpleExperimentsManager
from QCLG_lvl2.the_exciting_game import Game
from QCLG_lvl3.quantum_algorithms.algorithms_manager import AlgorithmsManager
from QCLG_lvl4.evaluation import Evaluation


class Manager:
    if __name__ == '__main__':
        flag = "Y"
        while flag == "Y":

            choice = input(constants.experimentation_level)
            while choice not in constants.acceptable_choice_inputs:
                choice = input(constants.experimentation_level)

            if choice == '1':
                SimpleExperimentsManager.showcase()
            elif choice == '2':
                Game.play_the_exciting_game()
            elif choice == '3':
                AlgorithmsManager.showcase()
            elif choice == '4':
                algorithm = input(constants.input_message_1)
                while algorithm not in constants.acceptable_algorithm_inputs:
                    algorithm = input(constants.input_message_1)
                Evaluation.evaluate(algorithm)

            flag = input("Would you like to keep experimenting? (Y/N)")
            while flag is not "Y" and flag is not "N":
                flag = input("Would you like to keep experimenting? Please give a valid response. (Y/N)")
        print("\nYour experimenting session is now concluded. \nThank you.")
