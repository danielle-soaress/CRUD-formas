# Projeto CRUD de Geometria 📐

## Descrição

Este projeto é uma aplicação Python que permite a criação, modificação e gerenciamento de figuras geométricas, como pontos, linhas, segmentos de linha, triângulos, retângulos e círculos. A interface gráfica é desenvolvida utilizando PyQt5 e o projeto é estruturado para ser compatível com diferentes sistemas operacionais, incluindo Windows e Linux.

## Funcionalidades

- ✏️**Criação e Manipulação de Figuras**: Adicione e modifique figuras geométricas como pontos, linhas, segmentos de linha, triângulos, retângulos e círculos.
- 🔢**Calculadora de Propriedades**: Calcule áreas, perímetros e verifique propriedades geométricas (por exemplo, paralelismo e distância entre pontos).
- 🖥️**Visualização Gráfica**: A interface é construída com PyQt5 e permite interação fácil com as figuras geométricas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **PyQt5**: Biblioteca Python para a elaboração da interface gráfica.
- **Git e GitHub**: Controle de versão e gerenciamento de código.

## Instalação

### Requisitos

- **Python 3.12** ou superior
- **PyQt5**

### Passos para Instalação

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```

2. **Crie e Ative um Ambiente Virtual**:
   ```bash
   python -m venv venv
   ```

   - **No Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - **No macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Compile os Recursos Qt**:

   Para garantir que as imagens e outros recursos gráficos sejam corretamente incorporados, você precisa compilar o arquivo de recursos Qt (`resources.qrc`) usando o `pyrcc5`:

   ```bash
   pyrcc5 resources.qrc -o resources_rc.py
   ```

5. **Execute o Projeto**:
   ```bash
   python main.py
   ```

## Arquivos de Recursos

As imagens utilizadas na interface gráfica são gerenciadas através de um arquivo de recursos Qt (`resources.qrc`). As imagens são incorporadas no projeto e devem estar localizadas na pasta `images/`.

## Contribuição

Se você deseja contribuir para o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas alterações.
3. Envie um pull request com uma descrição clara das suas alterações.
