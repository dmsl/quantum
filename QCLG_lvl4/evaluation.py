from QCLG_lvl3.classical.random_binary import RandomBinary
from tools import Tools
import constants
from qiskit.providers import JobStatus


class Evaluation:

    @classmethod
    def evaluate(cls, algorithm):

        if algorithm == "0":
            cls.evaluate_deutsch_josza()
        elif algorithm == "1":
            cls.evaluate_bernstein_vazirani()

    @classmethod
    def plot_results(cls, inputs: list, quantum: list, classical: list, accuracy: list):
        import numpy as np
        import matplotlib.pyplot as plt
        X = np.arange(start=1, stop=len(inputs) + 1, step=1)
        plt.figure()
        plt.subplot(211)
        plt.title("Execution Times")
        plt.bar(X + 0.00, classical, color='b', width=0.25)
        plt.bar(X + 0.25, quantum, color='g', width=0.25)
        plt.ylabel("In seconds")
        plt.legend(labels=['Classical', 'Quantum'])
        plt.subplot(212)
        plt.title("Quantum Accuracy")
        plt.bar(inputs, accuracy, color='g')
        plt.ylabel("Percentage")
        plt.legend(labels=['Accuracy Percentage'])
        plt.show()
        return

    @classmethod
    def evaluate_deutsch_josza(cls):
        print(constants.input_message_3)
        test_range = int(input())
        while test_range > 14 or test_range < 1:
            test_range = int(input("Enter a number between 1 and 14."))

        circuits = []
        n_bits = []
        quantum_execution_times = []
        classical_execution_times = []
        success_rates = []

        print("Evaluating Deutsch - Josza... This might take a while...")

        for number_of_bits in range(1, test_range + 1):
            n_bits.append(number_of_bits)
            circuits.append(Tools.prepare_dj(number_of_bits))
            total_time = 0.0
            for i in range(1024):
                classical_result = Tools.deutsch_josza_classical(number_of_bits)
                total_time = total_time + classical_result[1]
            classical_execution_times.append(total_time)
            completion_percentage = int((number_of_bits / test_range) * 100)
            print(f"{completion_percentage}% of classical executions done.")

        print("Now looking for the least busy backend...")
        least_busy_backend = Tools.find_least_busy_backend_from_open(test_range)

        print("Now waiting for the Quantum Batch Job to finish...\nThis will take a while...")
        quantum_results = Tools.run_batch_job(circuits, least_busy_backend)
        flag = False
        while not flag:
            for status in quantum_results.statuses():
                flag = True
                if status != JobStatus.DONE:
                    flag = False
        print("Quantum experiments finished.")

        print("Preparing plots...")
        count_jobs = 1
        for job in quantum_results.managed_jobs():
            quantum_execution_times.append(job.result().time_taken)
            counts_dict = job.result().get_counts()
            correct_counts = counts_dict.get('1' * count_jobs, 0)
            print(correct_counts)
            success_percentage = (correct_counts / 1024) * 100
            success_rates.append(success_percentage)
            count_jobs = count_jobs + 1

        cls.plot_results(n_bits, quantum_execution_times, classical_execution_times, success_rates)
        return

    @classmethod
    def evaluate_bernstein_vazirani(cls):
        print(constants.input_message_3)
        test_range = int(input())
        while test_range > 14 or test_range < 1:
            test_range = int(input("Enter a number between 1 and 14."))

        n_bits = []
        circuits = []
        quantum_execution_times = []
        classical_execution_times = []
        success_rates = []
        random_binaries = []
        print("Evaluating Bernstein - Vazirani... This might take a while...")

        for number_of_bits in range(1, test_range + 1):
            n_bits.append(number_of_bits)
            classical_result = Tools.bernstein_vazirani_classical(number_of_bits)
            random_binary = RandomBinary.generate_random_binary_v2(number_of_bits)
            random_binaries.append(random_binary)
            circuits.append(Tools.prepare_bv(random_binary))
            classical_execution_times.append(classical_result[1])
            completion_percentage = int((number_of_bits / test_range) * 100)
            print(f"{completion_percentage}% of preparation done.")

        print("Now looking for the least busy backend...")
        least_busy_backend = Tools.find_least_busy_backend_from_open(test_range)

        print("Now waiting for the Quantum Batch Job to finish...\nThis will take a while...")
        quantum_results = Tools.run_batch_job(circuits, least_busy_backend)
        flag = False
        while not flag:
            for status in quantum_results.statuses():
                flag = True
                if status != JobStatus.DONE:
                    flag = False
        print("Quantum experiments finished.")

        print("Preparing plots...")
        count = 0
        for job in quantum_results.managed_jobs():
            quantum_execution_times.append(job.result().time_taken)
            counts_dict = job.result().get_counts()
            correct_counts = counts_dict.get(random_binaries[count], 0)
            print(correct_counts)
            success_percentage = (correct_counts / 1024) * 100
            success_rates.append(success_percentage)
            count = count + 1

        cls.plot_results(n_bits, quantum_execution_times, classical_execution_times, success_rates)
        return
