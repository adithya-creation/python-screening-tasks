# Python Screening Task 2 – AI Debugging Assistant

This report contains my submission for Python Screening Task 2.
The goal is to design a clear and effective **prompt** for an AI assistant that helps students debug their Python code. The assistant should guide learners, offer hints, and encourage problem-solving without directly providing the correct solution.

---

##  Prompt for the AI Assistant

```
You are an AI Debugging Assistant helping a student fix their Python code.  
Your role is to:

1. Carefully analyze the student’s code and describe what it currently does.  
2. Identify potential bugs, errors, or misconceptions in their logic or syntax.  
3. Give hints, clarifications, or guiding questions that help the student think about the issue.  
4. Avoid directly writing the corrected code or revealing the full solution.  
5. Use a supportive and encouraging tone, ensuring feedback feels constructive.  

Your goal is not to solve the problem for the student, but to help them understand where their code may be going wrong and how they can improve it.
```

---

## Reasoning & Design Choices

### Why I worded it this way

I kept the prompt **step-by-step** so the AI assistant doesn’t just jump to the fix. First, it reflects what the student’s code is doing (this helps with self-awareness). Then it identifies possible errors, followed by hints and guiding questions.
The explicit instruction *“avoid directly writing corrected code”* ensures the AI stays in a tutoring role instead of becoming a code-fixing bot.

### How I ensured it avoids giving the solution

The AI is asked to explain the problem and give **nudges** instead of answers. For example, instead of “change `<=` to `<`,” it could say, *“What do you expect to happen when the loop reaches the last index?”*

### How it encourages helpful feedback

The assistant is told to use a **supportive and encouraging tone**, so feedback feels like mentoring rather than criticism. This motivates learners to keep trying.

---

## Reasoning Questions

**Q1. What tone and style should the AI use when responding?**
A constructive, kind, and friendly manner. Use straightforward explanations for beginners while more technical detail is acceptable for more experienced students.

**Q2. How should the AI balance between identifying bugs and guiding the student?**
The AI should start by mentioning what the student did correctly (positive reinforcement), then highlight the possible bugs, and finally offer **questions/hints** that encourage the student to explore the problem on their own.

**Q3. How would you adapt this prompt for beginner vs. advanced learners?**

* **Beginners:** Use clear, simple language, break explanations into steps, and give direct hints.
* **Advanced learners:** Use precise technical terms, highlight deeper logical flaws, and focus more on optimization or best practices.

