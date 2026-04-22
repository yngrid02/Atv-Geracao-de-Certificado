# Geração de Certificados Digitais (Simulação ICP-Brasil) 🔒🇧🇷
Este repositório contém a implementação de um script em Python para a simulação do processo de geração de certificados digitais, seguindo os conceitos fundamentais da Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil).

# Tecnologias Utilizadas
**Linguagem:** Python 3.x

**Biblioteca Criptográfica:** cryptography

**Padrão de Certificado:** X.509

**Algoritmo de Chave:** RSA (2048 bits)

**Algoritmo de Assinatura:** SHA-256

# Funcionalidades do Script
O código desenvolvido realiza as seguintes etapas automaticamente:

- **Geração de Chaves:** Cria um par de chaves RSA de 2048 bits.
  
- **Coleta de Dados:** Interface via terminal para inserção de dados (País, Estado, Cidade, Organização, Curso e Nome).
  
- **Cálculo de Validade:** Define automaticamente a data de início (timestamp atual) e o término (exatos 365 dias após a emissão).
  
- **Emissão do Certificado:** Gera um certificado X.509 auto-assinado.
  
- **Persistência:** Exporta a Chave Privada e o Certificado em arquivos separados no formato .pem.
  
# Como Executar
**1. Pré-requisitos**

Certifique-se de ter o Python instalado. Instale as bibliotecas necessárias:

- pip install requirements.txt

**2. Execução** 

Clone o repositório ou baixe o arquivo gerador_certificado.py e execute:

- python certificado.py

**3. Saída Gerada** 

Após a execução, os seguintes arquivos serão criados na raiz do projeto:

- **private_key.pem:** Contém a sua chave privada (Mantenha em segurança!).
  
- **certificate.pem:** O seu certificado digital contendo sua chave pública e dados de identificação.

# Descrição do Passo a Passo (Relatório Técnico)
**I. Geração do Par de Chaves**

Utilizou-se o algoritmo RSA com um expoente público padrão (65537) e tamanho de 2048 bits. Esta configuração garante que a chave seja robusta contra ataques de força bruta atuais, respeitando os requisitos de segurança da ICP-Brasil.

**II. Estruturação do Certificado (Subject)**

O certificado foi preenchido com campos de identificação baseados no padrão X.509:

- **C** (Country Name): Sigla do país.
 
- **ST** (State or Province): Unidade federativa.
 
- **L** (Locality): Cidade.
 
- **O** (Organization): Nome da entidade.
 
- **OU** (Organizational Unit): Curso/Departamento.
 
- **CN** (Common Name): Nome do titular.

**III. Gestão de Temporalidade**

O script utiliza a biblioteca datetime com timezone.utc para garantir que a validade seja calculada com precisão astronômica, definindo o campo not_valid_after como Data Atual + valid_days (365).

**IV. Assinatura e Integridade**

O certificado é assinado digitalmente utilizando a própria chave privada do usuário com o algoritmo de hash SHA-256. Isso garante que qualquer alteração posterior nos dados do certificado invalidará a assinatura.

## ⚠️ Avisos de Segurança
**Chave Privada:** Nunca compartilhe o arquivo private_key.pem. Se alguém tiver acesso a ele, poderá assinar documentos em seu nome.

**Ambiente:** Em produção, chaves privadas devem ser geradas dentro de módulos de segurança criptográficos (Tokens ou HSMs).

## 👥 Desenvolvedores

  * Taylanne Castelo Branco Cavalcante
  * William Dias Marinho
  * Yara Fernandes Ribeiro
  * Yngrid Guimarães Silva
