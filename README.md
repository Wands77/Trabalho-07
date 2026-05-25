# Avaliação de Desempenho e Otimização de Código com Locust

Este repositório contém a implementação prática para a medição, relato e otimização do desempenho básico de uma API REST monolítica desenvolvida com Python e FastAPI, utilizando o Locust como ferramenta para testes de carga e estresse.

## 🚀 Passos de Reprodução

Siga as instruções abaixo para configurar o ambiente e executar os testes localmente em sua máquina.

### 1. Clonar o Repositório
Abra o seu terminal e clone este repositório executando:

```bash
git clone https://github.com/Wands77/Trabalho-07.git
cd Trabalho-07
```
### 2. Preparar o Ambiente e Dependências
É altamente recomendado o uso de um ambiente virtual (venv) para evitar conflitos de pacotes. Crie e ative o ambiente virtual:

**No Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**No Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Com o ambiente ativo, instale as dependências necessárias para a API e para o Locust:

```bash
pip install fastapi uvicorn locust pydantic
```
### 3. Inicializar a API Monolítica (FastAPI)
No terminal, suba o servidor local executando:

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```
> **Nota:** Certifique-se de alterar a variável de controle `OTIMIZADO` no topo do arquivo `main.py` para alternar entre os cenários do teste.
> * **Fase 1 (Baseline - Código Original):** `OTIMIZADO = False`
> * **Fase 2 (Otimizado - Código Refatorado):** `OTIMIZADO = True`

### 4. Inicializar o Locust (Testes de Carga)
Em um segundo terminal (lembre-se de ativar o `.venv` nele também), execute o Locust apontando para o arquivo de testes:

```bash
python -m locust -f locustfile.py --host http://127.0.0.1:8000
```
Após executar este comando, acesse a interface web do Locust pelo seu navegador em: `http://localhost:8089`.

---

## ⚙️ Configuração do Mix de Carga (Workload Mix)
O script de testes distribui os acessos entre 4 endpoints diferentes para simular o comportamento de produção:

* **GET `/api/recurso-lento`** (40% dos acessos) - Rota com o gargalo de código focado no estresse.
* **GET `/api/recurso-detalhe/{id}`** (30% dos acessos) - Consulta simples indexada por ID.
* **GET `/api/status`** (20% dos acessos) - Rota leve de verificação de integridade/healthcheck.
* **POST `/api/recurso`** (10% dos acessos) - Cadastro simples de novos dados.

---

## 📈 Parâmetros do Experimento
As duas fases do teste devem seguir rigorosamente os critérios abaixo na interface web do Locust:

* **Número de Usuários (Pico):** 50 usuários simultâneos.
* **Aumento gradual (Spawn Rate):** 1 usuário por segundo.
* **Duração de cada teste:** 5 minutos por rodada.
* **Aquecimento (Warm-up):** O 1º minuto deve ser descartado utilizando o botão **"Reset Stats"** na interface do Locust.
* **Repetições:** Realizar 5 repetições de cada cenário para garantir a validade estatística e calcular a média dos resultados obtidos.

---

## 📊 Resultados e Evidências
Todos os resultados obtidos durante os testes locais foram consolidados na pasta `/results` deste repositório. Nela você encontrará:

* Os arquivos `.csv` e `.html` extraídos nativamente do Locust contendo os logs brutos das 10 repetições.
* Gráficos comparativos de latência e vazão (Throughput).
* A planilha `resumo.csv` / `resumo_testes_carga.xlsx` demonstrando matematicamente o impacto da redução do algoritmo de `O(N)` para `O(1)`, validando a mitigação do estrangulamento da CPU.
