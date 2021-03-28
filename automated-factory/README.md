# Automated Factory

You Work in a automated factory and your objective is to write the function that will dispatch the packages to the correct stack, according to their volume and mass.

- A package is BULKY if it's volume (width x height x length) is greater than or equal to 1,000,000 cm3 or when one of its dimensions is greater or equal that 150 cm.

- A package is HEAVY when its mass is greater or equal that 20 kg.

You must dispatch the packages in the following stacks:

- STANDARD: standard packages (those which are not bulky nor heavy) can be handled normally.
- SPECIAL: packages that are either heavy or bulky can't be handled automatically.
- REJECTED: packages that are both heavy and bulky are rejected.