from data.container_handler import get_containers

async def get_total_value(username):
    containers, extras = get_containers(username)

    if containers is None:
        return None
    
    total = sum([x[1] for x in extras.items()])

    for name, item_list in containers.items():
        total += sum(x.total for x in item_list)

    return {"total": total}