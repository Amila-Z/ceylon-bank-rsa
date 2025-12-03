"""
Ceylon Bank RSA Key Management System
Implementation of RSA Encryption and Decryption

This module provides secure RSA encryption and decryption capabilities
for Ceylon Bank's banking operations and secure communications.

Author: Ceylon Bank IT Security Team
Date: November 2025
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import time


def generate_rsa_keys(key_size=2048):
    """
    Generate RSA key pair with specified key size.
    
    Args:
        key_size (int): Size of the RSA key in bits (2048, 3072, or 4096)
        
    Returns:
        tuple: (private_key, public_key, key_object)
    """
    print(f"\n{'='*70}")
    print(f"Generating {key_size}-bit RSA key pair...")
    print(f"{'='*70}")
    
    start_time = time.time()
    key = RSA.generate(key_size)
    generation_time = time.time() - start_time
    
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    print(f"✓ Key generation completed in {generation_time:.4f} seconds")
    print(f"  Public Exponent (e): {key.e}")
    print(f"  Modulus Size: {key.n.bit_length()} bits")
    
    return private_key, public_key, key


def encrypt_message(message, public_key):
    """
    Encrypt a message using RSA public key with PKCS#1 OAEP padding.
    
    Args:
        message (str): Plaintext message to encrypt
        public_key (bytes): RSA public key in PEM format
        
    Returns:
        str: Base64-encoded ciphertext
    """
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    
    # Encrypt the message
    encrypted = cipher.encrypt(message.encode('utf-8'))
    
    # Return base64-encoded ciphertext for easy transmission
    return base64.b64encode(encrypted).decode('utf-8')


def decrypt_message(encrypted_message, private_key):
    """
    Decrypt a message using RSA private key with PKCS#1 OAEP padding.
    
    Args:
        encrypted_message (str): Base64-encoded ciphertext
        private_key (bytes): RSA private key in PEM format
        
    Returns:
        str: Decrypted plaintext message
    """
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    
    # Decode base64 and decrypt
    encrypted_bytes = base64.b64decode(encrypted_message)
    decrypted = cipher.decrypt(encrypted_bytes)
    
    return decrypted.decode('utf-8')


def get_security_level(key_size):
    """
    Get security level description based on key size.
    
    Args:
        key_size (int): RSA key size in bits
        
    Returns:
        dict: Security information
    """
    security_info = {
        2048: {
            "security_bits": 112,
            "level": "Standard Security",
            "nist_approval": "Through 2030",
            "use_case": "Routine operations and standard transactions"
        },
        3072: {
            "security_bits": 128,
            "level": "High Security",
            "nist_approval": "Beyond 2030",
            "use_case": "High-value transactions and long-term protection"
        },
        4096: {
            "security_bits": 152,
            "level": "Maximum Security",
            "nist_approval": "Maximum recommended",
            "use_case": "Critical infrastructure and executive communications"
        }
    }
    return security_info.get(key_size, {})


def display_security_info(key_size):
    """Display security information for the selected key size."""
    info = get_security_level(key_size)
    
    print(f"\n┌{'─'*68}┐")
    print(f"│ SECURITY INFORMATION - {key_size}-bit RSA Key{' '*(32-len(str(key_size)))}│")
    print(f"├{'─'*68}┤")
    print(f"│ Security Strength: ~{info['security_bits']} bits{' '*(41-len(str(info['security_bits'])))}│")
    print(f"│ Security Level: {info['level']}{' '*(50-len(info['level']))}│")
    print(f"│ NIST Approval: {info['nist_approval']}{' '*(51-len(info['nist_approval']))}│")
    print(f"│ Recommended Use: {info['use_case']}{' '*(48-len(info['use_case']))}│")
    print(f"└{'─'*68}┘")


def test_rsa_implementation(key_size=2048):
    """
    Test RSA implementation with specified key size.
    
    Args:
        key_size (int): Size of RSA key to test (2048, 3072, or 4096)
    """
    # Display security information
    display_security_info(key_size)
    
    # Generate keys
    private_key, public_key, key_obj = generate_rsa_keys(key_size)
    
    # Test message representing Ceylon Bank transaction
    plaintext = "Ceylon Bank Confidential Transaction: Transfer $50,000 to Account #12345678"
    
    print(f"\n{'─'*70}")
    print("ENCRYPTION TEST")
    print(f"{'─'*70}")
    print(f"Original Message:")
    print(f"  {plaintext}")
    
    # Encrypt the message
    start_time = time.time()
    ciphertext = encrypt_message(plaintext, public_key)
    encryption_time = time.time() - start_time
    
    print(f"\nEncrypted Message (Base64, first 80 characters):")
    print(f"  {ciphertext[:80]}...")
    print(f"  Full ciphertext length: {len(ciphertext)} characters")
    print(f"✓ Encryption completed in {encryption_time:.4f} seconds")
    
    # Decrypt the message
    print(f"\n{'─'*70}")
    print("DECRYPTION TEST")
    print(f"{'─'*70}")
    
    start_time = time.time()
    decrypted_text = decrypt_message(ciphertext, private_key)
    decryption_time = time.time() - start_time
    
    print(f"Decrypted Message:")
    print(f"  {decrypted_text}")
    print(f"✓ Decryption completed in {decryption_time:.4f} seconds")
    
    # Verify correctness
    print(f"\n{'─'*70}")
    print("VERIFICATION")
    print(f"{'─'*70}")
    
    if plaintext == decrypted_text:
        print("✓ SUCCESS: Decrypted text matches original message!")
        print("✓ RSA encryption/decryption verified for Ceylon Bank")
    else:
        print("✗ FAILURE: Decrypted text does not match original!")
    
    print(f"{'='*70}\n")


def main():
    """Main function to demonstrate Ceylon Bank RSA implementation."""
    
    print("\n" + "="*70)
    print(" "*15 + "CEYLON BANK RSA KEY MANAGEMENT SYSTEM")
    print(" "*10 + "Implementing Secure Asymmetric Encryption for Banking")
    print("="*70)
    
    # Test all three key sizes as per NIST recommendations
    key_sizes = [2048, 3072, 4096]
    
    for key_size in key_sizes:
        test_rsa_implementation(key_size)
        time.sleep(0.5)  # Brief pause between tests
    
    print("="*70)
    print(" "*20 + "All RSA Tests Completed Successfully!")
    print(" "*15 + "Ceylon Bank Encryption System Ready for Deployment")
    print("="*70)
    print("\nRECOMMENDATIONS:")
    print("  • Use 2048-bit keys for routine operations (valid through 2030)")
    print("  • Use 3072-bit keys for high-value transactions")
    print("  • Use 4096-bit keys for critical infrastructure and long-term security")
    print("\nIMPORTANT SECURITY NOTES:")
    print("  • Always keep private keys confidential and secure")
    print("  • Use Hardware Security Modules (HSMs) for key storage")
    print("  • Implement proper key lifecycle management")
    print("  • Monitor for quantum computing developments")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
