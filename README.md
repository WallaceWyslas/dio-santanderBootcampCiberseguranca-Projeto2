# Simulação Simples de Ransomware com Python

Este projeto demonstra um exemplo **DIDÁTICO** e **SIMPLIFICADO** de como um ransomware pode funcionar, utilizando criptografia simétrica com AES no modo CTR.  **ATENÇÃO:** Este projeto é apenas para fins educacionais e **NÃO DEVE SER USADO EM PRODUÇÃO**, pois contém vulnerabilidades significativas.

## Funcionamento

O projeto consiste em dois scripts Python:

* **`encrypt.py`:** Simula o "ransomware". Ele criptografa o arquivo `test.txt` e salva a versão criptografada como `test.txt.encrypted`.  A chave de criptografia, gerada aleatoriamente, é exibida no console durante a execução.  **Em um ransomware real, a chave seria gerenciada de forma muito mais segura e maliciosa.**

* **`decrypt.py`:**  Simula o processo de descriptografia. Requer a chave gerada pelo `encrypt.py` para restaurar o arquivo original.  O arquivo descriptografado é salvo como `test.txt.decrypted`.


## Como usar

1. **Criptografar:**
   ```bash
   python encrypter.py

2. **Descriptografar:**
   ```bash
   python decrypter.py
