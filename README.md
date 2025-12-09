# 🛡️ UPI Fraud Detection Web App

A secure and intelligent web application to detect fraudulent UPI (Unified Payments Interface) transactions using machine learning. Built using Flask, PostgreSQL, and XGBoost, it supports multiple users with admin controls and visualizes predictions from uploaded CSV files.

🔗 **Live App**: [https://upi-fraud-db.onrender.com](https://upi-fraud-db.onrender.com)

---

## 🚀 Features

- 🔐 **User Authentication**: Register/Login for both regular users and admin.
- 📤 **CSV Upload**: Upload transaction records in bulk.
- 📊 **ML Predictions**: Real-time classification of transactions as `Fraud` or `Legit` using a trained XGBoost model.
- 📁 **Admin Dashboard**: Admin can view and delete all users' transactions.
- 👤 **User Dashboard**: Users can only view their own transactions.
- 📌 **Predefined CSV Template**: Example file provided inside the `/uploads` folder on GitHub.

---

## 🧠 Machine Learning Model

- **Model**: XGBoost Classifier  
- **Trained On**: UPI transaction dataset with features like `Amount`, `MerchantCategory`, `BankName`, `FailedAttempts`, etc.
- **Imbalance Handling**: SMOTE used for balancing fraud vs legit transactions during training.
- **Accuracy**: Achieved optimal results through hyperparameter tuning and feature engineering.

---

## 🛠️ Tech Stack

| Component       | Technology         |
|----------------|--------------------|
| Backend         | Flask (Python)     |
| ML Model        | XGBoost, Scikit-Learn |
| Database        | PostgreSQL         |
| ORM             | SQLAlchemy + Flask-Migrate |
| Deployment      | Render             |
| Auth            | Flask-Login        |

---

## 📂 Folder Structure

```
upi_fraud_db/
│
├── app.py                  # Main Flask app
├── helpers.py              # Preprocessing & encoding functions
├── models.py               # Database models (if separated)
├── templates/              # HTML templates
├── static/                 # CSS, JS (optional)
├── uploads/                # Sample CSVs to test
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment (Gunicorn)
└── .env                    # For environment variables
```

---

## 📄 Sample CSV Format

Use the template provided in the `uploads/` folder on this GitHub repo.  
Required headers:

```csv
Amount,MerchantCategory,TransactionType,Latitude,Longitude,AvgTransactionAmount,
TransactionFrequency,UnusualLocation,UnusualAmount,NewDevice,FailedAttempts,BankName
```

---

## 👨‍💻 How to Use (Locally)

```bash
# Clone the repository
git clone https://github.com/Azzanraj/upi_fraud_db.git
cd upi_fraud_db

# Create a virtual environment and activate it
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Set up environment variable for DB
echo DATABASE_URL=your_postgres_url > .env

# Run the app
flask run
```

---

## 🌐 Deployment

This app is deployed on **Render** using:
- PostgreSQL as the production database
- Gunicorn WSGI server via `Procfile`
- Environment variables via `.env` file (managed in Render settings)

Live Demo: [https://upi-fraud-db.onrender.com](https://upi-fraud-db.onrender.com)

---

## 👤 Admin Login

- **Username**: `admin`  
- **Password**: `admin`

> Admin can view/delete all users’ transactions.

---

## 📬 Contact

Made with 💻 by **Azzan Raj**

GitHub: [@Azzanraj](https://github.com/Azzanraj)

---

## 📜 License

This project is licensed under the MIT License.
