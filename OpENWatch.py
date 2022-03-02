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
from logging import getLogger

from pyopenwatch import EthereumNFTWatcher, NFT

from database import NFTStore


def run_watcher(host: str, port: int, log_level: int, wait: bool, output: str, block_count: int) -> None:
    nft_store = NFTStore(output)
    try:
        watcher = EthereumNFTWatcher(host, str(port), log_level)
        watcher.fetch_nfts_until_block(
            limit=block_count, callback=nft_store.insert, wait=wait)
    except Exception as e:
        print('Error occurred during NFT fetching.')
        print(e)
    finally:
        nft_store.close()


if __name__ == '__main__':
    parser = ArgumentParser('OpENWatch', )
    parser.add_argument('--host', '-a', default='http://127.0.0.1',
                        help='Host address of the Ethereum Node.')
    parser.add_argument('--port', '-p', default=8545,
                        help='Port to the Ethereum Node\'s HTTP JSON RPC Server.')
    parser.add_argument('--log_level', '-l', default=40,
                        help='Log level issued to logger, compliant with Python.',
                        type=int)
    parser.add_argument('--wait', '-w', action='store_true',
                        help='Wait for the host and port to stop syncing'
                        )
    parser.add_argument(
        '--output', '-o', help='Path to output database file.', default='nft.sqlite')
    parser.add_argument('--block_count', '-c',
                        help='Maximum number of blocks to be fetched', default=10)
    args = parser.parse_args()
    run_watcher(args.host, args.port, args.log_level,
                args.wait, args.output, args.block_count)
