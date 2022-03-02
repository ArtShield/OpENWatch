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

from sqlite3 import connect, OperationalError

from pyopenwatch import NFT


class NFTStore:
    def __init__(self, filename: str = 'nft') -> None:
        self.db = connect(filename)
        self._init_db()

    def _init_db(self) -> None:
        """
        Initialise the databases.
        """
        cursor = self.db.cursor()
        try:
            cursor.execute('SELECT * FROM nfts WHERE id=1')
        except OperationalError:
            cursor.execute('CREATE TABLE nfts ('
                           'id INTEGER PRIMARY KEY, '
                           'url TEXT, '
                           'token_id TEXT, contract_address TEXT, '
                           'transaction_hash TEXT, '
                           'found_on INTEGER'
                           ')')

    def insert(self, nft: NFT) -> None:
        """Insert an NFT to the store

        Insert an NFT record to the store.

        :param nft: NFT data to be inserted to the store.
        :type nft: NFT
        """
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO '
                       'nfts(url, token_id, contract_address, transaction_hash, found_on) '
                       'VALUES (?, ?, ?, ?, DateTime(\'now\'))', (
                           nft.token_url,
                           str(nft.token_id),
                           nft.issuing_contract_address,
                           nft.minting_transaction_hash
                       ))
        self.db.commit()

    def close(self) -> None:
        self.db.close()
