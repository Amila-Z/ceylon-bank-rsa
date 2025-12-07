# Ceylon Bank RSA Key Management System

## 📌 Project Overview
Enterprise-grade implementation of RSA encryption and decryption for secure banking communications, integrated with Public Key Infrastructure (PKI) for scalable key management. Developed as part of an academic assignment on asymmetric cryptography and enterprise security architecture.

## 🔧 Technologies Used
- **Python 3.x** with pycryptodome library
- **JavaScript** with JSEncrypt library
- **HTML/CSS** for web interface
- **PKI Integration** with SSL/TLS and IPsec protocols

## Files Included

### 1. ceylon_bank_rsa.py
Python implementation featuring:
- RSA key generation (2048, 3072, 4096-bit keys)
- PKCS#1 OAEP encryption
- PKCS#1 OAEP decryption
- Performance testing across all key sizes
- NIST-compliant security levels

### 2. Ceylon_Bank_RSA_Interface.html
Web-based interface featuring:
- Interactive key generation with security level indicators
- Real-time encryption/decryption
- Support for pasting previously generated keys
- Professional Ceylon Bank branding
- Copy functionality for keys and encrypted messages
- No server required - runs completely client-side

## How to Use

### Python Implementation
```bash
# Install required library
pip install pycryptodome

# Run the program
python ceylon_bank_rsa.py
```

**Output:** Tests encryption/decryption with all three key sizes (2048, 3072, 4096 bits) and displays performance metrics.

### Web Interface
Simply open `Ceylon_Bank_RSA_Interface.html` in any modern web browser.

**Features:**
- Generate RSA key pairs with one click
- Encrypt messages using any public key
- Decrypt messages using corresponding private keys
- Paste previously generated keys for reuse
- Copy keys and encrypted messages with one click

## Enterprise Deployment Architecture

This implementation is designed to integrate with enterprise security infrastructure:

### Public Key Infrastructure (PKI)
- **Certificate Authority (CA):** Centralized trust management for public keys
- **Two-tier structure:** Offline Root CA (4096-bit) and operational Intermediate CA (3072-bit)
- **Certificate lifecycle:** Automated issuance, validation, and revocation

### Secure Communication Protocols
- **SSL/TLS VPN:** Web-based employee access with RSA handshake and AES-256 data encryption
- **IPsec VPN:** Site-to-site tunnels between branches with IKEv2 and RSA authentication

### Multi-Factor Authentication
- **Something you have:** RSA private key in certificate
- **Something you know:** Password authentication
- **Something you are:** Biometric verification for high-value transactions

## Security Features
- NIST-compliant key sizes (SP 800-57)
- PKCS#1 OAEP padding for semantic security
- Cryptographically secure random number generation
- Defense-in-depth security architecture
- Automated certificate validation and revocation checking

## Key Size Recommendations

| Key Size | Security Bits | NIST Approval | Use Case |
|----------|--------------|---------------|----------|
| 2048-bit | ~112 bits | Through 2030 | Routine operations |
| 3072-bit | ~128 bits | Beyond 2030 | High-value transactions |
| 4096-bit | ~152 bits | Maximum | Critical infrastructure |

## Performance Metrics

Based on testing (average):
- **2048-bit:** Key generation ~0.2s, Encryption ~0.003s, Decryption ~0.035s
- **3072-bit:** Key generation ~1.4s, Encryption ~0.002s, Decryption ~0.058s
- **4096-bit:** Key generation ~6.9s, Encryption ~0.002s, Decryption ~0.089s

## Academic Context
This project demonstrates understanding of:
- Asymmetric cryptography principles (RSA algorithm)
- Enterprise Public Key Infrastructure (PKI)
- Secure communication protocols (SSL/TLS, IPsec)
- Multi-factor authentication mechanisms
- NIST cryptographic standards and best practices
- Real-world banking security requirements

## System Architecture

```
                Certificate Authority (CA)
                         |
                [Signs & validates keys]
                         |
        ┌────────────────┴────────────────┐
        ↓                                 ↓
   Employee A                        Employee B
   [Certificate]                    [Certificate]
        ↓                                 ↓
   SSL/TLS VPN Tunnel ══════════════════→
        ↓                                 ↓
   RSA Encryption  ═════════════════════→
```

## Security Best Practices

### For Development:
1. Always use cryptographically secure random number generators
2. Implement proper padding (PKCS#1 OAEP) to prevent attacks
3. Use NIST-recommended key sizes (minimum 2048-bit)
4. Validate all inputs and handle errors securely
5. Keep cryptographic libraries updated

### For Deployment:
1. Store private keys in Hardware Security Modules (HSMs)
2. Implement certificate-based authentication
3. Use Certificate Revocation Lists (CRL) or OCSP
4. Enable audit logging for all cryptographic operations
5. Regular security assessments and penetration testing

## References

1. NIST Special Publication 800-57 Part 1 Revision 5: Recommendation for Key Management
2. Rivest, R., Shamir, A., & Adleman, L. (1978). A Method for Obtaining Digital Signatures and Public-Key Cryptosystems
3. Bellare, M. and Rogaway, P. (1994). Optimal Asymmetric Encryption Padding
4. Cooper, D. et al. (2008). Internet X.509 Public Key Infrastructure Certificate and CRL Profile (RFC 5280)
5. Frankel, S. and Krishnan, S. (2011). IP Security (IPsec) and IKE Document Roadmap (RFC 6071)

## Key Features

- **Complete RSA Implementation** - Key generation, encryption, decryption
- **Professional Web Interface** - User-friendly GUI for all operations
- **Multiple Key Sizes** - 2048, 3072, 4096-bit support
- **NIST Compliant** - Follows SP 800-57 recommendations
- **PKI Ready** - Designed for enterprise PKI integration
- **Secure by Default** - PKCS#1 OAEP padding, secure RNG
- **Well Documented** - Comprehensive code comments and README

## License
This is an academic project developed for educational purposes.

## Author
Amila Niroshana Thilakarathne (Amila_Z)
Academic Project - Cryptography and Network Security Course  
November 2025

## Contact
For questions or feedback about this implementation, please open an issue on this repository.

---

**Note:** This implementation is designed for educational purposes to demonstrate RSA encryption concepts and enterprise security architecture. For production banking systems, additional security measures, compliance certifications, and professional security audits would be required.

<img width="1106" height="880" alt="Cylon_Bank_RSA" src="https://github.com/user-attachments/assets/984385ca-a513-4be8-814e-b29fe87ad59d" />
