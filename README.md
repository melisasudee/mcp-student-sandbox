# Mystery Module - Quadratic Equation Solver

## 📋 Amaç (Purpose)

Bu modül, ikinci dereceden denklemlerin köklerini hesaplamak için kullanılır. Matematiksel olarak `ax² + bx + c = 0` formundaki denklemlerin reel köklerini bulur.

**Matematiksel Formül:**
```
x = [-b ± √(b² - 4ac)] / (2a)
```

Burada `b² - 4ac` ifadesi **discriminant (diskriminant)** olarak adlandırılır ve köklerin varlığını belirler.

## 🔧 Fonksiyon: `fn_x(a, b, c)`

### Parametreler (Parameters)

| Parametre | Tip | Açıklama | Örnek |
|-----------|-----|----------|-------|
| `a` | `float` | x² katsayısı (sıfır olmamalı) | `2.0` |
| `b` | `float` | x katsayısı | `-3.0` |
| `c` | `float` | Sabit terim | `1.0` |

### Dönüş Değeri (Return Value)

- **Başarılı:** `(tuple)` - İki kök içeren tuple `(x1, x2)`
  - `x1`: Pozitif kök (-b + √discriminant)
  - `x2`: Negatif kök (-b - √discriminant)
- **Başarısız:** `None` - Eğer discriminant negatifse (reel kök yok)

### Özel Durumlar (Edge Cases)

- **Discriminant = 0:** Çift kök (x1 = x2)
- **Discriminant < 0:** Reel kök yok → `None`
- **a = 0:** Geçersiz (bölme hatası) → **Dikkat:** Fonksiyon kontrol etmiyor!

## 📖 Kullanım Örnekleri (Usage Examples)

### Temel Kullanım

```python
from mystery_module import fn_x

# Denklemi: 2x² - 3x + 1 = 0
roots = fn_x(2, -3, 1)
print(roots)  # (1.0, 0.5)
```

### Farklı Senaryolar

```python
# 1. Reel kökler var
result = fn_x(1, -5, 6)  # x² - 5x + 6 = 0
print(result)  # (3.0, 2.0)

# 2. Çift kök (discriminant = 0)
result = fn_x(1, -4, 4)  # x² - 4x + 4 = 0
print(result)  # (2.0, 2.0)

# 3. Reel kök yok (discriminant < 0)
result = fn_x(1, 1, 1)   # x² + x + 1 = 0
print(result)  # None
```

### Manuel Doğrulama

```python
# Denklemi: x² - 5x + 6 = 0
# Beklenen kökler: x = 3 veya x = 2

roots = fn_x(1, -5, 6)
print(f"Kökler: {roots}")

# Doğrulama:
x1, x2 = roots
print(f"x1 doğrulama: {x1}² - 5*{x1} + 6 = {x1**2 - 5*x1 + 6}")  # ≈ 0
print(f"x2 doğrulama: {x2}² - 5*{x2} + 6 = {x2**2 - 5*x2 + 6}")  # ≈ 0
```

## ⚠️ Uyarılar (Warnings)

1. **a = 0 kontrolü yok:** Eğer `a = 0` ise `ZeroDivisionError` oluşur
2. **Float hassasiyeti:** Büyük sayılarla yuvarlama hataları olabilir
3. **Karmaşık kökler:** Sadece reel kökleri döndürür (karmaşık kökler için None)

## 🔬 Teknik Detaylar (Technical Details)

### Algoritma Adımları:
1. **Discriminant hesapla:** `d = b² - 4ac`
2. **Kök kontrolü:** `d < 0` ise reel kök yok
3. **Kökleri hesapla:** `(-b ± √d) / (2a)`

### Matematiksel Kısıtlar:
- `a ≠ 0` (fonksiyon kontrol etmiyor!)
- `d ≥ 0` için reel kökler
- Float precision limitleri

### Performans:
- **Zaman karmaşıklığı:** O(1) - sabit zaman
- **Uzay karmaşıklığı:** O(1) - sabit alan
- **Bağımlılıklar:** `math` modülü (sqrt için)

## 🧪 Test Örnekleri (Test Cases)

```python
# Test suite
def test_quadratic_solver():
    # Test 1: Normal case
    assert fn_x(1, -5, 6) == (3.0, 2.0)
    
    # Test 2: Double root
    assert fn_x(1, -4, 4) == (2.0, 2.0)
    
    # Test 3: No real roots
    assert fn_x(1, 1, 1) is None
    
    # Test 4: Fractional coefficients
    result = fn_x(0.5, -1.5, 1)
    assert abs(result[0] - 2.0) < 1e-10
    assert abs(result[1] - 1.0) < 1e-10

if __name__ == "__main__":
    test_quadratic_solver()
    print("✅ All tests passed!")
```

## 📚 İlgili Konular (Related Topics)

- **Kökler:** Quadratic formula, discriminant
- **Matematik:** Algebra, equations
- **Programlama:** Numerical computing, error handling

## 🤝 Katkıda Bulunma (Contributing)

Kod iyileştirmeleri için:
- `a = 0` kontrolü ekleyin
- Karmaşık kökler desteği
- Daha iyi error handling
- Type hints ekleyin
- Unit tests yazın

---

**Not:** Bu modül eğitim amaçlı basit bir implementasyondur. Production kullanım için daha robust kütüphaneler (numpy, scipy) tercih edilmelidir.