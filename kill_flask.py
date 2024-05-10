import psutil

def find_and_kill_flask(identifier, port=5000):
    """Find and kill a Flask process running on a given port with a specific identifier."""
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # Check if this is the Flask process with the correct identifier
            if identifier in " ".join(proc.cmdline()):
                for conn in proc.connections(kind='inet'):
                    if conn.laddr.port == port:
                        proc.kill()
                        print(f"Killed Flask process with identifier {identifier} on port {port} with PID {proc.pid}")
                        return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print("No Flask process found with the specified identifier on the port.")
    return False

if __name__ == "__main__":
    find_and_kill_flask('flask_app_unique_id')
