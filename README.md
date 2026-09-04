# PassGuard: Password Vulnerability & Entropy Analyzer

## 1. Project Title
**PassGuard: Cryptographic Entropy & Password Vulnerability Assessment Tool**

---

## 2. Problem Statement
Users routinely generate weak, repetitive, or dictionary-based passwords, exposing systems to credential stuffing, dictionary attacks, and high-speed offline hash cracking.

---

## 3. Objective
To construct a lightweight, privacy-focused security tool that analyzes password resilience using Shannon entropy calculations, character set diversity analysis, and common pattern detection while providing actionable recommendations.

---

## 4. Proposed Solution
A modular Python utility that evaluates password keyspace mathematically, flags predictable keyboard sequences and repeating characters, checks against known dictionary wordlists, and estimates brute-force resistance without storing or leaking sensitive inputs.

---

## 5. Tech Stack
* **Language:** Python
* **Libraries:** Standard Library (`math`, `re`, `getpass`) - zero third-party dependencies to minimize supply chain attack surface.

---

## 6. Implementation Approach
1. **Shannon Entropy Calculation:** Computes information entropy via $H = L \cdot \log_2(R)$ where $L$ is password length and $R$ is character pool size.
2. **Predictable Sequence Detection:** Regular expressions identify consecutive identical characters and standard keyboard sequences (`123`, `qwerty`, `abc`).
3. **Character Pool Diversity:** Audits uppercase, lowercase, numbers, and special symbols.
4. **Dictionary Lookup:** Performs offline comparisons against common weak password lists.
5. **Secure Input Handling:** Uses `getpass` to mask terminal input and eliminate shoulder surfing.

---

## 7. Security Considerations
* **Zero Disk Retention:** Inputs reside strictly in volatile memory and are cleared after analysis.
* **Input Masking:** Passwords are not echoed to stdout or terminal histories.
* **Synthetic Data Only:** Built strictly for testing sample/synthetic passwords in compliance with responsible security evaluation guidelines.

---

## 8. Testing & Results

| Test Case | Sample Input | Expected Rating | Observed Rating | Status |
| :--- | :--- | :--- | :--- | :--- |
| Common Breached Word | `password123` | CRITICAL / VERY WEAK | CRITICAL / VERY WEAK | ✅ PASS |
| Sequential Numbers | `12345678` | CRITICAL / VERY WEAK | CRITICAL / VERY WEAK | ✅ PASS |
| Repeated Characters | `aaaaaa111` | WEAK | WEAK | ✅ PASS |
| Moderate Complexity | `Summer@2024` | MODERATE | MODERATE | ✅ PASS |
| High Complexity Passphrase | `kP9#mX2$vL8!qZ` | VERY STRONG | VERY STRONG (94.2 bits) | ✅ PASS |

---

## 9. Screenshots / Demo
*(Terminal execution demo outputs showing multiple test scenarios)*

```text
==================================================
  PassGuard: Password Vulnerability & Entropy Tool
==================================================
Enter sample password to analyze (masked input): 

------------------------------
[+] Security Rating : CRITICAL / VERY WEAK
[+] Shannon Entropy : 18.0 bits
------------------------------

[ Analysis / Risk Factors ]
 • Password found in common breach/dictionary lists.
 • Contains predictable keyboard sequences or numbers.
 • Missing character classes: Uppercase letters, Special characters.

[ Recommendations ]
 • Never use default dictionary words or common phrases.
 • Remove predictable sequential patterns.
 • Include Uppercase letters, Special characters to broaden keyspace.
==================================================

```

 ## 10. How to Run
  Clone the repository:
   git clone [https://github.com/LingeshN004/PassGuard.git](https://github.com/LingeshN004/PassGuard.git)
   cd PassGuard

## 11. Limitations
1. Entropy calculations assume uniform character distribution across the keyspace.
2. Operates strictly as an offline tool; does not query external third-party breach APIs to avoid data exposure.

## 12. Future Improvements
1. Add a k-Anonymity API integration (e.g., HaveIBeenPwned API) for secure live hash checks.

2. Implement an offline Bloom filter pre-loaded with common compromised password hashes.

3. Build a local GUI interface using Tkinter or Streamlit for non-technical users.

## 13. AI / External Resources Used
1. NIST SP 800-63B (Digital Identity Guidelines Authentication and Lifecycle Management).

2. Python standard library documentation (math, re, getpass).

3. LLMs(Claude/Gemini) for structuring documentation templates and validating regex patterns.
