# Scanner de Imagens

Este projeto é um Scanner de Imagens que identifica as bordas de uma foto contendo uma folha de papel e recorta a imagem para que fique somente a folha. A aplicação utiliza técnicas de processamento de imagem para detectar e extrair a folha da foto original.

## Funcionalidades

- **Detecção de Bordas**: Identifica as bordas da folha de papel na imagem.
- **Recorte da Imagem**: Recorta a imagem para que contenha somente a folha de papel.
- **Correção de Perspectiva**: Ajusta a perspectiva da folha de papel, se necessário, para que fique alinhada corretamente.
- **Exportação de Imagem**: Salva a imagem recortada em um arquivo.

## Requisitos

- Python 3.x
- Bibliotecas:
  - OpenCV
  - NumPy

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/scanner-de-imagens.git
    cd scanner-de-imagens
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Estrutura do Projeto

- `main.py`: Script principal que executa o processamento da imagem.
- `scanner.py`: Contém a lógica para detecção de bordas e recorte da imagem.
- `utils.py`: Funções auxiliares para manipulação de imagens.
- `data/`: Pasta para armazenar as imagens de entrada e saída.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para mais informações, entre em contato pelo email: contato@daviga.dev.br
