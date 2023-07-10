import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


os.chdir("./audiocraft") 

os.environ["HF_HOME"] = "../huggingface"
os.environ["XFORMERS_FORCE_DISABLE_TRITON"] = "1"

os.system("python.exe app.py")