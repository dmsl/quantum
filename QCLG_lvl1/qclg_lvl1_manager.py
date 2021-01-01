import constants
from QCLG_lvl1.hello_quantum_world import HelloWorld
from QCLG_lvl1.interference import Interference
from QCLG_lvl1.single_qubit_superposition import SingleQubitSuperposition
from QCLG_lvl1.three_qubits_superposition import ThreeQubitSuperposition


class SimpleExperimentsManager:
    @classmethod
    def showcase(cls):
        print("Hi, these are the available experiments")

        for i in range(len(constants.experiments)):
            print(f"{i}. {constants.experiments[i]}")

        choice = input(f"Which experiment would you like to try from 0 to {len(constants.experiments)-1}? ")

        while choice not in constants.acceptable_experiment_inputs:
            choice = input(f"Which experiment would you like to try from 0 to {len(constants.experiments) - 1}? ")
        if choice == "0":
            HelloWorld.run()
        elif choice == "1":
            SingleQubitSuperposition.run()
        elif choice == "2":
            ThreeQubitSuperposition.run()
        elif choice == "3":
            Interference.run()

