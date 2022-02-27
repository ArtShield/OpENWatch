# OpENWatch
# Copyright (C) 2021  Ege Emir Özkan

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from argparse import ArgumentParser

from openwatch import EthereumNFTWatcher
from openwatch.blockchain_classes import NFT


def callback(nft: NFT):
    print(
        f'Minted NFT hosted in {nft.token_url} by transaction {nft.minting_transaction_hash}')


def run_watcher(host: str, port: int) -> None:
    watcher = EthereumNFTWatcher(host, str(port))
    watcher.fetch_nfts_until_block(limit=10, callback=callback)


if __name__ == '__main__':
    parser = ArgumentParser('OpENWatch')
    parser.add_argument('--host', '-a', default='http://127.0.0.1',
                        help='Host address of the Ethereum Node.')
    parser.add_argument('--port', '-p', default=8545,
                        help='Port to the Ethereum Node\'s HTTP JSON RPC Server.')
    args = parser.parse_args()
    run_watcher(args.host, args.port)
