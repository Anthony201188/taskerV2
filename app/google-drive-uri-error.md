# Using HTTPS for Local Development

To use HTTPS locally for development purposes, follow the steps below to create a self-signed SSL certificate and modify your application to use HTTPS.

### 1. Generate SSL Certificates

Run the following commands to create your self-signed SSL certificate and key:

```bash
openssl genpkey -algorithm RSA -out key.pem
openssl req -new -key key.pem -out csr.pem
openssl x509 -req -in csr.pem -signkey key.pem -out cert.pem
