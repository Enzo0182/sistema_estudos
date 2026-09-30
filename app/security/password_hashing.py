import bcrypt



def senha_hashing(senha):
    senha_hash = bcrypt.hashpw(
        senha.encode("utf-8"),
        bcrypt.gensalt()
    )
    return senha_hash

def verificar_senha(senha, senha_hash):
    resultado = bcrypt.checkpw(senha, senha_hash)
    return resultado