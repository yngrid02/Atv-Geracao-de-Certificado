from cryptography import x509
from datetime import timedelta


with open("certificate.pem", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read())

print("\n================ CERTIFICADO DIGITAL ================\n")


print(" DADOS DO TITULAR:")
dados = {}
for attr in cert.subject:
    dados[attr.oid._name] = attr.value

print(f"País: {dados.get('countryName')}")
print(f"Estado: {dados.get('stateOrProvinceName')}")
print(f"Cidade: {dados.get('localityName')}")
print(f"Organização: {dados.get('organizationName')}")
print(f"Nome comum: {dados.get('commonName')}")


print("\n VALIDADE:")
data_inicio = (cert.not_valid_before_utc - timedelta(hours=3)).strftime("%d/%m/%Y %H:%M:%S")
data_fim = (cert.not_valid_after_utc - timedelta(hours=3)).strftime("%d/%m/%Y %H:%M:%S")

print("Início:", data_inicio)
print("Fim   :", data_fim)


print("\n INFORMAÇÕES TÉCNICAS:")
print("Serial Number:", cert.serial_number)
print("Algoritmo:", cert.signature_hash_algorithm.name)

print("\n====================================================\n")