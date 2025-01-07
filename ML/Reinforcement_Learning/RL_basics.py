import gym
from gym import envs
envids = [spec.id for spec in envs.registry.all()]
for envid in sorted(envids):
    print(envid)

env = gym.make('BattleZone-v0')
env.reset()
for _ in range(100):
    env.render(mode='rgb_array')
    env.step(env.action_space.sample())
env.env.close()