import argparse
import config


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Get values to generate new wireguard config file')
    parser.add_argument('name',
                        type=str)

    parser.add_argument('ip',
                        type=int)

    parser.add_argument('key',
                        type=str)

    return parser


def create_config_file(user_private_key: str, user_name: str, user_ip: int) -> None:
    config_file_content = f""" 
[Interface]
PrivateKey = {user_private_key}
Address = 10.0.0.{user_ip}/32
DNS = {config.DNS}

[Peer]
PublicKey = {config.SERVER_PUBLIC_KEY}
Endpoint = {config.ENDPOINT}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 20    
    """
    with open(f"ready_configs/{user_name}.conf", "w") as conf_file:
        conf_file.write(config_file_content)


def main(args: argparse.Namespace) -> None:
    ip = args.ip
    name = args.name
    key = args.key
    create_config_file(key, name, ip)


if __name__ == "__main__":
    parser = create_arg_parser()
    args = parser.parse_args()

    main(args)
