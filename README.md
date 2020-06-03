# scrapy-user-agent-rotator

Este módulo tem por finalidade permitir rotacionar user-agents no [Scrapy](https://scrapy.org/). 

## Instalação

- Maneira mais simples, via **pip**:
    ```bash
    pip install scrapy-user-agent-rotator
    ```
## Como usar

- No arquivo de configuração de seu projeto Scrapy, adicione as seguintes linhas (**settings.py**):
    ```python
    DOWNLOADER_MIDDLEWARES = {
        ...,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'user_agent_rotator.middlewares.RotateUserAgentMiddleware': 500,
    }
    ```
- Defina a lista de user-agents, ative o módulo e defina um uso mínimo e máximo de cada user-agent (o uso de um user-agent será aleatório entre esses números) (**settings.py**):
    ```python
    USER_AGENTS = ['user-agent-1', 'user-agent-2',...,'user-agent-n']
    ROTATE_USER_AGENT_ENABLED = True
    MIN_USER_AGENT_USAGE = #uso mínimo de user-agent
    MAX_USER_AGENT_USAGE = #uso máximo de user-agent
    ```

- É possível conferir o user-agent usado no site: https://www.whatismybrowser.com/detect/what-is-my-user-agent 
