# Optional: export instead of using defaults below
# export E2B_DOMAIN=sae.sandbox.com
# export E2B_API_KEY=admin-987654321

import os

os.environ.setdefault("E2B_DOMAIN", "sae.sandbox.com")
os.environ.setdefault("E2B_API_KEY", "admin-987654321")

# Import the E2B SDK
from e2b_code_interpreter import Sandbox
from kruise_agents.patch_e2b import patch_e2b

patch_e2b(https=False)  # patch sdk

sbx: Sandbox = Sandbox.create(template="code-interpreter")
print(f"sandbox id: {sbx.sandbox_id}")
result = sbx.run_code("print('hello, world')")
print(f"run code result: {result}")
text = input("enter some text to be saved to file 'text.txt' inside sandbox:  ")
sbx.files.write("text.txt", text)
print(f"read file from sandbox via files api: [{sbx.files.read('text.txt')}]")
print(f"read file from sandbox via commands api: [{sbx.commands.run('cat text.txt')}]")
input("press ENTER to kill the sandbox")
print(sbx.kill())