import os.path
import os
import random
import string

scripts_dir = os.path.dirname(os.path.abspath(__file__))
secrets_path = os.path.join(scripts_dir, '../..', '.hz', 'secrets.toml')
secrets_template_path = os.path.join(scripts_dir, 'secrets_template.toml')
if not os.path.isfile(secrets_path):
    with open(secrets_template_path, 'r') as f:
        secrets_toml = f.read()
    # generate secret token
    N = 20
    token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
    secrets_toml = 'token_secret = "%s"\n' % (token) + secrets_toml
    with open(secrets_path, 'w') as f:
        f.write(secrets_toml)