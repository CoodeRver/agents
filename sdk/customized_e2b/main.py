# export E2B_DOMAIN=3000-sandbox1234.example.com
# export E2B_API_KEY=admin-987654321
# 120.79.183.30 3000-sandbox1234.example.com


# Import the E2B SDK
from e2b_code_interpreter import Sandbox
from kruise_agents.patch_e2b import patch_e2b

patch_e2b(https=False)  # patch sdk

sbx: Sandbox = Sandbox.create(template="sandbox-nginx-complex-1-202604071748")
print(f"sandbox id: {sbx.sandbox_id}")
# result = sbx.run_code("print('hello, world')")
# print(f"run code result: {result}")
# text = input("enter some text to be saved to file 'text.txt' inside sandbox:  ")
# sbx.files.write("text.txt", text)
# print(f"read file from sandbox via files api: [{sbx.files.read('text.txt')}]")
# print(f"read file from sandbox via commands api: [{sbx.commands.run('cat text.txt')}]")
# input("press ENTER to kill the sandbox")
# print(sbx.kill())