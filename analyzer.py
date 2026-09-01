import math
import re
import getpass

# Optional: Load common passwords from a local text file
COMMON_PASSWORDS = {"password", "123456", "admin", "welcome", "qwerty", "12345678", "password123"}

def calculate_entropy(password):
    pool_size = 0
    if re.search(r'[a-z]', password): pool_size += 26
    if re.search(r'[A-Z]', password): pool_size += 26
    if re.search(r'[0-9]', password): pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): pool_size += 32

    if pool_size == 0 or len(password) == 0:
        return 0
    return len(password) * math.log2(pool_size)

def analyze_password(password):
    reasons = []
    recommendations = []
    
    # 1. Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        reasons.append("Password is present in known common breach lists.")
        recommendations.append("Never use dictionary words or standard default passwords.")

    # 2. Length Check
    if len(password) < 8:
        reasons.append(f"Password length ({len(password)}) is too short.")
        recommendations.append("Increase length to at least 12-16 characters.")
    elif len(password) >= 14:
        reasons.append("Good length provides high resistance to brute-force.")

    # 3. Predictable Patterns & Repetition
    if re.search(r'(.)\1\1', password):
        reasons.append("Contains 3 or more repeated consecutive characters.")
        recommendations.append("Avoid consecutive repeating characters.")
    if re.search(r'123|abc|qwerty|admin', password.lower()):
        reasons.append("Contains common predictable sequences.")
        recommendations.append("Remove predictable keyboard or number sequences.")

    # 4. Diversity
    missing_sets = []
    if not re.search(r'[A-Z]', password): missing_sets.append("Uppercase letters")
    if not re.search(r'[a-z]', password): missing_sets.append("Lowercase letters")
    if not re.search(r'[0-9]', password): missing_sets.append("Numbers")
    if not re.search(r'[^a-zA-Z0-9]', password): missing_sets.append("Special symbols")

    if missing_sets:
        reasons.append(f"Missing character types: {', '.join(missing_sets)}.")
        recommendations.append(f"Include {', '.join(missing_sets)} to increase complexity.")

    # 5. Calculate Score & Rating
    entropy = calculate_entropy(password)
    if entropy < 30 or password.lower() in COMMON_PASSWORDS or len(password) < 6:
        rating = "CRITICAL / VERY WEAK"
    elif entropy < 50:
        rating = "WEAK"
    elif entropy < 70:
        rating = "MODERATE"
    elif entropy < 90:
        rating = "STRONG"
    else:
        rating = "VERY STRONG"

    return {
        "rating": rating,
        "entropy_bits": round(entropy, 2),
        "reasons": reasons,
        "recommendations": recommendations
    }

if __name__ == "__main__":
    print("=== PassGuard: Password Security Analyzer ===")
    sample_pwd = getpass.getpass("Enter sample password to analyze (input is masked): ")
    
    result = analyze_password(sample_pwd)
    print(f"\n[+] Assessment: {result['rating']}")
    print(f"[+] Entropy Score: {result['entropy_bits']} bits")
    
    print("\n--- Assessment Reasons ---")
    for r in result['reasons']:
        print(f" • {r}")
        
    print("\n--- Recommendations ---")
    for rec in result['recommendations']:
        print(f" • {rec}")
