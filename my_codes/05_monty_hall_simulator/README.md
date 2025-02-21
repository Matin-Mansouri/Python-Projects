# Monty Hall Simulator

This project simulates the Monty Hall problem, a famous probability puzzle based on a game show scenario. The simulator allows users to experiment with different strategies and observe the outcomes.

The Monty Hall problem is a probability puzzle based on a game show. You are given the choice of three doors: behind one door is a car; behind the others, goats. After you pick a door, the host, who knows what's behind the doors, opens another door, revealing a goat. You are then given the choice to switch to the remaining unopened door or stay with your original choice. The simulator will reveal if you won a car or a goat. For more information, visit [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the simulator, execute the following command:

```bash
streamlit run src/app.py
```

This will start a Streamlit web application where you can interact with the Monty Hall simulation.

## Project Structure

- `src/monty_hall.py`: Contains the logic for simulating the Monty Hall game.
- `src/app.py`: The Streamlit application to visualize the simulation.
- `requirements.txt`: The file containing the required Python packages.


## License

This project is licensed under the MIT License.
