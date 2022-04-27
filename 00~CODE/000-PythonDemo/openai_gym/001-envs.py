from gym import envs

env_ids = [spec.id for spec in envs.registry.all()]

for env_id in sorted(env_ids):
    print(env_id)
