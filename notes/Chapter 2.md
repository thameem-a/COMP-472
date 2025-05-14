# COMP-472: Artificial Intelligence (AIMA 4th Edition) - Chapter 2 Notes

# 🤖 Intelligent Agents (Explain like I'm 5)

## 📚 Outline

* What are Agents and Environments?
* What is Rationality?
* PEAS: Task Environments
* Different Environment Types
* Different Agent Types

---

## 👀 Agents and Environments

Imagine you are playing a video game. You see things (through your screen) and you press buttons to move your character. **You are an agent!**

* **Agent:** Something that can look at the world (using sensors) and do stuff (using actuators).
* **Examples:** Humans, robots, software programs, even a thermostat!

An agent gets information (**percepts**) from the **environment** and does **actions**.

**Simple example:**

* Sensors: Eyes and ears.
* Actuators: Hands and feet.

The agent follows a rule: **"If I see X, I do Y."**

## 🤔 Vacuum Cleaner World

Imagine a little robot whose only job is to clean dirty squares:

* **Percepts:** Where it is (A or B) and whether it's dirty.
* **Actions:** Move Left, Move Right, Suck dirt, Do Nothing.

A very simple "smart" vacuum can follow a tiny rule:

```plaintext
If dirty → Suck
Else if at A → Move Right
Else if at B → Move Left
```

But... is this vacuum really smart? Not really 😅. It just follows simple rules blindly!

## 🤔 What is Rationality?

**Rational = Doing the right thing!**

How do we know if an agent is doing the right thing?

* We **check the results** of what it does.

Example: If there's smoke, a smart agent runs to call help. A silly agent plays with the smoke.

We judge smartness using a **Performance Measure**:

* How clean the floor is?
* How safe the building is?
* How happy the customer is?

**Super Duper Vacuum Cleaner:**

* 1 point for each clean square!
* Or, 1 point for being clean and minus points for unnecessary moves!

**Important:**

> A rational agent picks actions that make the world the best it can be, according to what it knows.

## 🔢 Rationality Depends on 4 Things

1. **Performance Measure**: What is considered "good".
2. **Knowledge of the World**: What the agent already knows.
3. **Possible Actions**: What the agent can do.
4. **Percept Sequence**: What the agent has seen so far.

## 💚 PEAS Framework

PEAS = Performance, Environment, Actuators, Sensors.

When building an agent, we think about:

**Example: Self-driving car**

* **Performance:** Safe driving, quick trips, comfort.
* **Environment:** Streets, traffic, weather.
* **Actuators:** Wheels, brakes, horn.
* **Sensors:** Cameras, GPS, speed sensors.

**Example: Internet Shopping Agent**

* **Performance:** Finds cheap and good stuff fast.
* **Environment:** Online shops.
* **Actuators:** Clicking buttons, filling forms.
* **Sensors:** Reading web pages.

## 🌐 Types of Environments

**Fully Observable vs Partially Observable**

* Fully observable: See everything (like chess).
* Partially observable: Only see parts (like driving in fog).

**Single-Agent vs Multi-Agent**

* Single: Just one (vacuum cleaner).
* Multi: Many players (chess, cars on the road).

**Deterministic vs Nondeterministic**

* Deterministic: Predictable (board games).
* Nondeterministic: Unpredictable (weather).

**Stochastic vs Nondeterministic**

* Stochastic: With probabilities ("20% chance of rain").
* Nondeterministic: No probabilities, just unknown.

**Episodic vs Sequential**

* Episodic: One job at a time (quality check on a line).
* Sequential: Every move matters for the future (chess).

**Static vs Dynamic**

* Static: World stands still.
* Dynamic: World changes while you think!

**Discrete vs Continuous**

* Discrete: Step-by-step (chess).
* Continuous: Smooth (driving a car).

**Known vs Unknown**

* Known: Rules are clear (chess).
* Unknown: Rules must be discovered (new video game).

## 👨‍💻 Types of Agents

### 1. Simple Reflex Agents

* Do actions based only on what they see now.
* Like: "If I see dirt, suck!"
* **No thinking ahead.**

### 2. Model-Based Reflex Agents

* Remember past information!
* Build a little "mental model" of the world.
* Smarter than simple reflex agents.

### 3. Goal-Based Agents

* Have a goal.
* Think: "Will this action help me reach my goal?"
* Example: A GPS finding the fastest route.

### 4. Utility-Based Agents

* Not just reaching goals, but **being happy** too!
* Think: "Which action will make me happiest?"
* Example: Choosing not just the shortest road but the safest too.

## 📈 Learning Agents

* Can learn and get better over time!
* Watch results, learn from mistakes, improve.
* Like humans getting better after practice!

Learning Agents have:

* **Performance Element**: Does stuff.
* **Learning Element**: Learns from experience.
* **Critic**: Tells how good or bad the job was.
* **Problem Generator**: Suggests new experiences.

---

## 🔍 Final Summary

* Agents **sense** the world and **act** on it.
* Good agents act **rationally** based on what they know and see.
* Designing agents needs thinking about **PEAS**.
* **Environment types** matter: Is it known? Static? Multi-agent?
* Different kinds of agents exist: **simple, model-based, goal-based, utility-based, learning agents**.

---

*Notes based on AIMA 4th Edition, Chapter 2*【35†source】
