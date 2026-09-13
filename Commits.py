import os
import random
import subprocess
from datetime import datetime, timedelta

# Terminal colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Configurations
days_back = 1096       # Timeframe length
start_date = datetime.now() - timedelta(days=days_back)

# Realistic commit messages to pull from randomly
COMMIT_MESSAGES = [
    "Refactor module architecture",
    "Fix edge case in data parsing pipeline",
    "Update README with deployment instructions",
    "Optimize database query performance",
    "Add unit tests for authentication helpers",
    "Clean up unused dependencies",
    "Fix styling and layout responsiveness",
    "Implement error boundary for API fallbacks"
]

print(f"\n{RED}🚨 GENERATING NATURAL CONTRIBUTIONS...{RESET}\n")

custom_env = os.environ.copy()

# Step 1: Loop through the timeline
for i in range(days_back + 1):
    current_date = start_date + timedelta(days=i)
    formatted_date = current_date.strftime("%Y-%m-%dT%H:%M:%S")
    weekday = current_date.weekday()  # 0=Monday, 6=Sunday
    
    # Step 2: Determine natural probability based on the day
    # Weekdays have a 15% chance of zero activity; Weekends have an 85% chance of zero activity.
    if weekday < 5:  
        is_active_day = random.random() > 0.15
        max_commits = 7  # High potential for multi-shade green days
    else:            
        is_active_day = random.random() > 0.85
        max_commits = 2  # Low activity on weekends
        
    if is_active_day:
        # Generate a random number of commits for this day
        daily_commits = random.randint(1, max_commits)
        
        for _ in range(daily_commits):
            # Pick a dynamic timestamp during standard waking hours (9 AM - 10 PM)
            hour = random.randint(9, 22)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            commit_time = current_date.replace(hour=hour, minute=minute, second=second).strftime("%Y-%m-%dT%H:%M:%S")
            
            custom_env["GIT_COMMITTER_DATE"] = commit_time
            custom_env["GIT_AUTHOR_DATE"] = commit_time
            
            # Select a random realistic message
            msg = random.choice(COMMIT_MESSAGES)
            
            subprocess.run(
                ["git", "commit", "--allow-empty", "-m", msg], 
                env=custom_env, 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            
        print(f"{GREEN}🟩 Planted {daily_commits} natural commits for: {formatted_date[:10]}{RESET}")
    else:
        # Keeps empty squares on your grid so it doesn't look like a solid wall
        print(f"{YELLOW}⬜ Skipping (Rest Day): {formatted_date[:10]}{RESET}")

print(f"\n{RED}🔥 Natural history staged!{RESET}")
print(f"👉 Push to a clean repo: {GREEN}git push -u origin main --force{RESET}\n")
