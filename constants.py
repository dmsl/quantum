algorithms = ["Deutsch-Josza", "Bernstein-Vazirani"]

experiments = ["Bell State - Hello World", "Superposition with one Qubit", "Superposition with three Qubits",
               "Interference"]

acceptable_execution_inputs = ['0', '1', '2', '3', '4']

acceptable_algorithm_inputs = ['0', '1']

acceptable_experiment_inputs = ['0', '1', '2', '3']

input_message_1 = "Choose an Algorithm: " \
                  "\n0 for Deutsch-Josza." \
                  "\n1 for Bernstein-Vazirani" \
                  "\nYour input:"

input_message_2 = "Enter:" \
                  "\n\n0 for execution on the Local Device Simulator." \
                  "\n\n1 for execution on the Qasm simulator." \
                  "\n\n2 for execution on a real device." \
                  "\n\n3 for execution on the local device and real device." \
                  "\n\n4 for evaluating the algorithm" \
                  "\nby running comparisons of classical and quantum inputs with different sized inputs." \
                  "\n\nYour input:"

input_message_3 = "\nEnter the maximum size of input you would like to evaluate" \
                  "\n(in number of bits). The maximum is 14."
cards = ["H", "H", "X", "X", "CX", "SX", "SXDG"]

acceptable_choice_inputs = ['1', '2', '3', '4']

experimentation_level = "Enter:" \
                        "\n\n1 For Level 1 experimentation. (Simple experiments)" \
                        "\n\n2 For Level 2 experimentation. (The Exciting Game)" \
                        "\n\n3 For Level 3 experimentation. (Algorithm Experimentation)" \
                        "\n\n4 For Level 4 experimentation. (Algorithm Evaluation)" \
                        "\n\nYour input:"
