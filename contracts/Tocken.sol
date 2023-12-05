// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    // Constructor: se ejecuta una vez al deploy del contrato
    constructor() ERC20("MyToken", "MTK") {
        // Emite la cantidad total de tokens en el deploy
        _mint(msg.sender, 1000000000000000000000000); // 1,000 MTK con 18 decimales
    }
}

