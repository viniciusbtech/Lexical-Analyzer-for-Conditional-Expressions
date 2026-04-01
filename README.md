# Lexical-Analyzer-for-Conditional-Expressions
This project implements a lexical analyzer (lexer) in Python to recognize tokens from a conditional statements language.

# 🔹 Conditional Statements Lexer in Python

This project implements a **lexical analyzer (lexer)** in Python to recognize tokens from a conditional statements language.

---

## 📌 Recognized Tokens

Tokens are displayed in the format:



### ✅ Supported Types

- **Keywords:** `IF`, `THEN`, `ELSE`  
- **Identifiers:** sequences starting with a letter (`ID`)  
- **Numbers:** integers, decimals, and exponential notation (`NUMBER`)  

- **Relational Operators (`RELOP`):**
  - `<` → LT  
  - `<=` → LE  
  - `>` → GT  
  - `>=` → GE  
  - `=` → EQ  
  - `<>` → NE  

- **EOF:** end of input  

---

## ⚙️ How It Works

The lexer processes the input **character by character**, using lookahead to recognize patterns.

- Whitespace is ignored  
- Identifiers are distinguished from keywords  
- Relational operators are recognized using lookahead  
- Numbers support:
  - Integer
  - Decimal
  - Scientific notation (e.g., `5E-3`)

---

## ▶️ Execution

Run in the terminal:


if x = 10 then 5E-3 > y else z <= y


<IF, None>
<ID, x>
<RELOP, EQ>
<NUMBER, 10.0>
<THEN, None>
<NUMBER, 0.005>
<RELOP, GT>
<ID, y>
<ELSE, None>
<ID, z>
<RELOP, LE>
<ID, y>
<EOF, None>

```bash
py lexer.py input.txt
