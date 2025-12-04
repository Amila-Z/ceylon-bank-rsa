# ceylon-bank-rsa
RSA Encryption Implementation for Ceylon Bank - Academic Project with Python and Web Interface
### 1. Ceylon_Bank_RSA_Interface.html
Professional web-based user interface featuring:
- **Key Size Selection:** Choose between 2048, 3072, or 4096-bit keys
- **Security Level Indicators:** Visual badges showing security strength
- **Key Generation:** Automatic generation with selected key size
- **Encryption Module:** Encrypt messages using public keys
- **Decryption Module:** Decrypt messages using private keys
- **Copy Functionality:** Easy copying of keys and encrypted messages
- **Professional Design:** Blue color scheme matching Ceylon Bank branding
- **Responsive Layout:** Works on desktop, tablet, and mobile devices

### 2. ceylon_bank_rsa.py
Python implementation with:
- RSA key generation (2048, 3072, 4096 bits)
- Message encryption using PKCS#1 OAEP padding
- Message decryption with security verification
- Comprehensive testing across all key sizes
- Performance metrics and security information
- NIST compliance indicators

## Installation & Setup

### Requirements
```bash
# Python 3.x (Python 3.8+ recommended)
# Install required library
pip install pycryptodome
```

### Running the Python Implementation
```bash
python3 ceylon_bank_rsa.py
```

This will:
1. Generate RSA key pairs for all three key sizes
2. Encrypt test messages representing Ceylon Bank transactions
3. Decrypt and verify the messages
4. Display security information and performance metrics

### Using the Web Interface

**Option 1: Direct Browser Access**
1. Double-click `Ceylon_Bank_RSA_Interface.html`
2. It will open in your default web browser
3. No server required - runs completely in the browser

**Option 2: Local Web Server (Recommended for testing)**
```bash
# Python 3
python3 -m http.server 8000

# Then open browser to:
# http://localhost:8000/Ceylon_Bank_RSA_Interface.html
```

## How to Use the Web Interface

### Step 1: Select Key Size
Choose the appropriate key size based on your security needs:
- **2048-bit:** Standard security for routine operations (NIST approved through 2030)
- **3072-bit:** High security for sensitive transactions (recommended for long-term protection)
- **4096-bit:** Maximum security for critical infrastructure

### Step 2: Generate Keys
Click "Generate New Key Pair" to create RSA keys with your selected size. The system automatically:
- Generates cryptographically secure keys
- Displays both public and private keys
- Pre-fills keys into encryption/decryption fields

### Step 3: Encrypt Messages
1. Enter your confidential message in the "Message to Encrypt" field
2. Ensure the public key is in the "Public Key for Encryption" field
3. Click "Encrypt Message"
4. Copy the encrypted message using the copy button

### Step 4: Decrypt Messages
1. Paste the encrypted message into the "Encrypted Message" field
2. Ensure the private key is in the "Private Key for Decryption" field
3. Click "Decrypt Message"
4. View the original decrypted message

### Step 5: Share Securely
- **Public Key:** Can be freely shared with anyone who needs to send you encrypted messages
- **Private Key:** Must be kept confidential and secure at all times
- **Encrypted Messages:** Can be transmitted over insecure channels

## Security Best Practices for Ceylon Bank Employees

### Key Management
1. **Never share private keys** - Only the holder of the private key can decrypt messages
2. **Use secure storage** - Store private keys in password-protected files or HSMs
3. **Unique keys per purpose** - Generate different key pairs for different purposes
4. **Regular key rotation** - Replace keys periodically (annually recommended)

### Key Size Selection Guidelines
- **Routine Communications:** 2048-bit keys (balance of security and performance)
- **Financial Transactions > $10,000:** 3072-bit keys (enhanced security)
- **Executive Communications:** 4096-bit keys (maximum security)
- **Long-term Data Storage:** 3072-bit or 4096-bit keys (future-proof)

### Operational Security
1. Always verify the authenticity of public keys before encrypting sensitive data
2. Use secure channels (in-person, phone verification) to exchange public keys
3. Keep encryption software and libraries updated
4. Report any suspected key compromise immediately to IT Security

## Technical Details

### RSA Key Sizes and Security
| Key Size | Security Bits | NIST Approval | Use Case |
|----------|--------------|---------------|----------|
| 2048-bit | ~112 bits | Through 2030 | Routine operations |
| 3072-bit | ~128 bits | Beyond 2030 | High-value transactions |
| 4096-bit | ~152 bits | Maximum | Critical infrastructure |

### Padding Scheme
The implementation uses **PKCS#1 OAEP** (Optimal Asymmetric Encryption Padding):
- Provides semantic security
- Protects against chosen-ciphertext attacks
- Industry-standard padding for RSA encryption
- Recommended by NIST and RSA Security

### Performance Characteristics
Based on testing:
- **2048-bit:** Generation ~0.2s, Encryption ~0.003s, Decryption ~0.035s
- **3072-bit:** Generation ~1.4s, Encryption ~0.002s, Decryption ~0.058s
- **4096-bit:** Generation ~6.9s, Encryption ~0.002s, Decryption ~0.089s

## Threat Mitigation

### Quantum Computing Threats
- **Current Status:** No immediate threat (cryptographically relevant quantum computers not yet available)
- **Ceylon Bank Action:** Monitor NIST post-quantum cryptography standards
- **Timeline:** Plan migration to post-quantum algorithms by 2030-2035

### Implementation Vulnerabilities
- **Mitigation:** Using well-tested pycryptodome library
- **Padding:** PKCS#1 OAEP prevents common attacks
- **RNG:** Cryptographically secure random number generation

### Key Management
- **Recommendation:** Use Hardware Security Modules (HSMs) for key storage
- **Policy:** Implement strict key lifecycle management
- **Audit:** Regular security audits of cryptographic systems

## Compliance & Standards

### NIST SP 800-57 Compliance
- All key sizes comply with NIST Special Publication 800-57 Part 1 Revision 5
- Recommendations for key management followed
- Security strength levels documented and validated

### Banking Security Standards
- Suitable for PCI DSS compliance
- Meets ISO 27001 requirements for cryptographic controls
- Compatible with Basel III operational risk management framework

## Troubleshooting

### Python Script Issues
**Error: "ModuleNotFoundError: No module named 'Crypto'"**
```bash
pip install pycryptodome --break-system-packages
```

**Error: "Permission denied"**
```bash
# Linux/Mac
chmod +x ceylon_bank_rsa.py
python3 ceylon_bank_rsa.py
```

### Web Interface Issues
**Keys not generating:**
- Ensure JavaScript is enabled in your browser
- Try refreshing the page
- Check browser console for errors (F12)

**Encryption/Decryption fails:**
- Verify the correct key is being used (public for encryption, private for decryption)
- Ensure the key format is correct (PEM format with header/footer)
- Check that the encrypted message is complete (no truncation)

<img width="1106" height="880" alt="Cylon_Bank_RSA" src="https://github.com/user-attachments/assets/984385ca-a513-4be8-814e-b29fe87ad59d" />
