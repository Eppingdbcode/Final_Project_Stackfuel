# Workflow operacional

**Raiz oficial:** `C:\Users\eppin\Desktop\Final_Project_Stackfuel`
**Remoto:** `https://github.com/Eppingdbcode/Final_Project_Stackfuel.git`

## Fluxo

1. VS Code: abra somente a raiz oficial e salve todos os buffers.
2. Codex: leia os documentos centrais na ordem de `AGENTS.md`, confirme branch/status e execute uma tarefa elegível.
3. Valide: `uv sync`, smoke tests, `uv run pytest`, links e entregáveis.
4. Revise: `git status`, `git diff` e ausência de RAW, segredos e caches no staging.
5. Commit/push: somente com autorização, em branch de tarefa; nunca force push ou merge automático em `main`.

## Continuidade

Novo chat: siga `New chat startup protocol` em `AGENTS.md`. Ao concluir, atualize `PROJECT_STATUS.md` e `TASKS.md`; registre decisões em `decision_log.md`; atualize `project_handoff.md` quando o estado material mudar.

## RAW e segredos

RAW é imutável, local e não publicável sem licença/autorização. `.env`, credenciais, tokens, chaves, estudos protegidos, caches e ambientes virtuais nunca entram no Git. Somente READMEs, manifesto e checksums explicitamente permitidos podem ser versionados nas áreas protegidas.

## Comandos essenciais

```powershell
uv sync
uv add <package>
uv add --dev <package>
uv remove <package>
uv run python <script.py>
uv run pytest

git status
git branch --show-current
git diff
git diff --cached
git switch -c <branch>
git add <arquivo-revisado>
git commit -m "<mensagem>"
git push -u origin <branch>
```
