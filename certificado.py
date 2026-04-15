from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

print("=== GERADOR DE CERTIFICADO DIGITAL ===\n")

country = input("País (use sigla, ex: BR, US, PT): ").strip().upper()


state = input("Estado: ")
city = input("Cidade: ")
organization = input("Organização: ")
course = input("Curso de formação: ")
common_name = input("Nome Completo: ")


key_size = 2048
valid_days = 365


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=key_size,
)


subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, country),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
    x509.NameAttribute(NameOID.LOCALITY_NAME, city),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),

    
    x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, course),

    x509.NameAttribute(NameOID.COMMON_NAME, common_name),
])


valid_from = datetime.datetime.now(datetime.timezone.utc)
valid_to = valid_from + datetime.timedelta(days=valid_days)

certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(valid_from)
    .not_valid_after(valid_to)
    .add_extension(
        x509.BasicConstraints(ca=True, path_length=None),
        critical=True,
    )
    .sign(private_key, hashes.SHA256())
)


with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )


with open("certificate.pem", "wb") as f:
    f.write(
        certificate.public_bytes(serialization.Encoding.PEM)
    )

print("\n✅ Certificado gerado com sucesso!")
print("Arquivos:")
print("- private_key.pem")
print("- certificate.pem")