import docker
# import time

class DockerMonitor:
    def __init__(self):
        self.client = docker.DockerClient(
            base_url='unix:///var/run/docker.sock',
            version='auto'
        )

    def memory_(self,mem: float) -> str:
        if mem > 1024 ** 3:
            mem = round(mem / 1024 ** 3, 2)
            mem = f"{mem}GB"
        elif mem > 1024 ** 2:
            mem = round(mem / 1024 ** 2, 2)
            mem = f"{mem}MB"
        elif mem > 1024:
            mem = round(mem / 1024, 2)
            mem = f"{mem}KB"
        else:
            mem = round(mem, 2)
            mem = f"{mem}Byte"
        return mem

    def container_one(self, container_name: str):
        container = self.client.containers.get(container_name)
        return container.attrs

    def container_list(self):
        return_list = []
        for container in self.client.containers.list(all=True):
            mounts = container.attrs.get('Mounts',[])
            mount_ = [f"{mount['Source']}:{mount['Destination']}" for mount in mounts]
            env = container.attrs.get('Config').get('Env')

            container_name = container.name
            image_id = container.image.short_id
            image_name = container.image.tags[0] if container.image.tags else ""

            state_ = container.attrs.get('State', {})
            memory_stats = container.stats(stream=False).get("memory_stats", {})

            usage = memory_stats.get("usage")
            limit = memory_stats.get("limit")
            now_mem = self.memory_(usage) if usage else 0
            # now_mem = self.memory_(memory_stats.get("usage"))
            mem_limit = self.memory_(limit) if limit else 0
            host_ports = [binding['HostPort'] for bindings in container.ports.values() if bindings for binding in bindings]

            return_list.append({
                "image_id": image_id.replace("sha256:",""),
                "image_name": image_name,
                "container_id": container.short_id,
                "container_name": container_name,
                "ports": host_ports[0] if host_ports else "",
                "status": container.status,
                "is_running": state_.get("Running"),
                "is_paused": state_.get("Paused"),
                "is_restarting": state_.get("Restarting"),
                "is_OOMKilled": state_.get("OOMKilled"),
                "is_dead": state_.get("Dead"),
                "now_mem_num": usage,
                "now_mem": now_mem,
                "mem_limit_num": limit,
                "mem_limit": mem_limit,
                "mount": mount_[0] if mount_ else "",
                "env": env,
            })

                # logs = container.logs(stream=True, follow=True)

        return return_list