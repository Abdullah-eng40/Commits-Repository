import os
import random
import subprocess
from datetime import datetime, timedelta

# Terminal colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# 1,095 days = 3 years back (fills 2023, 2024, 2025, and 2026)
days_back = 1095       
start_date = datetime.now() - timedelta(days=days_back)

# --- ROLE-SPECIFIC COMMIT MESSAGES (Natural Progression) ---
# Year 1 (Days 0-365): Flutter & MERN Stack Era
MERN_FLUTTER_COMMITS = [
    "Init Express.js server backend with MongoDB connection clusters",
    "Implement JWT stateless authentication and HTTP-only cookie storage",
    "Add Redux Toolkit slices for global user state management",
    "Optimize Mongoose aggregation pipelines for dashboard metrics",
    "Fix memory leak in React useEffect cleanup listeners",
    "Build reusable custom hooks for form validation and API polling",
    "Integrate Stripe Webhooks for seamless subscription lifecycle events",
    "Configure Tailwind custom theme extensions and dark mode variants",
    "Implement Flutter BloC architecture for reactive state streams",
    "Fix layout overflow constraints on iOS small-factor screens",
    "Integrate native secure storage plugin for local encrypted tokens",
    "Configure push notification payloads with Firebase Cloud Messaging",
    "Optimize Flutter build sizes by shrinking asset resource bundles"
]

# Year 2 (Days 366-730): Cloud Data Engineering Era
CLOUD_DATA_COMMITS = [
    "Write PySpark ETL job to aggregate streaming transactional logs",
    "Deploy Terraform configurations for multi-AZ RDS infrastructure",
    "Configure Apache Airflow DAGs with custom backfill schedules",
    "Optimize Snowflake warehouse compute clusters for heavy analytical loads",
    "Build dbt models for dimensional data warehousing transformations",
    "Implement AWS Lambda triggers for automated S3 file ingestion",
    "Configure Kafka topic replication factors and partition strategies",
    "Migrate legacy relational tables to highly scalable DynamoDB",
    "Optimize Dockerfile build layers to reduce container image footprint",
    "Implement Kubernetes horizontal pod autoscaling for ingestion workers",
    "Add Great Expectations validation suites to core data pipelines",
    "Configure IAM roles with strict principle of least privilege access"
]

# Year 3 (Days 731-1095): AI/ML & Data Science Era
AI_ML_DATA_SCIENCE_COMMITS = [
    "Train PyTorch ResNet model with customized learning rate schedulers",
    "Implement data augmentation pipelines using Albumentations",
    "Configure MLflow experiments tracking parameters and validation metrics",
    "Optimize BERT transformer inference speed using ONNX Runtime",
    "Build custom data preprocessing tokenizers for NLP datasets",
    "Deploy FastAPI endpoint to serve real-time model predictions",
    "Implement vector database indexing using FAISS for semantic search",
    "Fine-tune hyperparameters using Optuna Bayesian search optimization",
    "Build automated CI/CD evaluation checks for model drift tracking",
    "Implement isolation forests for unsupervised anomaly detection",
    "Convert tabular models to XGBoost to accelerate feature engineering",
    "Fix gradient exploding issue by introducing gradient clipping thresholds"
]

print(f"\n{RED}🚨 INJECTING 3-YEAR MULTI-ROLE CAREER PORTFOLIO...{RESET}\n")

custom_env = os.environ.copy()

for i in range(days_back + 1):
    current_date = start_date + timedelta(days=i)
    weekday = current_date.weekday()
    
    # 1. Distribute messages dynamically across the 3-year timeline
    if i <= 365:
        pool = MERN_FLUTTER_COMMITS
        role_label = "MERN/Flutter"
    elif i <= 730:
        pool = CLOUD_DATA_COMMITS
        role_label = "Cloud Data"
    else:
        pool = AI_ML_DATA_SCIENCE_COMMITS
        role_label = "AI/ML/DataSci"

    # 2. Weekday/Weekend natural activity distribution
    if weekday < 5:  # Monday to Friday
        is_active_day = random.random() > 0.15  # 85% chance of activity
        max_commits = 6
    else:            # Saturday and Sunday
        is_active_day = random.random() > 0.85  # 15% chance of activity
        max_commits = 2
        
    if is_active_day:
        daily_commits = random.randint(1, max_commits)
        
        for _ in range(daily_commits):
            # Scramble hours between standard waking windows
            hour = random.randint(8, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            commit_time = current_date.replace(hour=hour, minute=minute, second=second).strftime("%Y-%m-%dT%H:%M:%S")
            
            custom_env["GIT_COMMITTER_DATE"] = commit_time
            custom_env["GIT_AUTHOR_DATE"] = commit_time
            
            msg = random.choice(pool)
            
            subprocess.run(
                ["git", "commit", "--allow-empty", "-m", msg], 
                env=custom_env, 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            
        print(f"{GREEN}🟩 [{role_label}] Planted {daily_commits} commits on: {commit_time[:10]}{RESET}")
    else:
        print(f"{YELLOW}⬜ Skipping (Rest Day) on: {current_date.strftime('%Y-%m-%d')}{RESET}")

print(f"\n{RED}🔥 Massive, multi-role 3-year history completely staged!{RESET}")
print(f"👉 Push to GitHub using: {GREEN}git push -u origin main --force{RESET}\n")
