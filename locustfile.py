from locust import HttpUser, task, between
import random

class APITester(HttpUser):
    # Intervalo de simulação entre requisições consecutivas de um mesmo usuário
    wait_time = between(1, 2)

    @task(4)
    def recurso_lento(self):
        """Simula 40% do tráfego na rota com gargalo"""
        self.client.get("/api/recurso-lento", name="GET /api/recurso-lento")

    @task(3)
    def recurso_detalhe(self):
        """Simula 30% do tráfego em consulta indexada"""
        recurso_id = random.randint(1, 10000)
        self.client.get(f"/api/recurso-detalhe/{recurso_id}", name="GET /api/recurso-detalhe/{id}")

    @task(2)
    def status(self):
        """Simula 20% do tráfego no healthcheck"""
        self.client.get("/api/status", name="GET /api/status")

    @task(1)
    def criar_recurso(self):
        """Simula 10% do tráfego de gravação de dados"""
        novo_id = random.randint(10001, 999999)
        payload = {
            "id": novo_id,
            "data": f"Novo dado {novo_id}",
            "value": random.randint(1, 100)
        }
        self.client.post("/api/recurso", json=payload, name="POST /api/recurso")