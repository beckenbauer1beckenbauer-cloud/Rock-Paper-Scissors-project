# Rock Paper Scissors AI Player

The core objective is to construct an autonomous adaptive player function that defeats 4 programmatic bots—each employing disparate mathematical and historical strategies (Quincy, Abbey, Kris, and Mrugesh)—by achieving a minimum win rate of **60%** over 1000 consecutive rounds per match.

## 🧠 Algorithmic Architecture (N-gram Markov Model)

Instead of utilizing heavy neural network frameworks, this solution implements an elegant, high-speed **Markov Chain N-gram predictive sequence engine**:
1. **State Preservation**: Leverages persistent list arguments to dynamically track the operational history of the opponent across continuous function calls.
2. **Pattern Scanning**: Isolates the most recent $N$ sequence steps ($N=3$) and maps potential trailing actions (`R`, `P`, or `S`).
3. **Frequency Assessment**: Performs full-string pattern analysis via `.count()` to dynamically estimate the probability distribution of the opponent's next action.
4. **Counter-Action Dispatch**: Executes the deterministic counter-move mapping designed to exploit the predicted selection.

## 🚀 Execution and Verification

Execute the tournament platform pipeline through your system shell to verify win thresholds:
```bash
python main.py
