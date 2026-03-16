# AI4SE-Testing-Forge ðŸ› ï¸ðŸ¤–
**Intelligent AI-Driven Software Testing Framework**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/)
[![AI4SE](https://img.shields.io/badge/AI-Software_Engineering-green.svg)](https://github.com/AI-DimitrisRentas)

## **Project Overview**
**AI4SE-Testing-Forge** is an industrial-scale framework designed to revolutionize the software testing lifecycle through **Artificial Intelligence for Software Engineering (AI4SE)**. 

Inspired by my research and implementation at **Ericsson Research**, this framework leverages **Large Language Models (LLMs)** and **Machine Learning** to automate test code generation and optimize test case selection within complex CI/CD environments.

---

## **Key Architecture**
The framework consists of two core components:
1.  **`IntelligentTestSelector`**: A Machine Learning engine (Random Forest based) that predicts test failures based on code change patterns, reducing execution time and resource consumption.
2.  **`LLMTestGenerator`**: A module demonstrating the integration of fine-tuned LLMs (e.g., Mixtral 8x7B) for generating high-quality Java/JUnit test code from natural language requirements.

---

## **Features**
-   ðŸ“ˆ **Predictive Regression Testing**: Intelligently select test cases that are most likely to fail based on recent commits.
-   âœï¸ **Automated Test Generation**: Convert user requirements directly into executable test code using generative AI.
-   âš–ï¸ **Flakiness Reduction**: Foundation for analyzing non-deterministic test results through log-based embedding analysis.
-   ðŸ­ **Industrial Integration**: Designed for high-scale environments where efficiency and quality are paramount.

---

## **Installation**

Clone the repository and install dependencies:

```bash
git clone https://github.com/AI-DimitrisRentas/AI4SE-Testing-Forge.git
cd AI4SE-Testing-Forge
pip install -r requirements.txt
```

---

## **Example Usage**

```python
from test_selector import IntelligentTestSelector
from llm_test_gen import LLMTestGenerator

# 1. Predictive Test Selection
selector = IntelligentTestSelector()
# Train on historical change logs and test results
selector.train_on_history(["fix: core parser update"], [1])
# Predict risk for current change
risk = selector.predict_impact(["refactor: modify parsing logic"])
print(f"Test Selection Risk: {risk['risk_score']}")

# 2. Automated Code Generation
generator = LLMTestGenerator()
test_code = generator.generate_test_case("Check if the database connection resets on timeout.")
print(f"Generated Code:\n{test_code['generated_code']}")
```

---

## **Why This Project?**
This project represents a synthesis of my professional work in **Industrial AI Research**. By combining **Large Language Models** with **Static Program Analysis**, we can achieve levels of automation and precision that were previously impossible. It showcases how AI can be a "force multiplier" for software quality and development speed.

---

## **Connect & Contribute**
I am always open to collaborating on AI research, LLM fine-tuning, and the future of Software Engineering.

-   **LinkedIn:** [Dimitris Rentas](https://www.linkedin.com/in/dimitris-rentas-224406259/)
-   **Portfolio:** [AI-DimitrisRentas](https://github.com/AI-DimitrisRentas)

---

> "Integrating intelligence into the very core of our development lifecycles."

---
*Disclaimer: This framework is a conceptual demonstration based on published research and industrial practices.*
