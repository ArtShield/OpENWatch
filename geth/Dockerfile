FROM ethereum/client-go:stable
WORKDIR /
EXPOSE 8545
CMD ["--syncmode", "light", "--http", "--http.vhosts", "*", "--fakepow", "--http.addr", "0.0.0.0", "--datadir", "/ethereum"]