import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from typing import List, Tuple

# ==========================================
# 1. BLOCO RESIDUAL (Building Block)
# ==========================================
class BlocoResiduo(nn.Module):
    """
    Bloco de conexão residual. Permite que a rede seja muito profunda
    passando o sinal original direto para frente (skip connection).
    """
    def __init__(self, dimensoes: int, dropout_rate: float = 0.2) -> None:
        super().__init__()
        # Primeira camada densa do bloco
        self.linear1 = nn.Linear(dimensoes, dimensoes)
        self.bn1 = nn.BatchNorm1d(dimensoes)
        self.relu = nn.ReLU()
        
        # Segunda camada densa do bloco
        self.linear2 = nn.Linear(dimensoes, dimensoes)
        self.bn2 = nn.BatchNorm1d(dimensoes)
        
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Guarda o valor original para a Conexão Residual
        residuo = x 
        
        out = self.linear1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.dropout(out)
        
        out = self.linear2(out)
        out = self.bn2(out)
        
        # Soma o sinal original (Resíduo) antes de aplicar a última ativação
        out += residuo 
        out = self.relu(out)
        return out


# ==========================================
# 2. A REDE NEURAL PROFUNDA (Main Network)
# ==========================================
class GrandeRedeNeural(nn.Module):
    """
    Rede Neural de Grande Porte escalável com múltiplas camadas ocultas
    e múltiplos blocos residuais internos.
    """
    def __init__(self, tam_entrada: int, tam_saida: int, 
                 num_blocos: int = 6, dim_oculta: int = 512) -> None:
        super().__init__()
        
        print(f"[Camada Inicial] Mapeando {tam_entrada} -> {dim_oculta} neurônios.")
        self.camada_entrada = nn.Sequential(
            nn.Linear(tam_entrada, dim_oculta),
            nn.BatchNorm1d(dim_oculta),
            nn.ReLU()
        )
        
        # Criando a espinha dorsal "Grande" da rede dinamicamente com uma lista de blocos
        print(f"[Espinha Dorsal] Criando {num_blocos} Blocos Residuais de {dim_oculta} neurônios cada.")
        self.blocos_ocultos = nn.ModuleList([
            BlocoResiduo(dimensoes=dim_oculta) for _ in range(num_blocos)
        ])
        
        print(f"[Camada Final] Classificador final mapeando {dim_oculta} -> {tam_saida}.")
        self.camada_saida = nn.Linear(dim_oculta, tam_saida)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Passa pela entrada
        out = self.camada_entrada(x)
        
        # Loop para processar todos os blocos residuais sequencialmente
        for bloco in self.blocos_ocultos:
            out = bloco(out)
            
        # Passa pela camada de classificação/regressão final
        return self.camada_saida(out)


# ==========================================
# 3. GERENCIADOR DE TREINAMENTO (Orquestrador)
# ==========================================
class GerenciadorTreinamento:
    """Gerencia o ciclo de vida de alimentação, cálculo de perda e otimização."""
    def __init__(self, modelo: nn.Module, lr: float = 0.001) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.modelo = modelo.to(self.device)
        self.criterio = nn.CrossEntropyLoss()