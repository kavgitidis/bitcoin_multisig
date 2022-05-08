from pprint import pprint

import click

from local_utils import Mom


@click.command()
@click.option('--pub1', default=None, help='Public Key 1')
@click.option('--pub2', default=None, help='Public Key 2')
@click.option('--pub3', default=None, help='Public Key 3')
@click.option('--rpcuser', default="admin", help='Rpcuser')
@click.option('--rpcpass', default="admin", help='Rpcpassword')
@click.option('--network', default="regtest", help='Bitcoin Network')
def main(*args, **kwargs):
    click.echo(f"Public Keys Provided: {kwargs['pub1']} | {kwargs['pub2']} | {kwargs['pub3']}")
    mom = Mom(net=kwargs['network'], rpcuser=kwargs['rpcuser'], rpcpass=kwargs['rpcpass'])
    multisig_address = mom.create_multisig_address([kwargs['pub1'], kwargs['pub2'], kwargs['pub3']], 2)
    print(f"Multisig Address: {multisig_address[0]['address']}")
    pprint(multisig_address)


if __name__ == '__main__':
    main()
