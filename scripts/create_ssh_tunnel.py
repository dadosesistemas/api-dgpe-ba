from sshtunnel import SSHTunnelForwarder
from app.core.config import settings

def start_ssh_tunnel():
    tunnel = SSHTunnelForwarder(
        (settings.SSH_HOST, settings.SSH_PORT),
        ssh_username=settings.SSH_USERNAME,
        ssh_pkey=settings.SSH_PRIVATE_KEY_PATH,
        remote_bind_address=(settings.REMOTE_DB_HOST, settings.REMOTE_DB_PORT)
    )
    tunnel.start()
    print(f"SSH Tunnel iniciado na porta local: {tunnel.local_bind_port}")
    return tunnel

if __name__ == "__main__":
    tunnel = start_ssh_tunnel()
    input("Pressione Enter para encerrar o tunnel...")
    tunnel.stop()