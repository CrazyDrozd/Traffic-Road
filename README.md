# Traffic-Road

> *"Architecture should speak of its time and place, but yearn for timelessness."*  
> — **Frank Gehry**

## 🚧 About the Project

At present, **Traffic-Road** is a clean, modular template for future PyGame projects.  
It was built as a pet project to practice **SOLID principles**, **software architecture patterns**, and to get comfortable with Robert C. Martin's coding style and best practices.

The ultimate goal is to evolve this into a reusable, well-architectured foundation that can be used daily for game development in Python.

---

## ✨ Key Features & Practices

| Concept | How it's used |
|---------|----------------|
| **OOP** | Core structure – everything is object-oriented. |
| **Interfaces** | Abstract base classes & methods to enforce contracts. |
| **Modularisation** | Code split into small, logical files inside `/data` with proper `__init__.py` exports, inheritance, and imports. |
| **Dataclasses** | Used primarily for main project configuration. |
| **Logging** | Simple but effective logging system – ready for error handling and debugging. |
| **Docstrings** | Detailed explanations for every class and method (visible on hover in most IDEs). |
| **Type Hints** | Explicit type annotations to prevent `TypeError`s and improve maintainability. |
| **Containerisation** | Basic Dockerfile included (not yet fully tested) for easy containerised execution. |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 — 3.12
- PyGame (install via `pip install pygame`)

### Installation
```bash
git clone https://github.com/yourusername/Traffic-Road.git
cd Traffic-Road
pip install -r requirements.txt   # if you have one, otherwise install pygame manually
```

---

## 🧠 What I've Learned (so far)
* Applying SOLID in a real (small) Python project

* Using abstract classes to mimic interfaces

* Keeping a clean module structure with __init__.py

* Writing self-documenting code via docstrings + type hints

* Thinking ahead with logging and error handling

* Experimenting with Docker

---

## 🔮 Future Plans
* Turn this into a production-ready architecture for daily use

* Add unit tests 

* Implement actual traffic/road simulation logic

* Fully test and polish Docker support

