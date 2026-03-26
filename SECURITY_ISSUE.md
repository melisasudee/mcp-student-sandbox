# 🚨 Security Issue: Hardcoded AWS Credentials in Repository

## Issue Title
**CRITICAL: Hardcoded AWS Secret Key Exposed in `secret_leak.py`**

## Severity
🔴 **CRITICAL** - Security Vulnerability

## Description
The repository contains hardcoded AWS credentials in plain text within the source code. This poses a significant security risk even if the key shown is a "FAKE_KEY" for demonstration purposes.

### Specific Vulnerability:
```python
# File: secret_leak.py (Line 1)
AWS_SECRET_KEY = "AKIA_FAKE_KEY_123456789_STUDENT_TEST"
```

### Risk Assessment:
- ✗ **Credentials in version control** - Visible to anyone with repo access
- ✗ **Git history** - Credentials persisted in commit history (cannot simply delete file)
- ✗ **No .gitignore** - No protection against accidental secret commits
- ✗ **Credentials in logs** - Credentials leaked via print statements in stdout/logs
- ✗ **No secret rotation** - If real credentials were exposed, rotation would be complex

## Impact
- If this were a real key, **any attacker with repo access could**:
  - Compromise AWS infrastructure
  - Access databases and data
  - Incur AWS costs maliciously
  - Encrypt/delete critical resources

- **All developers** have implicit access to credentials
- **Third-party services** (CI/CD, deployment platforms) download full repo with credentials

## Root Causes
1. Lack of `.gitignore` configuration
2. No environment variable management
3. No secret detection in pre-commit hooks
4. No developer guidance on credential handling

## Solution (Recommended)

### ✅ Short Term (Immediate)
1. **Rotate the key** (if real)
2. **Remove credentials from code** (use environment variables)
3. **Apply .gitignore** to prevent future leaks
4. **Rewrite git history** (BFG Repo-Cleaner or git-filter-branch)

### ✅ Long Term (Process)
1. Implement `.gitignore` with `.env` patterns
2. Use `python-dotenv` for environment management
3. Setup pre-commit hooks (detect-secrets)
4. Use secret management services (AWS Secrets Manager, HashiCorp Vault)
5. Enable branch protection and code review
6. Add security scanning to CI/CD pipeline

## Acceptance Criteria
- [ ] Hardcoded credentials removed from `secret_leak.py`
- [ ] `.gitignore` created with `.env` and secrets patterns
- [ ] Code updated to use environment variables (`os.getenv()`)
- [ ] `.env.example` template created (without actual secrets)
- [ ] Pre-commit hook configured for secret detection
- [ ] Git history cleaned (BFG Repo-Cleaner)
- [ ] All team members notified

## Related Issues
- CWE-798: Use of Hard-Coded Credentials
- OWASP A07:2021 – Identification and Authentication Failures
- OWASP A02:2021 – Cryptographic Failures

## Resources
- [OWASP: Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [git-secrets](https://github.com/awslabs/git-secrets)
- [Detect-secrets by Yelp](https://github.com/Yelp/detect-secrets)
- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

## Assigned To
[Assign to security team/lead developer]

## Labels
`security` `critical` `aws` `credentials` `hardcoded` `must-fix`
