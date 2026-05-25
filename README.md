# Avaliação de Desempenho e Otimização de Código com Locust

Este repositório contém a implementação prática para a medição, relato e otimização do desempenho básico de uma API REST monolítica desenvolvida com Python e FastAPI, utilizando o Locust como ferramenta para testes de carga e estresse.

## 📋 Pré-requisitos e Dependências

Para reproduzir os testes locais, certifique-se de ter o Python instalado em sua máquina e, em seguida, instale os pacotes necessários executando o comando abaixo no terminal:

```bash
pip install fastapi uvicorn locust pydantic
```

## 🚀 Como Executar o Projeto

O experimento é dividido em duas fases (Baseline e Otimizado) para analisar o impacto real da alteração do código.  

### 1. Inicializar a API Monolítica (FastAPI)
No terminal, execute o seguinte comando para subir o servidor local na porta 8000:

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

> **Nota:** Certifique-se de alterar a variável de controle `OTIMIZADO` no topo do arquivo `main.py` para alternar entre os cenários do teste.  
> * **Fase 1 (Baseline - Código Original):** `OTIMIZADO = False`
> * **Fase 2 (Otimizado - Código Refatorado):** `OTIMIZADO = True`

### 2. Inicializar o Locust (Testes de Carga)
Em um segundo terminal, execute o Locust apontando para o arquivo de testes do plano:

```bash
python -m locust -f locustfile.py --host http://127.0.0.1:8000
```

## ⚙️ Configuração do Mix de Carga (Workload Mix)

O script de testes distribui os acessos entre 4 endpoints diferentes para simular o comportamento de produção:  

* **GET `/api/recurso-lento`** (40% dos acessos) - Rota com o gargalo de código focado no estresse. 
* **GET `/api/recurso-detalhe/{id}`** (30% dos acessos) - Consulta simples indexada por ID. 
* **GET `/api/status`** (20% dos acessos) - Rota leve de verificação de integridade/healthcheck. 
* **POST `/api/recurso`** (10% dos acessos) - Cadastro simples de novos dados.

---

## 📈 Parâmetros do Experimento

As duas fases do teste devem seguir rigorosamente os critérios abaixo na interface web do Locust (`http://localhost:8089`):  

* **Número de Usuários (Pico):** 50 usuários simultâneos. 
* **Aumento gradual (Spawn Rate):** 1 usuário por segundo.
* **Duração de cada teste:** 5 minutos por rodada.
* **Aquecimento (Warm-up):** O 1º minuto deve ser descartado utilizando o botão **"Reset Stats"** na interface do Locust. 
* **Repetições:** Realizar 5 repetições de cada cenário para calcular a média dos resultados obtidos.
