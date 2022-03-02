# OpENWatch

**Op**en **E**thereum **N**FT **Watch** is an open source GPLv3 licensed project that can be used to create a database of links to NFT resources in a given Etherium network progressivelly or for one time use, the intended use case of OpENWatch is protection against NFT minters stealing artist's art without their permission and selling them.

## Usage

Simply run

```
docker-compose up --build
```

And it will start creating a database under the output folder. If you want more control over it, or you
already have a local Ethereum node, simply type

```
python OpENWatch.py --help
```

For usage information, you will need Python 3.10

### Development Limits

Currently, it fetches the first ten blocks and dies, there is no reason for this, and I will remove the limit in the v1.0,
you can do that yourselves too, simply by changing the `Dockerfile`, but I would suggest against it as the program isn't really
working 100% right now.

### Lower Level Solution

If you want to have more control over what you are doing with the fetched NFTs,
[try the Python package this program is built on](https://github.com/ArtShield/pyOpENWatch).

## Naming

The term 'watch' here was probably a bad choice, the program does not update the database in real time, the idea is that it
should be run periodically.

## The Problem with Art Thievery and NFTs

Art thievery has been [growing](https://www.nbcnews.com/tech/security/nft-art-sales-are-booming-just-artists-permission-rcna10798) [rampant](https://futurism.com/the-byte/artist-stealing-nfts) in the NFT scapes leading commercial websites to [develop software system that detect thievery](https://www.deviantart.com/team/journal/DeviantArt-Protect-Helping-Safeguard-Your-Art-884278903) however, an open source solution has been lacking, OpENWatch itself is not this solution, but it aims to enable the creation of a database of possible links that should be checked against any input data to aid in this mission.
