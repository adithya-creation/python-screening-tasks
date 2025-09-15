# Python Screening Task 3 - Evaluating Open Source Models for Student Competence Analysis

This report contains my research plan and a small demo for using open-source AI models to support **competence analysis in Python learning**. The goal is to see whether models trained on code can go beyond bug detection and help generate meaningful prompts that test a student’s depth of understanding, highlight misconceptions, and encourage reflective thinking without simply handing out solutions.

---

## Research Plan

To approach this task, I first explored freely available open-source language models with a focus on **code understanding**. Models like **StarCoder** (BigCode) and **CodeGen** (Salesforce) stood out because they are trained on large-scale GitHub repositories, including Python, which makes them capable of analyzing student code. The criteria I used to assess suitability included:

1. Whether the model can interpret Python syntax and logic.
2. Its ability to generate prompts in natural language rather than just code fixes.
3. Licensing and availability for educational use.
4. Evidence from benchmarks or community usage that it can reason about programming tasks.

To validate their applicability, I would run them on **student-written Python snippets that contain typical misconceptions** (e.g., wrong base case in recursion, off-by-one loop errors, misuse of lists vs. sets and other syntax errors). I would then check if the model can generate prompts such as *“What should happen when n = 0 in factorial?”*. These outputs would be reviewed against **Bloom’s Taxonomy levels** and also judged by educators for depth of reasoning. The goal is not correctness alone but the ability to spark deeper understanding.

---

## Reasoning

- **What makes a model suitable?**
  A good model must understand both **code semantics** and **conceptual reasoning**, not just syntax. It should be able to translate raw Python code into meaningful educational feedback.

- **How to test meaningful prompts?**
  I would test models on code snippets with intentional mistakes and evaluate whether the generated prompts target *understanding* (e.g., “Why is the base case important in recursion?”) instead of just giving answers. Educator feedback and alignment with Bloom’s taxonomy can guide this evaluation.

- **Trade-offs:**
  Larger models like **StarCoder-15B** produce richer insights but require high compute. Smaller models (e.g., CodeBERT) are lighter and more interpretable but may miss deeper reasoning patterns. Static analyzers (like pylint) are transparent but can’t generate conceptual prompts. So, there’s a balance between **accuracy, interpretability, and cost**.

- **Model chosen (StarCoder):**
  I focused on **StarCoder** because it is open-source, trained extensively on real-world code, and capable of producing natural language explanations. Its strengths are strong Python understanding and adaptability for education. Its main limitation is high resource demand and occasional overconfidence in wrong answers.

**References:**

* [StarCoder on Hugging Face](https://huggingface.co/bigcode/starcoder)
* [CodeGen GitHub Repo](https://github.com/salesforce/CodeGen)

---

## Setup & Demo

You can try a simple demo to see how an open-source model can generate conceptual prompts for student-written Python code.

### 1. Install dependencies

```bash
pip install torch transformers
```

### 2. Run the demo

Save the following as `demo.py`:

```python
python demo.py
```

### 3. Expected behavior

The model should produce a question like:

> *“What should factorial(0) return according to the mathematical definition?”*

This shows how the model can encourage **reflection** rather than giving the final answer.
