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

from typing import Any
from uuid import uuid4

from requests import post

from .blockchain_classes import Block, Transaction


class GethServer:
    def __init__(self, host: str, port: str) -> None:
        """
        Initialise a Geth server instance.

        :param host: Host address of the server.
        :param port: Port of the server.
        """
        self.address = f'https://{host}:{port}'

    def _send_json_rpc(self, method_name: str, params: list[Any]) -> dict:
        """
        Send a JSON RPC request to the Geth Server.

        :param method_name: Name of the method to be executed by RPC
            server.
        :param params: Parameters of the request
        :return The result key of the server response.
        """
        response = post(self.address, {
            'jsonrpc': '2.0',
            'id': uuid4().int,
            'method': method_name,
            'params': params
        })
        return response.json()['result']

    @property
    def latest_block(self) -> Block:
        """
        Return the latest block from the blockchain.

        :return the latest block from the blockchain.
        """
        block_data = self._send_json_rpc(
            'eth_getBlockByNumber', ['latest', False])
        return Block(block_data['hash'],
                     block_data['parentHash'],
                     block_data['transactions'])
