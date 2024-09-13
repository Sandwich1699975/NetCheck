from dotenv import load_dotenv


from string import Template
import logging
import os

load_dotenv(override=True)  # take environment variables from .env.

logger = logging.getLogger(__name__)

# Keys needed from .env for substitution
ENV_VARS_NEEDED = {"URL", "USERNAME", "API_TOKEN"}


def check_env() -> bool:
    """Check if the .env variables are ready to be substituted into prometheus.yml

    Returns:
        bool: True if all of the variables are OK. False otherwise
    """
    something_wrong = False

    for env_var_name in ENV_VARS_NEEDED:
        env_var_value = os.getenv(env_var_name)
        if env_var_value is None:
            # Missing variable
            logger.error(
                f"Missing .env variable: {env_var_name}. Please add it into .env")
            something_wrong = True
        elif env_var_value == "":
            # Blank variable
            logger.error(
                f"Blank .env variable: {env_var_name}. Please edit .env to define a value")
            something_wrong = True

    if not something_wrong:
        logger.info(
            "Note that previous initialisations of .env variables may still be in scope if not re-defined in .env")
        logger.info("All environment variables defined.")
    return not something_wrong


def substitute_prometheus() -> bool:
    PATH_PROMETHEUS = "prometheus.yml"
    PATH_PROMETHEUS_TEMPLATE = "prometheus.yml.template"

    # Check template file exists
    if not os.path.isfile(PATH_PROMETHEUS_TEMPLATE):
        logger.error(f"Template file: {PATH_PROMETHEUS_TEMPLATE} missing")
        return False

    with open(PATH_PROMETHEUS_TEMPLATE, "r") as r:
        TEMPLATE_CONTENT = r.read()

    TEMPLATE_PROMETHEUS = Template(TEMPLATE_CONTENT)

    # Create mapping to substitute
    template_mapping = {}
    for env_var_name in ENV_VARS_NEEDED:
        env_var_value = os.getenv(env_var_name)
        if env_var_value is None or env_var_value == "":
            logger.error(
                f"Environment variable: {env_var_name} is missing or blank")
            return False
        template_mapping[env_var_name] = env_var_value

    try:
        SUBSTITUTED_CONTENT = TEMPLATE_PROMETHEUS.substitute(template_mapping)
    except KeyError as E:
        logger.error(f"{PATH_PROMETHEUS_TEMPLATE} could not be substituted")
        logger.error(f"KeyError: {E}")
        return False

    if not os.path.isfile(PATH_PROMETHEUS):
        logger.info(f"Creating {PATH_PROMETHEUS}")

    with open(PATH_PROMETHEUS, "w") as w:
        w.write(SUBSTITUTED_CONTENT)

    logger.info(
        f"Successfully substituted {len(ENV_VARS_NEEDED)} environment variables into {PATH_PROMETHEUS}")

    return True


def main():
    # Start logger
    # Copy format from speedtest image
    # https://github.com/MiguelNdeCarvalho/speedtest-exporter/blob/8e4a39b9c0282102a9868f43b60dc99465dd0974/src/exporter.py#L14
    FORMAT_STRING = 'level=%(levelname)s datetime=%(asctime)s %(message)s'
    logging.basicConfig(encoding='utf-8',
                        level=logging.DEBUG,
                        format=FORMAT_STRING)
    logger.info(f'Started {__file__}')

    # Check if .env has been created and filled out
    if (check_env()):
        # Put those values into prometheus.yml
        if (substitute_prometheus()):
            logger.info("Completed prometheus.yml procedure successfully")
        else:
            logger.error("Failed prometheus.yml procedure")
            exit(1)
    else:
        logger.info("Skipping prometheus.yml procedure")
        exit(1)

    logger.info(f'Finished {__file__}')


if __name__ == "__main__":
    main()
