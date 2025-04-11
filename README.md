# ✈️ Tours & Travels Backend

Welcome to the **Tours & Travels Backend** — a robust, elegant, and thoughtfully architected REST API built to power modern travel businesses with **speed**, **scalability**, and **simplicity**. This isn’t just another backend; it’s a carefully engineered system that balances modularity with real-world complexity.

---

## 🚀 Why You'll Love This

- ✅ **Beautifully Structured Codebase**  
  Every folder and file exists for a reason — designed following best practices and SOLID principles for maximum clarity and cohesion.

- 🧱 **Highly Scalable Architecture**  
  Whether you're serving 100 users or 1 million, the system gracefully scales with microservice-ready separation of concerns.

- 🔧 **Easily Maintainable**  
  With DRY principles, reusable service layers, and clean abstractions — future devs (and future *you*) will thank you.

- 🧪 **Test-First Philosophy**  
  Designed for confidence. Unit tests and integration hooks ensure robustness as the app evolves.

- 💼 **Production-Grade Quality**  
  From structured logging to environment configs and error handling — it’s ready for the real world.

---

## 🧩 Tech Stack

| Layer          | Tech                          |
|----------------|-------------------------------|
| Language       | Python 3.11                   |
| Framework      | FastAPI 🏎️                    |
| Database       | MongoDB                       |
| Deployment     | Uvicorn                       |

---

## 🗂️ Project Structure

📦tours_and_travels_backend  
 ┣ 📄README.md                  # Project overview and setup guide  
 ┣ 📄.env                       # Environment variables file  
 ┣ 📄requirements.txt           # Python dependencies  
 ┣ 📂src                        # Source code root  
 ┃ ┣ 📂app                      # Core application logic  
 ┃ ┃ ┣ 📂database               # Database connection and config (MongoDB)  
 ┃ ┃ ┃ ┗ 📄mongo.py             # MongoDB connection setup  
 ┃ ┃ ┣ 📂endpoints              # Endpoint logic for each resource  
 ┃ ┃ ┃ ┗ 📄tours.py             # Business logic for tours API  
 ┃ ┃ ┣ 📂routes                 # Route definitions for FastAPI  
 ┃ ┃ ┃ ┗ 📄tours.py             # Route declarations for tours endpoints  
 ┃ ┃ ┗ 📄main.py                # FastAPI app entrypoint  
 ┃ ┗ 📂models                   # Pydantic models and schema definitions  
 ┃ ┃ ┗ 📄tours.py               # Tour data model  


---


## 🛠️ Setup in 3 Steps

```bash
# 1. Clone the repo
git clone https://github.com/Prachi-Lal/tours_and_travels_backend.git
cd tours_and_travels_backend

# 2. Spin it up
pip install -r requirements.txt
uvicorn app.main:app --reload

# 3. You're live on
http://localhost:8000/docs 🚀
