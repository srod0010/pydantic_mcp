1. Run `uv sync` command in a terminal into the project directory to setup the necessary libraries.

2. Activate the created virtual environment.

```
source .venv/bin/activate
# .venv\Scripts\activate (on Windows)
```

3. Set your `OPENAI_API_KEY`.

   This project loads the key via [python-dotenv](https://pypi.org/project/python-dotenv/), so you have two options:

   - Copy `.env.example` to `.env` and put your key there (the `.env` file is git-ignored):

     ```
     cp .env.example .env
     # then edit .env and set OPENAI_API_KEY=sk-your-real-key
     ```

   - Or export it in your shell (dotenv won't override a value already set in the environment):

     ```
     export OPENAI_API_KEY=sk-your-real-key
     ```

4. Run the `server.py` file.

```
uv run server.py
```

5. Run the `client.py` file, in a separate terminal.

```
uv run client.py
```

> **Note on transport:** the client/server use the **Streamable HTTP** transport
> (`transport="streamable-http"`, served at `http://127.0.0.1:8000/mcp`). The older
> **SSE** transport is deprecated in MCP and its redirect/handshake behaviour can cause
> the client to hang, so it has been replaced here.

6. For sampling demo, once the virtual environment is activated, go into the sampling directory.

```
cd sampling-example
```

7. Run the `client.py` file.

```
uv run client.py
```

> **Note on sampling:** the sampling example uses the **stdio** transport
> (the client spawns the server as a subprocess), so it is unaffected by the SSE
> change above. MCP sampling (`ctx.sample(...)`) is a current feature and is not deprecated.
