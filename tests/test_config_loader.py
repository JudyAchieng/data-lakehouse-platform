from ingestion.common.config_loader import load_config


def test_load_config():

    config = load_config()

    print(config)

    assert config is not None