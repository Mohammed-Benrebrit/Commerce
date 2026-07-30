# Commerce: E-Commerce & Auction Platform

A robust, eBay-like e-commerce and auction application built with Python and Django.

Engineered as a core component of **Harvard's CS50**, this project focuses on complex relational database design, transactional logic, and user state management. As I transition into advanced **Artificial Intelligence and Machine Learning** (currently completing **Stanford's ML specialization**), mastering these backend data pipelines is essential. Building secure, transactional platforms provides the underlying infrastructure required to deploy intelligent, data-driven applications in real-world retail and e-commerce environments.

### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### 🧠 Architecture & Core Features

This platform handles continuous user inputs, strict data validation, and multi-table database queries to ensure auction integrity.

*   **Transactional Bidding Engine:** Implements strict backend validation (`views.py`) to ensure new bids exceed the current highest bid before writing to the database, preventing invalid data entry.
*   **Relational Data Modeling:** Utilizes Django's ORM (`models.py`) with 5 interconnected tables (`User`, `listing`, `bids`, `comment`, `selled`) managing foreign keys and cascading deletions for data integrity.
*   **Stateful User Watchlists:** Enables users to save active listings to a personalized watchlist using boolean toggles that instantly update database records and DOM rendering.
*   **Auction Resolution Logic:** Features an administrative function for listing creators to close auctions, automatically transferring the item to the highest bidder's `selled` dashboard and removing it from the active query set.
*   **Dynamic Categorization:** Parses the database to dynamically generate category pages, filtering large datasets into specific retail sectors.

### 💻 Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mohammed-Benrebrit/Commerce.git](https://github.com/Mohammed-Benrebrit/Commerce.git)
   cd Commerce
