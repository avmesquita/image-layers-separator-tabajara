# Image Color Layer Extractor

Utilitário em Python para análise e segmentação de imagens baseadas em agrupamento de cores (K-Means). O projeto isola faixas de cores dominantes de uma imagem de entrada e exporta cada agrupamento como uma camada PNG transparente independente.

## 📋 Pré-requisitos

* Python 3.8+
* Ambiente Linux / macOS / WSL

## 🚀 Como Executar

Para simplificar o fluxo de trabalho, o projeto inclui o script `start.sh`, que gerencia automaticamente a criação do ambiente virtual, a instalação das dependências e a execução.

1. **Dar permissão de execução ao script de arranque:**

```bash
chmod +x start.sh
```

2. **Executar o projeto:**
```bash
bash
./start.sh
```

---

## 🛠️ Instalação Manual

Se preferires configurar o ambiente passo a passo manualmente:

1. **Criar e ativar o ambiente virtual (`venv`):**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. **Instalar as dependências:**

```bash
pip install -r requirements.txt
```

3. **Executar o script:**

```bash
python3 script.py "Screenshot from 2026-11-01 08-22-14.png"
```

---

## ⚙️ Estrutura de Ficheiros

```text
.
├── script.py          # Código principal de processamento de imagem (K-Means)
├── start.sh           # Script de automação (Cria venv, instala deps e executa)
├── requirements.txt   # Dependências do projeto (Pillow, numpy, scikit-learn)
└── README.md          # Documentação do repositório
```

---

## 🎨 Como Funciona a Segmentação

O algoritmo processa a imagem em três etapas principais:
1. Converte os pixels para o espaço de cor RGB.
2. Aplica **K-Means Clustering** para agrupar pixels com tonalidades semelhantes conforme o parâmetro `n_colors`.
3. Gera ficheiros `.png` isolados com fundo transparente (`RGBA`) para cada camada identificada.


