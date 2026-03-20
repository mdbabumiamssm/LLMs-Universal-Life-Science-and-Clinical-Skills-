import re

with open("Skills/README.md", "r") as f:
    readme = f.read()

# For README, we will accept the HEAD (remote) version but inject our two skills.
# Let's just run git checkout --ours Skills/README.md to get the remote version
