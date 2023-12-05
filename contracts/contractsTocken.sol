// contracts/Token.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Token {
    mapping(address => uint256) private _balances;
    address private _owner;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() {
        _owner = msg.sender;
        _balances[msg.sender] = 1000000;
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    function transfer(address to, uint256 value) public returns (bool) {
        require(value <= _balances[msg.sender], "Insufficient balance");
        require(to != address(0), "Transfer to the zero address");

        _balances[msg.sender] -= value;
        _balances[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }
}
