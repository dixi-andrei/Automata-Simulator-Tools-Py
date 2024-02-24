# Automata Simulator Tools (Python)

This project is an Automata Simulator Tools implemented in Python. It enables users to simulate various types of automata, including Non-deterministic Finite Automaton (NFA), Deterministic Finite Automaton (DFA), Context-Free Grammar (CFG), and Pushdown Automaton (PDA).

## Features

- **NFA Simulation:** Simulate the behavior of Non-deterministic Finite Automata (NFA). NFAs can represent systems that can be in multiple states simultaneously, leading to a non-unique computation path for a given input string.

- **DFA Simulation:** Simulate the behavior of Deterministic Finite Automata (DFA). DFAs are state machines where, for each input symbol, there is a unique transition to a next state, making their computation paths deterministic.

- **CFG Simulation:** Simulate the behavior of Context-Free Grammars (CFG). CFGs are used to describe context-free languages and are widely employed in the analysis and processing of programming languages.

- **PDA Simulation:** Simulate the behavior of Pushdown Automata (PDA). PDAs extend the capabilities of DFAs by using a stack to manage memory, allowing them to recognize languages that cannot be recognized by DFAs or NFAs.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/dixi-andrei/Automata-Simulator-Tools-Py
    cd automata-simulator-tools-py
    ```

2. Navigate to the specific automaton directory you want to simulate (e.g., `nfa`, `dfa`, `cfg`, `pda`).

    ```bash
    cd nfa
    ```

3. Run the Python script with your desired input file.

    ```bash
    python simulate.py datainNFA(1.7)
    ```

4. View the output for the simulation.

    ```plaintext
    # Example output for NFA(1.7)
    Accepts strings with 0 as the penultimate symbol
    ```

## Example Input Files

- `datainNFA(1.7)`: Example input file for NFA(1.7)
- `datainDFA(1.5)`: Example input file for DFA(1.5)
- `datainCFG(2.4)`: Example input file for CFG(2.4)
- `datainPDA(2.6)`: Example input file for PDA(2.6)

Each input file contains the necessary information to define the automaton's structure and behavior.

## Example Output Files

- `dataoutNFA`: Example output file for NFA(1.7)
- `dataoutDFA`: Example output file for DFA(1.5)
- `dataoutCFG`: Example output file for CFG(2.4)
- `dataoutPDA`: Example output file for PDA(2.6)

These output files contain the expected output for each respective automaton.
