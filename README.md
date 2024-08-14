## Integração com o Modelo LLaMA3 8B
***
Este repositório contém o código necessário para executar o modelo LLaMA3 da Meta, uma poderosa ferramenta de processamento de linguagem natural. O objetivo deste projeto é fornecer uma integração simplificada e eficiente com o modelo para diversos usos em projetos de NLP.

### Instruções de Instalação e Execução
#### 1. Configuração do Ambiente
Siga as instruções do repositório oficial do LLaMA3: Para obter detalhes sobre o modelo e seu uso, visite o repositório oficial do LLaMA3.
Baixe os arquivos do modelo:

Acesse a página do Meta-Llama-3.1-8B no Hugging Face.
Faça o cadastro e solicite a liberação para acesso ao modelo, conforme necessário.
Coloque os arquivos do modelo:

Após o download, coloque todos os arquivos na pasta Meta-Llama-3.1-8B no diretório do projeto.
#### 2. Instalação de Dependências
Instale as bibliotecas necessárias:
Utilize o arquivo (requirements.txt)[requirements.txt] para instalar as bibliotecas necessárias. Execute o comando:

``` bash
pip install -r requirements.txt
```
Caso necessário, utilize os arquivos .whl encontrados na pasta (bibliotecas)[bibliotecas] para instalar as dependências adicionais.

#### 3. Execução do Código
Execute o script principal:
Para iniciar a execução do modelo, rode o script (IA_Hard-LLaMA.py)[IA_Hard-LLaMA.py]:

``` bash
python IA_Hard-LLaMA.py
```

### Comentários de Uso
O código foi testado em uma GPU RTX 2080, com o comprimento das respostas limitado a 100 caracteres. Embora tenha funcionado corretamente, observe que a GPU foi utilizada em sua totalidade.
As respostas geradas pelo modelo levaram aproximadamente 2 minutos para serem completadas. Este tempo pode variar com base na capacidade da GPU e nas configurações do modelo.

### Notas Adicionais
Certifique-se de ter espaço suficiente na memória da GPU para carregar o modelo.
Para otimizar o tempo de resposta, considere ajustar os parâmetros do modelo e o tamanho das respostas conforme necessário.
Se você tiver dúvidas ou encontrar problemas, por favor, abra uma issue no repositório para obter suporte.
