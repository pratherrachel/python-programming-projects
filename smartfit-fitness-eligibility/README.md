# SmartFit Fitness Membership Eligibility

An interactive Python command-line project demonstrating **conditional logic, logical operators, input validation, functions, and basic pricing calculations**. Developed from an introductory programming exercise and refactored for readability and testability.

## What the program does

1. Requests a customer's age and assigns an age-based fitness program.
2. Asks for a yes/no medical-condition response and applies a **fictional enrollment policy**.
3. If registration can continue, offers **Basic** and **Premium** memberships.
4. Asks whether Basic customers want personal training.
5. Calculates the monthly price and applies a **10% youth discount** to Premium customers under age 30.
6. Displays plan-specific information.

## Eligibility and pricing

| Condition | Result |
|---|---|
| Under 18 | Teen Fitness Program |
| 18–40 | Regular Fitness Program |
| Over 40 | Senior Wellness Program |
| Age 40 or older **and** answers yes to medical-condition question | Example policy requires medical clearance before registration |

| Membership | Monthly price |
|---|---:|
| Basic | $30.00 |
| Basic + personal training | $45.00 |
| Premium | $60.00 |
| Premium for customers under 30 | $54.00 (10% discount) |

**Important:** These enrollment rules are illustrative requirements from a programming exercise, **not medical advice, clinical screening, or real-world safety guidance**. The program does not collect diagnoses or save medical information.

## Run locally

Requires Python 3.9 or newer and no external packages.

```bash
python smartfit.py
```

## Run tests

From the project folder:

```bash
python -m unittest discover -s tests -v
```

## Skills demonstrated

- `if` / `elif` / `else` and nested conditional logic
- Boolean expressions using `and` / `not`
- Input validation with loops and exception handling
- Functions, return values, and basic unit tests
- Formatted output with f-strings

## Potential improvements

- Offer multiple membership selections and a summary receipt.
- Add a GUI or web interface.
- Separate user interaction from business rules further.
- Replace illustrative eligibility rules with appropriate real-world processes if adapting beyond coursework.

## Attribution

Refactored from the author's SmartFit introductory Python programming exercise.
