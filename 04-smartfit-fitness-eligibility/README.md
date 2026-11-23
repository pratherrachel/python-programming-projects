# SmartFit Fitness Program for New Customers Eligibility

This folder contains my **original Python code**, preserved without refactoring or functional improvements. The project is an introductory exercise in conditional statements and logical operators.

## What the program does

- Requests a customer age and displays the corresponding Teen, Regular, or Senior program.
- Asks for a yes/no medical-condition response and follows the exercise’s registration logic.
- Offers Basic or Premium membership when registration continues.
- For Basic membership, displays $45/month with personal training or $30/month without it.
- For Premium membership, displays $60/month and identifies customers under 30 as eligible for a youth discount, **without calculating a discounted price**.
- Offers a consultation message for Premium customers who answered yes to the medical-condition question and were allowed to continue.

## Run

From this directory:

```bash
python smartfit.py
```

Only the Python standard library is used; no additional packages are required.

## Notes on the original implementation

This is intentionally the original assignment code. Input validation is limited: entering a non-integer age will raise an error, and an invalid response does not trigger another prompt. The youth discount is announced but not applied to the price. The medical-condition questions and enrollment rules are **fictional exercise logic**, not medical advice or actual gym policy.
