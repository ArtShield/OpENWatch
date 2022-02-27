class InvalidMintTransactionException(Exception):
    """
    Given transaction is not a mint transaction but was
        handled as one.
    """

    def __init__(self, transaction_hash: str, *args: object) -> None:
        super().__init__(
            f'Transaction with the hash {transaction_hash} is not a mint transaction', *args)
