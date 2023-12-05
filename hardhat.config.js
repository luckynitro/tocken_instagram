// hardhat.config.js
const { privateKey } = require('./secrets.json');

module.exports = {
  networks: {
    hardhat: {
      chainId: 1337, // Chain ID de la red de prueba de Hardhat
    },
    ropsten: {
      url: 'https://ropsten.infura.io/v3/abd0b48d19164fd792ad4fb7f1172733',
      accounts: [privateKey],
    },
    mainnet: {
      url: 'https://mainnet.infura.io/v3/abd0b48d19164fd792ad4fb7f1172733',
      accounts: [privateKey],
    },
  },
  solidity: {
    version: "0.8.20", // Actualiza esto a la versión que necesites
  },
};

