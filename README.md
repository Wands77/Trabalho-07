# Avaliação de Desempenho e Otimização de Código com Locust

[cite_start]Este repositório contém a implementação prática para a medição, relato e otimização do desempenho básico de uma API REST monolítica desenvolvida com Python e FastAPI, utilizando o Locust como ferramenta para testes de carga e estresse[cite: 1, 3].

## 📋 Pré-requisitos e Dependências

Para reproduzir os testes locais, certifique-se de ter o Python instalado em sua máquina e, em seguida, instale os pacotes necessários executando o comando abaixo no terminal:

```bash
pip install fastapi uvicorn locust pydantic
```

## 🚀 Como Executar o Projeto

[cite_start]O experimento é dividido em duas fases (Baseline e Otimizado) para analisar o impacto real da alteração do código.  

### 1. Inicializar a API Monolítica (FastAPI)
No terminal, execute o seguinte comando para subir o servidor local na porta 8000:

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
