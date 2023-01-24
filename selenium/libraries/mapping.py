import os

environment = {'test': 'https://demoblaze.com/index.html'}


def map_environment():
    try:
        if 'ENV_NAME' in os.environ:
            env = os.environ.get("ENV_NAME", None)
            print(env)

    except Exception as ex:
        print("Missing environment", ex)
        return None
    return environment[env]
