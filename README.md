# Quantum Computing Learning Gate

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Structure](#structure)
* [Useful Resources](#useful-resources)

## General info
A standalone platform capable of hosting Quantum Computing experiments of different levels using Qiskit resources.
	
## Technologies
Technologies and Frameworks used for this project:
* Python 3.7
* Qiskit
* IBM Quantum Experience
* Conda environments
* PyCharm
	
## Setup
- We demonstrate the procedure of setting up QCLG in a new Windows 10 machine.
- The instructions are very similar for Ubuntu with slight modifications required for paths.
- Clone the repository locally by doing the following:
* 1. Launch PyCharm.
* 2. From the “VCS” tab, choose the option “Get from Version Control…”
* 3. From the pop-up window paste the https URL of the dmsl/quantum repository: https://github.com/dmsl/quantum.git
* 4. Press the Clone button and choose to open on a new window.
- The project will not yet work. We need to create and setup the conda environment and setup a Run Configuration in PyCharm.
- For the conda environment:
- Install Anaconda.
- Open an Anaconda cmd.
- We will now need to create the environment using these instructions:
https://docs.anaconda.com/anacondaorg/user-guide/tasks/work-with-environments/
- We have uploaded our environment into our personal account, (sooodos/quantum) and we can activate it with the following command.

- Now execute the following command and replace the “my_env_name” with your desired environment name.
```
conda create --name my_env_name sooodos/quantum
```
- After the installation finishes, go back to PyCharm. In the bottom-right corner click on the Project Interpreter box.
- Choose the “Add Interpreter…” option.
- From the pop-up window choose “Conda Environment” and then click on the “Existing environment” option.
- Now you need to search for the python.exe script responsible for the Interpreter.
- By default, it should be located in C:\Users\NameOfUser\Anaconda3\envs\my_env_name\python.exe.
- Save changes.
- Now we need to add a Run Configuration from PyCharm.
- Go to the upper-right corner of the window, the Run Configurations box is located to the left of the “run” icon.
- Click on it and then click “Edit Configurations”.
- On the pop-up window click the “+” icon and choose “Python”. Now we need to add the script path of manager.py in order to create our Run Configuration. Just click on the folder icon which is on the far-right corner of the “Script path” place holder and find manager.py from the project hierarchy.
- Click Apply and OK.
- Now add the token generated by your IBM Account and insert into the account_details.py file in the corresponding token placeholder.

- QCLG is now operational.

## Structure

The idea of QCLG is to allow individuals of different competence levels to experiment with Quantum Computing. It is also possible to contribute to different levels according to the structure rules. We have implemented four different levels of experimentation, each with a different goal. All levels take advantage of Qiskit resources but to different degrees. 

![Alt text](Pictures/qclg.PNG?raw=true "qclg")

### Level 1

Level 1 is where experimentations concerning the basic concepts of Quantum
Computing take place. It is the starting place after getting familiarized with the Quantum
Primers we discussed in Chapter 3. Here, the user can explore and add experimentations
of very basic quantum circuits in order to test their understanding before moving on to
the next levels. The currently available experiments in Level 1 are about Superposition,
Entanglement, and Phase Kickback and we showcase them in more detail in Chapter 5.

### Level 2

Level 2 is an intermediate layer that aims to motivate the user to learn about
Quantum Computing through more interactive mediums. Once the user has become more
proficient with the basic quantum concepts, they can test their knowledge with a quantum
game for example. The currently available game is “The Exciting Game” which we cover
extensively in Chapter 6.

### Level 3

Level 3 has two objectives. The first objective is to implement quantum
algorithms and the second objective is to implement the classical solution to that
algorithm in order to allow the user to achieve a deeper understanding of that algorithm.
Level 3 has many choices regarding the execution of experiments. They can choose to
solve the problem classically by executing the solution onto their local device and observe
the results, execute the quantum solution of the problem in the IBM backends or solve 
the problem with both approaches and observe the differences. Below we list the three
directories included in Level 3.

#### quantum_algorithms

In this directory, we store the implementations of major quantum Algorithms, as
well as a controller class that allows individual calling of each of these algorithms. Up to
the current point of development of this thesis, we have implementations for the DeutschJozsa and Bernstein-Vazirani,
offering execution for each algorithm on a simulator, on a real quantum system, on the
local machine, executed classically, on both a real quantum system and the local machine
for comparison.

#### oracles

In the oracles directory, we store all the oracle functions necessary for
implementing the quantum algorithms. Currently, there are implementations for one
possible oracle function of Deutsch-Jozsa which can be found in 7.3.3, and the
implementation of the oracle function for Bernstein-Vazirani which can be found in 7.6.3.

#### classical

The classical directory contains all required classes for implementing the classical
solutions of the Quantum Algorithms. This includes the logic for the classical algorithms,
as well as some additional implementations for input generation.

### Level 4

Once the user feels comfortable with all the previous levels, they can proceed to
Level 4, which is the automated evaluation of an Algorithm based on its classical and
quantum solution. Here, besides an adequate understanding of Quantum Computation
concepts, the user must also practice with the Qiskit API in order to extract the necessary 
data to extract useful results.
