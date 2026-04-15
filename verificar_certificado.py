from cryptography import x509


with open("certificate.pem", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read())

print("\n================ CERTIFICADO DIGITAL ================\n")


print("🔹 DADOS DO TITULAR:")
dados = {}
for attr in cert.subject:
    dados[attr.oid._name] = attr.value

print(f"País: {dados.get('countryName')}")
print(f"Estado: {dados.get('stateOrProvinceName')}")
print(f"Cidade: {dados.get('localityName')}")
print(f"Organização: {dados.get('organizationName')}")
print(f"Nome comum: {dados.get('commonName')}")


print("\n🔹 VALIDADE:")
print("Início:", cert.not_valid_before_utc)
print("Fim   :", cert.not_valid_after_utc)


print("\n🔹 INFORMAÇÕES TÉCNICAS:")
print("Serial Number:", cert.serial_number)
print("Algoritmo:", cert.signature_hash_algorithm.name)

print("\n====================================================\n")