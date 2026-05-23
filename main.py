from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulação de banco de dados populado em memória
db_list = [{"id": i, "data": f"Dado {i}", "value": i * 2} for i in range(1, 10001)]
db_dict = {i: {"id": i, "data": f"Dado {i}", "value": i * 2} for i in range(1, 10001)}

class Recurso(BaseModel):
    id: int
    data: str
    value: int

# Variável de controle para alternar as fases do experimento
OTIMIZADO = True

@app.get("/api/recurso-lento")
def get_recurso_lento():
    """40% dos acessos - Endpoint com gargalo proposital"""
    target_id = 9999
    
    if not OTIMIZADO:
        # Fase 1: Busca linear ineficiente com processamento de CPU extra
        resultado = None
        for item in db_list:
            # Simulação de processamento pesado síncrono
            _ = [x**2 for x in range(100)] 
            if item["id"] == target_id:
                resultado = item
        if not resultado:
            raise HTTPException(status_code=404, detail="Não encontrado")
        return resultado
    else:
        # Fase 2: Otimização utilizando busca direta por chave (O(1))
        if target_id not in db_dict:
            raise HTTPException(status_code=404, detail="Não encontrado")
        return db_dict[target_id]

@app.get("/api/recurso-detalhe/{recurso_id}")
def get_recurso_detalhe(recurso_id: int):
    """30% dos acessos - Consulta simples e indexada"""
    if recurso_id not in db_dict:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return db_dict[recurso_id]

@app.get("/api/status")
def get_status():
    """20% dos acessos - Rota leve de verificação de integridade"""
    return {"status": "ok", "uptime": "100%"}

@app.post("/api/recurso")
def create_recurso(recurso: Recurso):
    """10% dos acessos - Cadastro simples de novos dados"""
    if recurso.id in db_dict:
        raise HTTPException(status_code=400, detail="ID já existe")
    
    # Inserção em ambas as estruturas para consistência
    db_list.append(recurso.model_dump())
    db_dict[recurso.id] = recurso.model_dump()
    return {"message": "Criado com sucesso"}