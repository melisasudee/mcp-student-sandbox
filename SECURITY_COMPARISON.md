# 🔒 Güvenlik Karşılaştırması: GÜVENLI vs GÜVENSIZ

## ❌ GÜVENLI OLMAYAN KOD (secret_leak.py)

```python
# ❌ KRİTİK HATA: Hardcoded credentials
AWS_SECRET_KEY = "AKIA_FAKE_KEY_123456789_STUDENT_TEST"

def connect():
    # ❌ Logs'ta secret leak oluyor
    print(f"Connecting with: {AWS_SECRET_KEY}")
```

### Sorunlar:
- ✗ Repository'de görülebilir
- ✗ Git history'de kalıcı
- ✗ Herkes tarafından erişilebilir
- ✗ Code review'de visible
- ✗ Backup'larda saklanır
- ✗ Hata loglarında sızıyor
- ✗ Deployment sırasında expose olur

---

## ✅ GÜVENLI KOD (secret_leak_secure.py)

```python
import os
import logging

logger = logging.getLogger(__name__)

def get_aws_secret_key() -> str:
    """Güvenli credential retrieval"""
    secret_key = os.getenv("AWS_SECRET_KEY")
    if not secret_key:
        raise ValueError("AWS_SECRET_KEY environment variable not set")
    return secret_key

def connect() -> dict:
    """Güvenli connection"""
    secret_key = get_aws_secret_key()
    
    # ✅ Log'ta key masked
    key_preview = f"{secret_key[:8]}...{secret_key[-4:]}"
    logger.info(f"Connecting with key: {key_preview}")
    
    return {"status": "connected", "region": os.getenv("AWS_REGION")}
```

### Avantajlar:
- ✅ Code'da secret yok
- ✅ Git history temiz
- ✅ Rotation kolayı (env var change)
- ✅ CI/CD friendly (secrets manager)
- ✅ Environment-specific configs
- ✅ Log'ta masked key
- ✅ Developer machine'de lokal (`~/.env`)

---

## 📋 TEMPLATEler

### .gitignore
```
.env
.env.local
.env.*.local
*.key
*.pem
.aws/credentials
secrets.json
**/*secret*
```

### .env.example (git'te commitle!)
```
AWS_SECRET_KEY=your_real_key_here
AWS_REGION=us-east-1
DATABASE_URL=postgresql://user:password@localhost/mydb
```

### .env (git'te ignore edilir)
```
AWS_SECRET_KEY=AKIA_YOUR_ACTUAL_KEY_HERE
AWS_REGION=us-west-2
DATABASE_URL=postgresql://actualuser:actualpass@db.company.com/prod
```

---

## 🛡️ Güvenli Credential Yönetimi - Best Practices

### Tier 1: LOCAL (Geliştirme)
```bash
# .env dosyası (git ignored)
AWS_SECRET_KEY=local_test_key_123
```
✅ Sadece local machine'de
✅ git ignored
✅ Kolay yönetim

### Tier 2: CI/CD (Test/Staging)
```yaml
# GitHub Actions / GitLab CI
env:
  AWS_SECRET_KEY: ${{ secrets.AWS_SECRET_KEY }}
```
✅ Secrets manager tarafından yönetilir
✅ Maskedloglar
✅ Audit trail

### Tier 3: Production (Kubernetes/Cloud)
```yaml
# Kubernetes Secret
apiVersion: v1
kind: Secret
metadata:
  name: aws-credentials
data:
  secret-key: base64_encoded_actual_key
```
✅ Encrypted at rest
✅ RBAC kontrolü
✅ Rotation policies
✅ Audit logging

---

## 🔧 Remediation Checklist

- [ ] `.gitignore` oluşturuldu
- [ ] `.env.example` oluşturuldu (örnek credentials ile)
- [ ] `secret_leak.py` → environment variables'a migrate edildi
- [ ] Logging'te credentials masked
- [ ] Error handling eklendi
- [ ] Hata mesajlarda sensitive info yok
- [ ] `.env` files git history'den temizlendi (BFG)
- [ ] Pre-commit hooks kuruldu (detect-secrets)
- [ ] Team dokumentasyonu güncellendi
- [ ] Credential rotation yapıldı

---

## 📚 Kaynaklar

### Python Best Practices
- `python-dotenv` - .env file loading
- `python-decouple` - Config management
- `hvac` - HashiCorp Vault client

### Secret Detection
- `git-secrets` - AWS specific
- `detect-secrets` (Yelp) - Generic
- `GitGuardian` - CI/CD Integration

### Cleanup Tools
- `BFG Repo-Cleaner` - Git history cleaning
- `git-filter-branch` - Manual history rewrite

### References
- [OWASP Secrets Mgmt](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [CWE-798: Hardcoded Credentials](https://cwe.mitre.org/data/definitions/798.html)
- [AWS Best Practices](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)

---

## ⚠️ Git History Temizleme (Adım Adım)

**Uyarı: Bu işlem yapılmadan önce tüm takımı bilgilendirin!**

```bash
# 1. BFG Repo-Cleaner'ı kur
brew install bfg

# 2. Repo clone et (--mirror ile)
git clone --mirror https://github.com/user/repo.git

# 3. Sensitive patterns'ı identify et
echo "AWS_SECRET_KEY" >> passwords.txt

# 4. BFG'yi çalıştır
bfg --replace-text passwords.txt repo.git

# 5. History temizle
cd repo.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive

# 6. Force push et (TEKNİK BORÇ!)
cd ../repo
git push --force
```

**Alternatif:** Sadece taze clone yaparak baştan başlamak daha güvenli olabilir!
